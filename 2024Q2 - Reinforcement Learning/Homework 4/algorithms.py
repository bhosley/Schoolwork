import numpy as np
import gymnasium as gym
import matplotlib.pyplot as plt
from scipy.stats import t
from sklearn import metrics
from time import perf_counter
from abc import abstractmethod
from collections import deque

class MDPBase():
    def __init__(self, env, **kwargs) -> None:

        assert env, "Error: An environment must be defined to run the algorithm. Please provide a valid Gymnasium environment."
        self.env = env

        """ Tunable Hyperparameters """
        self.eps_a      = kwargs.get('eps_a',0.5)   # Eps-Greedy stepsize rule
        self.eps_a      = kwargs.get('eps_a',0.5)   # Eps-Greedy stepsize rule
        self.alpha_a    = kwargs.get('alpha_a',1.0) # Learning Rate
        self.alpha_b    = kwargs.get('alpha_b',0.5) # Learning Rate
        self.qinit      = kwargs.get('qinit',1.0)

        """ Tunable (But un-tuned) Hyperparameters """
        self.gamma      = 0.999     # discount rate

        """ Discretizing the Space """
        self.Sintervals = 11 # e.g., using 11 intervals indicates 12 discrete states per dim
        self.Slow       = np.array(env.observation_space.low)
        self.Shigh      = np.array(env.observation_space.high)
        Srange          = self.Shigh-self.Slow
        self.Sunit      = Srange/self.Sintervals
        Ssize           = (self.Sintervals+1) * np.ones(len(self.env.observation_space.low)).astype(int) # intervals * number of dimensions
        num_actions     = env.action_space.n            # Discrete Action Space
        self.SAsize = np.append(Ssize,num_actions)      # size of state-action space

        """ Data Store """
        self.Gzm = [] # record each episode's cumulative reward to measure online performance
        self.GzmTest = []
        # Initialize the data structure to hold the Top 10 scores and VEA parameters 
        self.num_best_scores = 10 
        self.best_scores = [{'ETDR': -np.inf, 'ETDR_hw': np.inf, 'Q': None} for _ in range(self.num_best_scores)]




        self.algorithm_name = kwargs.get('self.algorithm_name', '')

        # number of Intervals per dimension
        self.qrange = (0,500)    # range of q-values for environment (for setting qinit)
        self.test_freq = 25 # policy evaluation test frequency (1/test_freq)
        self.num_test_reps = 30 # number of replications per test 
        self.offset = 0 # random number generator seed manual offset 
        """Discretizing the Space"""
        self.total_training_reps = 0
        self.avg_execution_time = 0.0
        self.total_episodes = 0




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
        n = np.size(data)               # number of data points
        se = np.std(data)/np.sqrt(n)    # standard error
        ts = t.ppf(1-alpha/2, n-1) # t-score
        mean = np.mean(data)
        halfwidth = ts*se
        return mean, halfwidth

    def update_best_scores(self, mean, hw, Q):
        # Find the first score that mean is greater than
        for i in range (len(self.best_scores)):
            if mean - hw > self.best_scores[i]['ETDR'] - self.best_scores[i]['ETDR_hw']:
                # insert best score and attendant parameters
                self.best_scores.insert(i, {'ETDR': np.copy(mean), 'ETDR_hw': np.copy(hw), 'Q': np.copy(Q)})
                # We only want the top scores, so remove the last one 
                self.best_scores.pop()
                return True
        return False

    def update_and_print(self, episode_number, mean, hw, Q):
        # update best scores if necessary
        best_scores = self.best_scores
        if self.update_best_scores(mean,hw,Q):
            print(f"   Test... Episode: {episode_number:>4}, EETDR CI: {mean:>6.2f} +/- {hw:4.2f} New Top {self.num_best_scores} EETDR 95CILB -- Q recorded")
        else:
            print(f"   Test... Episode: {episode_number:>4}, EETDR CI: {mean:>6.2f} +/- {hw:4.2f}\n *------* Current Top 5 Reliable EETDRs: {best_scores[0]['ETDR']:>6.2f}, {best_scores[1]['ETDR']:>6.2f}, {best_scores[2]['ETDR']:>6.2f}, {best_scores[3]['ETDR']:>6.2f}, {best_scores[4]['ETDR']:>6.2f}")

    def evaluate_policy_test(self, Q, num_reps, seed_mult=1):
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
        s = f'{self.algorithm_name} Algorithm Performance,\
            {reps} reps, {np.round(self.avg_execution_time,1)} sec/rep\n\
            gamma={self.gamma},\
            eps_a={self.eps_a}, eps_b={self.eps_b}, g0={self.qinit},\
            |S|/d={self.Sintervals+1}\n'
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

        avgTestEETDR = np.mean (TestEETDR, axis=0)
        avgTestSE = np.std(TestEETDR,axis=0)/np.sqrt(Z)
        avgTestHW = t.ppf(1-0.05/2,Z-1)*avgTestSE

        AULC = [metrics.auc(np.arange(0,M+1,self.test_freq), TestEETDR[z,:])/M for z in range(Z)]
        meanAULC = np.round(np.mean(AULC),1)
        hwAULC = t.ppf(1-0.05/2, Z-1)*np.std(AULC)/np.sqrt(Z)

        _, maxETDR, maxETDRhw = self.find_superlative()

        plt.figure(0)
        plt.plot(np.arange(0,M+1,self.test_freq),avgTestEETDR, marker = 'o', ms = 3, mec = 'k', linewidth = 1, label='Mean EETDR')
        plt.plot(np.arange(0,M+1,self.test_freq),avgTestEETDR+avgTestHW, color='blue', linestyle = '--', linewidth = 0.5, label='95% Halfwidth')
        plt.plot(np.arange(0,M+1,self.test_freq),avgTestEETDR-avgTestHW, color='blue', linestyle = '--', linewidth = 0.5)
        plt.xlabel('Episode')
        plt.ylabel('Mean Estimated Expected\nTotal Discounted Reward (EETDR)')
        sub_title = f'Mean Max EETDR: {meanMaxTestEETDR:>6.2f} +/- {maxTestHW:4.2f},\
            Mean Time-Avg EETDR = {meanAULC:>6.2f} +/- {hwAULC:4.2f})\n\
            Superlative Policy EETDR: {maxETDR:>6.2f} +/- {maxETDRhw:4.2f}'
        plt.title(self.title(reps=Z)+sub_title, fontsize =9)
        plt.legend(loc="lower right",fontsize=7)
        plt.xlim([-0.05*M, 1.05*M])
        plt.ylim([-5,505])
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
            mean, hw = self.evaluate_policy_test(score['Q'], 2*num_test_reps,2)
            print(f"\nBest VFA ({self.ordinal (i+1)}) test...  EETDR CI: {mean:>6.2f} +/- {hw:4.2f}")
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
        return maxETDR, maxETDRhw, meanMaxTestEETDR, maxTestHW, meanAULC, hwAULC, self.avg_execution_time

    @abstractmethod
    def train():
        return



class SARSA(MDPBase):
    def __init__(self, env, nm1, # Number of steps for computing n-step returns; nm1 = 0 indicates 1-step return
                 **kwargs) -> None:
        super().__init__(env, **kwargs)
        self.nm1 = nm1
        self.algorithm_name = f'{nm1+1}-step SARSA'


    def train(self):
        """ Training Loop """
        time_start = perf_counter()
        # perform each algorithm replication
        for z in range(Z):
            # initialize Q-table
            Q = self.qinit*np.ones(self.SAsize) * (self.qrange[1] - self.qrange[0]) + self.qrange[0]
            # initialize state-action counter
            C = np.zeros(self.SAsize)
            print(f"\n{self.nm1+1} - step SARSA(alpha_a = {self.alpha_a:<3.2f}, alpha_b={self.alpha_b:<3.2f}, eps_a={eps_a:<3.2f}, eps_b={eps_b:<3.2f}, |S|/d {Sintervals}, qinit={qinit}, rep {z}...")
            for m in range(M):
                # initialize episode complete flag (when system enters terminal state)
                terminated = False
                truncated = False
                # Initialize episode reward
                Gm = 0
                # Set random number generator seed
                np.random.seed(int(z*1e6+m+1e5*self.offset))
                # Initialize the system by resetting the environment, obtain state var
                state_continuous = env.reset(seed=int(z*1e6+m))[0]
                # Transform continuous state to discrete representation via aggregation
                state = self.phi(state_continuous)
                # Initialize state array, records of states
                state_queue = deque([state])
                # Compute number of times state has been visited
                cs = np.sum(C[tuple(state)])
                # Select action based on epsilon-greedy exploration mechanism
                if np.random.rand() > self.epsilon(cs):
                    # Act greedy by exploiting current knowledge
                    action = np.argmax(Q[tuple(state)])  # using Q
                else:
                    # Act randomly with probability epsilon to explore
                    action = np.random.randint(0, num_actions)
                # Initialize action array, record of actions
                action_queue = deque([action])
                # Initialize reward array, record of rewards
                reward_queue = deque([])

                # SARSA main loop (first nml transitions)
                for _ in range(nm1):
                    # Apply action and observe system information
                    next_state_continuous, reward, terminated, truncated, _ = env.step(action)
                    # Transform continuous state to discrete representation
                    next_state = phi(next_state_continuous)
                    # Append reward to reward array
                    reward_queue.append(reward)
                    # Update episode cumulative reward
                    Gm += reward
                    # Append next state to state array
                    state_queue.append(next_state)
                    # Compute number of times state has been visited
                    cs = np.sum(C[tuple(next_state)])
                    # Select action based on epsilon-greedy exploration mechanism
                    if np.random.rand() > epsilon(cs):
                        # Act greedy by exploiting current knowledge
                        next_action = np.argmax(Q[tuple(next_state)])
                    else:
                        # Act randomly with probability epsilon to explore
                        next_action = np.random.randint(0, num_actions)
                    # Append next action to action array
                    action_queue.append(next_action)
                # SARSA main loop (first nml transitions until end of episode)
                while not (terminated or truncated):
                    # Apply action and observe system information
                    next_state_continuous, reward, terminated, truncated, _ = env.step(action_queue[-1])
                    # Transform continuous state to discrete representation
                    next_state = phi(next_state_continuous)
                    # Append next state to state array
                    state_queue.append(next_state)
                    # Append reward to reward array
                    reward_queue.append(reward)
                    # Update episode cumulative reward
                    Gm += reward
                    # Compute number of times state has been visited
                    cs = np.sum(C[tuple(next_state)])
                    # select action based on epsilon-greedy exploration mechanism
                    if np.random.rand() > epsilon(cs):
                        # act greedy by exploiting current knowledge
                        # take best action at current state using Q
                        next_action = np.argmax(Q[tuple(next_state)])
                    else:
                        # act randomly with probability epsilon to explore
                        next_action = np.random.randint(0, num_actions)
                    # append next action to action array
                    action_queue.append(next_action)
                    # temporal difference learning mechanism
                    qhat = np.dot(reward_queue, gamma**np.array(range(len(reward_queue)))) + \
                        (1-terminated) * gamma**len(reward_queue) * Q[tuple(next_state) + (next_action,)]
                    # update state-action counter (for earliest state-action in queue)
                    state_action = tuple(state_queue[0]) + (action_queue[0],)
                    C[state_action] += 1
                    # determine number of times current state-action pair visited
                    csa = C[state_action]
                    # update Q
                    Q[state_action] = (1-alpha(csa)) * Q[state_action] + alpha(csa) * qhat
                    # update state, action, and reward arrays by removing oldest values
                    state_queue.popleft()
                    action_queue.popleft()
                    reward_queue.popleft()
                    
                    # SARSA main loop (episode complete, update for last nml transitions)
                    # identify last state action in trajectory
                    last_state_action = tuple(state_queue[-1]) + (action_queue[-1],)
                    while len(reward_queue)>0:
                        # compute qhat
                        qhat = np.dot(reward_queue, gamma**np.array(range(len(reward_queue)))) + \
                            (1-terminated) * gamma**len(reward_queue) * Q[last_state_action]
                        # update state-action counter
                        state_action = tuple(state_queue[0]) + (action_queue[0],)
                        C[state_action] += 1
                        # determine number of times current state-action pair visited
                        csa = C[state_action]
                        # update Q
                        Q[state_action] = (1-alpha(csa)) * Q[state_action] + alpha(csa) * qhat
                        # update state, action, and reward arrays by removing oldest values
                        state_queue.popleft()
                        action_queue.popleft()
                        reward_queue.popleft()
                    
                    # record performance
                    print(f"\nIn Episode: {m}, Cumulative reward: {Gm}")
                    Gzm.append((z, Gm))
                    
                    # test current policy (as represented by current Q) every test_freq episodes
                    if m % test_freq == 0:
                        mean, hw = evaluate_policy_milestone_test(Q, num_test_reps)
                        GzmTest.append((z,m, mean, hw))
                    # update best EETDR scores if necessary
                    if update_best_scores(mean, hw, Q, best_scores):
                        print(f"Test... Episode: {m:>4}, EETDR CI: {mean:>6.1f} +/- {hw:4.1f}) *** New Top {num_best_scores} Reliable EETDR")
                    else:
                        print(f"Test... Episode: {m:>4}, EETDR CI: {mean:>6.1f} +/- {hw:4.1f}")

            # last test of current algorithm replication
            mean, hw = evaluate_policy_milestone_test(Q, num_test_reps)
            GzmTest.append((z,M, mean, hw))

            # update best EETDR scores if necessary
            if update_best_scores(mean, hw, Q, best_scores):
                print(f"Test... Episode: {M:>4}, EETDR CI: {mean:>6.1f} +/- {hw:4.1f}) *** New Top {num_best_scores} Reliable EETDR")
            else:
                print(f"Test... Episode: {M:>4}, EETDR CI: {mean:>6.1f} +/- {hw:>4.1f}\n *-------* Current Top 5 Reliable EETDRs: {best_scores[0]['ETDR']:>6.1f}, {best_scores[1]['ETDR']:>6.1f}, {best_scores[2]['ETDR']:>6.1f}, {best_scores[3]['ETDR']:>6.1f}, {best_scores[4]['ETDR']:>6.1f}")

        toc = time.perf_counter()
        print(f"\nExecuted {Z} algorithm reps in {toc - tic:0.4f} seconds.")
        print(f"\nIdentifying superlative policy via testing of policies from Top {num_best_scores} Reliable EETDRs...")





import gymnasium as gym

env = gym.make('MountainCar-v0')
one_sarsa = SARSA(env, nm1=0)

