import numpy as np
import gymnasium as gym
import matplotlib.pyplot as plt
from scipy.stats import t
from sklearn import metrics
from abc import abstractmethod

class MDPBase():
    def __init__(self, env, **kwargs) -> None:
        self.env = env
        self.algorithm_name = kwargs.get('self.algorithm_name', '')

        """ Tunable Hyperparameters """
        self.eps_a      = kwargs.get('eps_a',1.0)   # Eps-Greedy stepsize rule
        self.eps_b      = kwargs.get('eps_b',0.5)   # Eps-Greedy stepsize rule
        self.alpha_a    = kwargs.get('alpha_a',1.0) # Learning Rate
        self.alpha_b    = kwargs.get('alpha_b',0.5) # Learning Rate
        self.qinit      = kwargs.get('qinit',1.0)
        self.gamma      = kwargs.get('gamma',0.999) # discount rate

        """ Discretizing the Space """
        self.num_actions= env.action_space.n        # Discrete Action Space
        discrete_states = 12
        self.Sintervals = discrete_states - 1
        self.Slow       = np.array(env.observation_space.low)
        self.Shigh      = np.array(env.observation_space.high)
        Srange          = self.Shigh-self.Slow
        self.Sunit      = Srange/self.Sintervals
        Ssize           = discrete_states * np.ones(len(env.observation_space.low)).astype(int)
        self.SAsize     = np.append(Ssize,self.num_actions)  # state-action space

        """ Testing Parameters """
        self.test_freq = 25 # policy evaluation test frequency (1/test_freq)
        self.num_test_reps = 30 # number of replications per test 
        self.offset = 0 # random number generator seed manual offset 

        """ Data Store """
        # record each episode's cumulative reward to measure online performance
        self.Gzm = [] 
        self.GzmTest = []
        # Hold the Top 10 scores and VEA parameters 
        self.num_best_scores = 10 
        self.best_scores = [{'ETDR': -np.inf, 'ETDR_hw': np.inf, 'Q': None}
                            for _ in range(self.num_best_scores)]
        self.total_training_reps = 0
        self.avg_execution_time = 0.0
        self.total_episodes = 0

        # Set range of q-values for environment (for setting qinit)
        match self.env.spec.id:
            case 'CartPole-v1' : self.qrange = [0,500]
            case 'MountainCar-v0' : self.qrange = [-200,-100]
            case _: self.qrange = [-200,200] # A WAG if unknown environment


    def ordinal(self,n):   # create string for ordinal number
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n%10, 4)]
        if 11 <= (n % 100) <= 13:suffix = 'th'
        return str(n) + suffix

    def epsilon(self,n) :
        return self.eps_a/(1+n)**self.eps_b

    def alpha(self,n):
        return self.alpha_a/(1+n)**self.alpha_b

    def phi(self, Scont) : 
        """convert continuous state to discrete 2D state var representation"""
        a = np.round((Scont-self.Slow)/self.Sunit).astype(int)
        return np.clip(a,0,self.Sintervals)

    def confinterval(self, data, alpha=0.05):
        n   = np.size(data)             # number of data points
        se  = np.std(data)/np.sqrt(n)   # standard error
        ts  = t.ppf(1-alpha/2, n-1)     # t-score
        mean = np.mean(data)
        halfwidth = ts*se
        return mean, halfwidth

    def update_best_scores(self, mean, hw, Q):
        # Find the first score that mean is greater than
        for i in range (len(self.best_scores)):
            lower_bound = self.best_scores[i]['ETDR'] - self.best_scores[i]['ETDR_hw']
            if mean - hw > lower_bound:
                # Insert best score and attendant parameters
                self.best_scores.insert(i, {'ETDR': np.copy(mean), 'ETDR_hw': np.copy(hw),
                                            'Q': np.copy(Q)})
                self.best_scores.pop()  # Remove least best score
                return True
        return False

    def update_and_print(self, episode_number, mean, hw, Q):
        # update best scores if necessary
        best_scores = self.best_scores
        if self.update_best_scores(mean,hw,Q):
            print(f"   Test... Episode: {episode_number:>4}, "
                  + f"EETDR CI: {mean:>6.2f} +/- {hw:4.2f} New Top {self.num_best_scores} "
                  + f"EETDR 95CILB -- Q recorded")
        else:
            print(f"   Test... Episode: {episode_number:>4}, "
                  + f"EETDR CI: {mean:>6.2f} +/- {hw:4.2f}\n"
                  + f"*------* Current Top 5 Reliable EETDRs: "
                  + "".join([f"{best_scores[i]['ETDR']:>6.2f}, " for i in range(5)])
                  #+ f"{best_scores[0]['ETDR']:>6.2f}, {best_scores[1]['ETDR']:>6.2f}, \
                  #{best_scores[2]['ETDR']:>6.2f}, {best_scores[3]['ETDR']:>6.2f}, \
                  #{best_scores[4]['ETDR']:>6.2f}"
                  )

    def evaluate_policy_test(self, Q, num_reps=30, seed_mult=1):
        # initialize test data structure
        test_data = np.zeros((num_reps))
        # run num_test_reps replications per test
        for rep in range(num_reps):
            # initialize episode complete flag (i.e., when system enters terminal state)
            terminated, truncated = False, False
            # initialize episode reward
            Gtest = 0
            # initialize the system by resetting the environment, obtain state var
            state = self.env.reset(seed=seed_mult*1000+rep)[0]
            while not (terminated or truncated) :
                # select action with highest q-value
                action = np.argmax(Q[tuple(self.phi(state))])
                # apply action and observe system information
                state, reward, terminated, truncated, _ = self.env.step(action)
                Gtest += reward    # update episode cumulative reward
            test_data[rep] = Gtest
        mean, hw = self.confinterval(test_data)
        return mean, hw

    def title(self,reps):
        s = (f"{self.algorithm_name} Algorithm Performance, {reps} reps, "
             + f"{np.round(self.avg_execution_time,1)} sec/rep\n"
             + f"gamma={self.gamma}, eps_a={self.eps_a}, eps_b={self.eps_b}, g0={self.qinit}, "
             + f"|S|/d={self.Sintervals+1}\n")
        return s

    def show_results(self):
        Z = self.total_training_reps
        M = self.total_episodes

        npGzmTest = np.array(self.GzmTest)
        size = np.shape(npGzmTest)

        TestEETDR = np.reshape(npGzmTest[:,2],(Z,int(size[0]/Z)))

        maxTestEETDR = np.max(TestEETDR,axis=1)
        meanMaxTestEETDR = np.mean(maxTestEETDR)
        maxTestSE = np.std(maxTestEETDR)/np.sqrt(Z)
        maxTestHW = t.ppf(1-0.05/2,Z-1)*maxTestSE

        avgTestEETDR = np.mean(TestEETDR, axis=0)
        avgTestSE = np.std(TestEETDR,axis=0)/np.sqrt(Z)
        avgTestHW = t.ppf(1-0.05/2,Z-1)*avgTestSE

        AULC = [metrics.auc(np.arange(0,M+1,self.test_freq), TestEETDR[z,:])/M for z in range(Z)]
        meanAULC = np.round(np.mean(AULC),1)
        hwAULC = t.ppf(1-0.05/2, Z-1)*np.std(AULC)/np.sqrt(Z)

        _, maxETDR, maxETDRhw = self.find_superlative()

        plt.figure(0)
        X = np.arange(0,M+1,self.test_freq)
        plt.plot(X, avgTestEETDR, marker='o', ms=3, mec='k', linewidth=1, label='Mean EETDR')
        plt.fill_between(X, avgTestEETDR+avgTestHW, avgTestEETDR-avgTestHW, linestyle = '--',
                        linewidth=0.5, facecolor='blue', alpha=0.15, label='95% Halfwidth')
        plt.xlabel('Episode')
        plt.ylabel('Mean Estimated Expected\nTotal Discounted Reward (EETDR)')
        sub_title = (f"Mean Max EETDR: {meanMaxTestEETDR:>6.2f} +/- {maxTestHW:4.2f}, "
                     + f"Mean Time-Avg EETDR: {meanAULC:>6.2f} +/- {hwAULC:4.2f})\n"
                     + f"Superlative Policy EETDR: {maxETDR:>6.2f} +/- {maxETDRhw:4.2f}")
        plt.title(self.title(reps=Z)+sub_title, fontsize =9)
        plt.legend(loc="lower right",fontsize=7)
        plt.xlim([-0.05*M, 1.05*M])
        #plt.ylim([-5,505])
        plt.grid(which='both')
        plt.show()

    def display_best_policy(self):
        """display best policy using greedy-only approach as an animation"""
        # initialize environment
        env = gym.make(self.env.spec.id, render_mode='human')
        indBestCILB,_,_ = self.find_superlative()
        Q = np.copy(self.best_scores[indBestCILB]['Q'])
        # number of reps to show
        num_reps_show = 10
        # initialize test data structure
        test_data = np.zeros((num_reps_show)) # original test_data = np.zeros((num_runs_show))
        # perform test replications
        for rep in range(num_reps_show):
            terminated, truncated = False, False
            # initialize episode reward
            Gtest = 0
            # initialize the system by resetting the environment, obtain state var
            state_continuous = env.reset(seed=1000+rep+self.offset)[0]
            state = self.phi(state_continuous)
            while not (terminated or truncated):
                action = np.argmax(Q[tuple(self.phi(state))])  # select action with highest q-value
                # apply action and observe system information
                state_continuous, reward, terminated, truncated, _ = env.step(action)
                state = self.phi(state_continuous)
                # update episode cumulative reward
                Gtest += reward
            test_data[rep] = Gtest
            print(f"Episode {rep} ETDR: {np.round(Gtest,4)}")
        env.close()
        mean, hw = self.confinterval(test_data)
        print (f"\n Rendered episodes... ETDR CI: {np.round(mean,1)} +/- {np.round(hw,1)}")
        return

    def find_superlative(self, num_test_reps=30):
        # initialize list of means and half-widths for testing top policies
        mean_values, hw_values = [], []
        # loop through top policies stored in best_scores to find superlative policy
        for i, score in enumerate(self.best_scores):
            mean, hw = self.evaluate_policy_test(score['Q'], num_test_reps,2)
            print(f"\nBest VFA ({self.ordinal (i+1)}) test... \EETDR CI: {mean:>6.2f}+/-{hw:4.2f}")
            mean_values.append(mean)
            hw_values.append(hw)
        
        # determine superlative policy and record its mean and half-width
        indBestCILB = np.argmax(np.array(mean_values)-np.array(hw_values))
        maxETDR = mean_values[indBestCILB]
        maxETDRhw = hw_values[indBestCILB]
        return indBestCILB, maxETDR, maxETDRhw

    def get_results(self):
        Z = self.total_training_reps
        M = self.total_episodes
        npGzmTest = np.array(self.GzmTest)
        size = np.shape(npGzmTest)
        TestEETDR = np.reshape(npGzmTest[:,2],(Z,int(size[0]/Z)))
        maxTestEETDR = np.max(TestEETDR,axis=1)
        meanMaxTestEETDR = np.mean(maxTestEETDR)
        maxTestSE = np.std(maxTestEETDR)/np.sqrt(Z)
        maxTestHW = t.ppf(1-0.05/2,Z-1)*maxTestSE
        AULC = [metrics.auc(np.arange(0,M+1,self.test_freq), TestEETDR[z,:])/M for z in range(Z)]
        meanAULC = np.round(np.mean(AULC),1)
        hwAULC = t.ppf(1-0.05/2, Z-1)*np.std(AULC)/np.sqrt(Z)
        _, maxETDR, maxETDRhw = self.find_superlative()
        return (maxETDR, maxETDRhw, meanMaxTestEETDR, maxTestHW, meanAULC, hwAULC, 
                self.avg_execution_time)

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def train(self, num_replications, num_episodes, verbose=False):
        pass



import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from scipy.stats.qmc import LatinHypercube
from joblib import Parallel, delayed
from datetime import datetime
from time import perf_counter
from statsmodels.formula.api import ols
import statsmodels.api as sm

class LHS_Experiment():
    def __init__(self, algorithm, env, features, **kwargs) -> None:
        self.algorithm = algorithm
        self.env = env
        self.features = features
        # ["alpha_a", "alpha_b", "eps_a", "eps_b"]
        self.column_names = ["Run Index"] + features + ["Sup EETDR", "Sup EETDR hw", 
                             "Mean Max EETDR", "Mean Max EETDR hw", "Time-Avg EETDR", 
                             "Time-Avg EETDR hw", "Secs per run", "Score"]
        self.NUM_CPU_PROCS  = kwargs.get('num_cpu_procs',6)     # Number of CPU threads to use
        self.num_episodes   = kwargs.get('episodes',int(1e3))
        self.replications   = kwargs.get('replications',10)
        self.runs           = kwargs.get('runs',50)
        self.verbose        = kwargs.get('verbose',False)

        self.results_table = None
        self.factor_table = None


    def single_experiment(self, run_index:int, factors:np.ndarray) -> tuple[int,float,float,float]:
        run_start_time = perf_counter()
        #algo = self.algorithm(*factors)
        algo = self.algorithm(self.env, **dict(zip(self.features,factors)))
        algo.train(self.replications, self.num_episodes)
        maxETDR, maxETDRhw, meanMaxTestEETDR, maxTestHW, meanAULC, hwAULC, time =algo.get_results()
        alg_score = 0.6*(meanMaxTestEETDR-maxTestHW) + 0.4*(meanAULC-hwAULC)
        if self.verbose: print(f"Complete experiment run {run_index} with a score of "
                               + f"{alg_score:.2f} ({perf_counter() - run_start_time:.1f}s)")
        return run_index, maxETDR, maxETDRhw, meanMaxTestEETDR, maxTestHW, meanAULC, hwAULC, time

    def parallel_lhs(self, rng_seed=0):
        """ Execute LHS Experiment in Parallel """
        sampler = LatinHypercube(len(self.features), scramble=False, 
                                 optimization="lloyd", seed=rng_seed)
        factor_table = sampler.random(n=self.runs)
        if self.verbose: print(f"\nInitializing LHS experiment with {self.runs} runs...")
        start_time = perf_counter()
        parallel_manager = Parallel(n_jobs = self.NUM_CPU_PROCS)
        run_list = (delayed(self.single_experiment)(run_index, factor_table[run_index]) 
                    for run_index in range (self.runs) )
        #execute the list of run_experiment() calls in parallel
        if self.verbose: print ("\nExecuting experiment...")
        results_table = parallel_manager(run_list)
        results_table = np.array(results_table)
        if self.verbose: print (f"\n\nCompleted experiment ({perf_counter() - start_time:.3f}s)")

        # Combine the factor and results tables, add column headers, and save the data to a CSV.
        # Compute algorithm run score, the avg 95% CI lower bound for max and mean performance.
        maxEETDR_95CI_LB = results_table[:,3] - results_table[:,4]
        meanEETDR_95CI_LB = results_table[:,5] - results_table[:,6]
        score = 0.6*maxEETDR_95CI_LB + 0.4*meanEETDR_95CI_LB
        results_table = np.column_stack((results_table[:,0], factor_table, 
                                         results_table[:,1:], score))
        # save data for performance scatter plot
        self.results_table = np.row_stack((self.column_names, results_table))
        self.factor_table = factor_table

    def export_results(self):
        filename_DOE = (f"{self.algorithm.name}_results_DOE_" 
                        + datetime.now().strftime('%Y%m%d_%H%M%S') + ".csv")
        np.savetxt(filename_DOE, self.results_table, delimiter = ",", fmt = "%s")

    def anova(self):
        # Input data
        X = self.factor_table

        # Generate full factorial polynomial function up to degree 2
        poly = PolynomialFeatures(2)
        X_poly = poly.fit_transform(X)

        # Clean up the feature names
        input_features = self.column_names[1: 1 + len(self.features)] # Run index and features
        feature_names = [name.replace(' ','_').replace('^','_pow_').replace('*','_times_')
                        for name in poly.get_feature_names_out(input_features=input_features)]
        df = pd.DataFrame(X_poly, columns=feature_names)

        # define response variable
        max_ind = self.column_names.index("Sup EETDR")
        mean_ind = self.column_names.index("Mean Max EETDR")
        maxEETDR_95CI_LB  = (np.array(self.results_table[1:,max_ind],float) 
                           - np.array(self.results_table[1:,max_ind+1],float))
        meanEETDR_95CI_LB = (np.array(self.results_table[1:,mean_ind],float) 
                           - np.array(self.results_table[1:,mean_ind+1],float))
        score = 0.6*maxEETDR_95CI_LB + 0.4*meanEETDR_95CI_LB
        df['AlgScore'] = score

        # Create the formula string for the OLS model
        # Exclude the first column (the constant term) from the predictors
        predictors = '+'.join(df.columns[1:-1]) # Exclude '1' and 'y'
        formula = f'AlgScore ~ {predictors}'

        # Create and fit the OLS model
        model = ols(formula, data=df)
        results = model.fit()

        # Display the summary
        print ("\n\n" )
        print (results.summary())

        # Perform ANOVA and display the table
        anova_results = sm.stats.anova_lm(results, typ=2)
        print(anova_results)

    def plot_results(self,x_var = "Mean Max EETDR", y_var = "Time-Avg EETDR"):
        x_ind = self.column_names.index(x_var)
        y_ind = self.column_names.index(y_var)
        x = np.array(self.results_table[1:,x_ind],float) # 0-index appears to be title
        y = np.array(self.results_table[1:,y_ind],float) # 0-index appears to be title
        # create scatter plot
        plt. scatter(x, y, label=f"{self.algorithm.name} -- {self.replications} reps per run, "
                     + f"{self.num_episodes} episodes per rep")
        # setting title and labels
        plt.title(f"{self.algorithm.name} LHS DOE Performance Results")
        plt.xlabel(x_var)
        plt.ylabel(y_var)
        # grid on
        plt.grid()
        # legend on
        plt.legend(loc='upper left', fontsize=7)
        # display the plot
        plt.show()

    def plot_param_comparison(self):
        y = np.array(self.results_table[1:,-1],float) # 0-index appears to be title
        # create scatter plot
        for i,param in enumerate(self.features):
            plt.scatter(np.array(self.results_table[1:,i],float), y , label=param)
        #plt.scatter(np.array(self.results_table[1:,1],float), y, label="eps_a")
        #plt.scatter(np.array(self.results_table[1:,2],float), y, label="eps_b")
        #plt.scatter(np.array(self.results_table[1:,3],float), y, label="Q-init")
        # setting title and labels
        plt.title(f"{self.algorithm.name} LHS DOE Performance Results -- "
                     + f"{self.replications} reps per run, {self.num_episodes} episodes per rep")
        plt.ylabel("Score")
        # grid on
        plt.grid()
        # legend on
        plt.legend(loc='upper left', fontsize=7)
        # display the plot
        plt.show()


