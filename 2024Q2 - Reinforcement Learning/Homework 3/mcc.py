"""
Large amount of code borrowed from Dr. Robbins
"""
import gymnasium as gym
import numpy as np
from scipy.stats import t
import collections
import matplotlib.pyplot as plt
from sklearn import metrics
import time

class MCC():
    def __init__(self,
                 eps_a = 0.5,
                 eps_b = 0.5,
                 qinit = 1.0,
                 ) -> None:
        self.env = gym.make('CartPole-v1')
        """ Algorithm Parameters for Hyperparameter Tuning """
        # eps-greedy stepsize rule
        self.eps_a = eps_a
        self.eps_b = eps_b
        self.qinit = qinit
        # number of Intervals per dimension
        # e.g., using 11 intervals indicates 12 discrete states per dim
        self.Sintervals = 11 

        """ """
        self.qrange = (0,500)    # range of q-values for environment (for setting qinit)
        self.gamma = 0.999       # discount rate
        #Z = 10 # number of algorithm replications
        #M = int(0.5e3) # number of episodes
        self.test_freq = 25 # policy evaluation test frequency (1/test_freq)
        self.num_test_reps = 30 # number of replications per test 
        self.offset = 0 # random number generator seed manual offset 

        """Discretizing the Space"""
        self.Slow = np .array([-2.5,-4.0,-0.3,-1.9])
        self.Shigh = np.array([2.5, 3.3, 0.3, 3.9])
        Srange = self.Shigh-self.Slow
        self.Sunit = Srange/self.Sintervals
        Ssize = (self.Sintervals+1) * np.ones(len(self.env.observation_space.low)).astype(int) # intervals * number of dimensions
        self.SAsize = np.append(Ssize,self.env.action_space.n) # size of state-action space


        self.Gzm = [] # record each episode's cumulative reward to measure online performance
        self.GzmTest = []

        # Initialize the data structure to hold the Top 2 scores and VEA parameters 
        self.num_best_scores = 10
        self.best_scores = [{'ETDR': -np.inf, 'ETDR_hw': np.inf, 'Q': None} for _ in range(self.num_best_scores)]

        self.total_training_reps = 0
        self.avg_execution_time = 0.0
        self.total_episodes = 0


    def ordinal(self,n):   # create string for ordinal number
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n%10, 4)]
        if 11 <= (n % 100) <= 13:
            suffix = 'th'
        return str(n) + suffix

    def epsilon(self,n) :
        return self.eps_a/(1+n)**self.eps_b

    def phi(self, Scont) : 
        """convert continuous state to discrete 2D state var representation"""
        return np.round((Scont-self.Slow)/self.Sunit).astype(int)

    def confinterval(self, data, alpha=0.05):
        n = np.size(data)               # number of data points
        se = np.std(data)/np.sqrt(n)    # standard error
        ts = t.ppf(1-alpha/2, n-1) # t-score
        mean = np.mean(data)
        halfwidth = ts*se
        return mean, halfwidth

    def update_best_scores(self,mean, hw, Q):
        # Find the first score that mean is greater than
        for i in range (len(self.best_scores)):
            if mean-hw > self.best_scores[i]['ETDR'] -self.best_scores[i]['ETDR_hw']:
                # insert best score and attendant parameters
                self.best_scores.insert(i, {'ETDR': np.copy(mean), 'ETDR_hw': np.copy(hw), 'Q': np.copy(Q)})
                # We only want the top scores, so remove the last one 
                self.best_scores.pop()
                return True
        return False

    def update_and_print(self,episode_number,mean,hw,Q):
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
            terminated = False
            truncated = False
            # initialize episode reward
            Gtest = 0
            # initialize the system by resetting the environment, obtain state var
            state = self.env.reset(seed=seed_mult*1000+rep)[0]
            while not (terminated or truncated) :
                # select action with highest q-value
                action = np.argmax(Q[tuple(self.phi(state))])
                # apply action and observe system information
                state, reward, terminated, truncated, _ = self.env.step(action)
                # update episode cumulative reward
                Gtest += reward
            test_data[rep] = Gtest
        mean, hw = self.confinterval(test_data)
        return mean, hw

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
        plt.title(f'MCC (on-policy) Algorithm Performance, {Z} reps, {np.round(self.avg_execution_time,1)} min/rep\
                  \ngamma={self.gamma}, eps_a={self.eps_a}, eps_b={self.eps_b}, g0={self.qinit}, |S|/d={self.Sintervals+1} \nMean Max EETDR: {meanMaxTestEETDR:>6.2f} +/- {maxTestHW:4.2f}, Mean Time-Avg EETDR = {meanAULC:>6.2f} +/- {hwAULC:4.2f}) \nSuperlative Policy EETDR: {maxETDR:>6.2f} +/- {maxETDRhw:4.2f}', fontsize =9)
        plt.legend(loc="lower right",fontsize=7)
        plt.xlim([-0.05*M, 1.05*M])
        plt.ylim([-5,505])
        plt.grid(which='both')
        plt.show()

    def display_best_policy(self):
        """display best policy using greedy-only approach as an animation"""
        # initialize environment
        env = gym.make('CartPole-v1', render_mode='human')
        indBestCILB,_,_ = self.find_superlative()
        Q = np.copy(self.best_scores[indBestCILB]['Q'])
        # number of reps to show
        num_reps_show = 10
        # initialize test data structure
        test_data = np.zeros((num_reps_show)) # original test_data = np.zeros((num_runs_show))
        # perform test replications
        for rep in range(num_reps_show):
            # initialize episode complete flag (i.e., when system enters terminal state)
            # done = False
            terminated = False
            truncated =False
            # initialize episode reward
            Gtest = 0
            # initialize the system by resetting the environment, obtain state var
            state = env.reset(seed=1000+rep+self.offset)[0]
            while not (terminated or truncated):
                # select action with highest q-value
                action = np.argmax(Q[tuple(self.phi(state))])
                # apply action and observe system information
                state, reward, terminated, truncated, _ = env.step(action)
                # update episode cumulative reward
                Gtest += reward
            test_data[rep] = Gtest
            print(f"Episode {rep} ETDR: {np.round(Gtest,4)}")
            #time.sleep(1)
        env.close()
        mean, hw = self.confinterval(test_data)
        print (f"\n Rendered episodes... ETDR CI: {np.round(mean,1)} +/- {np.round(hw,1)}")
        return

    def find_superlative(self, num_test_reps=30):
        # initialize list of means and half-widths for testing top policies
        mean_values = []
        hw_values = []
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

    def train_on_policy(self, num_episodes, replications):
        time_start = time.perf_counter()
        # loop through each algorithm replication for current design run
        for z in range(replications):
            # initialize Q-table
            Q = self.qinit*np.ones(self.SAsize)*(self.qrange[1]-self.qrange[0]) +self.qrange[0]
            # initialize state-action counter
            C = np.zeros(self.SAsize)

            print(f"\nMCC (on-policy)(eps_a={self.eps_a:<3.2f},eps_b={self.eps_b:<3.2f},q0={self.qinit}) rep {z}...")

            # loop through each episode
            for m in range(num_episodes):
                # initialize episode complete flag (when system enters terminal state)
                terminated, truncated = False, False
                # initialize state, action, and reward queues
                state_queue, action_queue, reward_queue = collections.deque([]),collections.deque([]),collections.deque([])
                # reset environment and set seeds
                state = self.env.reset(seed=int(z*1e6+m+self.offset))[0]
                np.random.seed(int(z*1e6+m+self.offset))    # set numpy random number generator seed

                # implement epsilon-greedy exploration mechanism
                if np.random.rand() > self.epsilon(m):                   # With epsilon probability:
                    action = np.argmax(Q[tuple(self.phi(state))])   # act greedy by taking best action at current state using Q bar
                else:
                    action = self.env.action_space.sample()              # act randomly with probability epsilon to explore

                # MCC episode generation, forward loop
                while not (terminated or truncated):
                    state_queue.append(state)# record state
                    action_queue.append(action)# record action
                    # apply action and observe system information
                    state, reward, terminated, truncated, _ = self.env.step(action)
                    reward_queue.append(reward)# record reward
                    # select action with epsilon-greedy exploration mechanism
                    if np.random.rand() > self.epsilon(m):                   # With epsilon probability:
                        action = np.argmax(Q[tuple(self.phi(state))])   # act greedy by taking best action at current state using Q bar
                    else:
                        action = self.env.action_space.sample()              # act randomly with probability epsilon to explore

                Gm = 0 # initialize episode total discounted reward

                # MCC update l-table, backward loop
                while len(state_queue) > 0:
                    # define state, action, reward from ends of queues
                    s = state_queue.pop()       # pop() method removes last value
                    s = self.phi(s)             # discretize state
                    a = action_queue.pop()      
                    r = reward_queue.pop()
                    Gm = self.gamma*Gm + r      # update total discounted reward
                    sa = tuple(np.append(s,a))  # specify state-action variable
                    C[sa] += 1                  # update state-action counter
                    Q[sa] += (Gm-Q[sa])/C[sa]   # update Q-table via incremental update mechanism

                self.Gzm.append((z,Gm))  # record performance

                # test current policy (as represented by current w and iht) every test_freq episodes
                if m % self.test_freq == 0:
                    mean, hw = self.evaluate_policy_test(Q, self.num_test_reps)
                    self.GzmTest.append((z, m, mean, hw))

                    # update best scores if necessary
                    self.update_and_print(m,mean,hw,Q)

            # last test of current algorithm replication
            mean, hw = self.evaluate_policy_test(Q, self.num_test_reps)
            self.GzmTest.append((z,num_episodes,mean,hw))

            # update best scores if necessary
            self.update_and_print(m,mean,hw,Q)

        self.total_episodes += num_episodes
        # Update execution time record
        execution_time = time.perf_counter()-time_start
        total_time = (self.total_training_reps * self.avg_execution_time) + execution_time
        self.total_training_reps += replications
        self.avg_execution_time = total_time/self.total_training_reps

    def train_off_policy(self, num_episodes, replications):
        time_start = time.perf_counter()
        # loop through each algorithm replication for current design run
        for z in range(replications):
            # initialize Q-table
            Q = self.qinit * np.ones(self.SAsize) * (self.qrange[1] - self.qrange[0]) + self.qrange[0]
            # initialize state-action counter
            C = np.zeros(self.SAsize)
            # initialize policy
            pi = np.argmax(Q,axis=-1)

            print(f"\nMCC (off-policy)(eps_a={self.eps_a:<3.2f},eps_b={self.eps_b:<3.2f},q0={self.qinit}) rep {z}...")

            # loop through each episode
            for m in range(num_episodes):
                # initialize episode complete flag (when system enters terminal state)
                terminated, truncated = False, False
                # initialize state, action, and reward queues
                state_queue, action_queue, reward_queue = collections.deque([]), collections.deque([]), collections.deque([])
                # reset environment and set seeds
                state = self.env.reset(seed=int(z*1e6 + m + self.offset))[0]
                np.random.seed(int(z*1e6 + m + self.offset))    # set numpy random number generator seed

                # Produce a random soft policy
                b = np.random.rand(*Q.shape) * Q.max()
                # MCC episode generation, forward loop, using b
                while not (terminated or truncated):
                    if np.random.rand() > self.epsilon(m):              # With epsilon probability:
                        action = np.argmax(b[tuple(self.phi(state))])   # act greedy by taking best action at current state using Q bar
                    else:
                        action = self.env.action_space.sample()         # act randomly with probability epsilon to explore
                    state_queue.append(state)  # record state
                    action_queue.append(action)  # record action
                    # apply action and observe system information
                    state, reward, terminated, truncated, _ = self.env.step(action)
                    reward_queue.append(reward)  # record reward

                Gm = 0  # initialize episode total discounted reward
                W = 1.0 # Initial weighted importance

                # MCC update Q-table, backward loop with weighted importance sampling
                while len(state_queue) > 0:
                    s = state_queue.pop()   # pop() method removes last value
                    s = self.phi(s)         # discretize state
                    a = action_queue.pop()
                    r = reward_queue.pop()
                    sa = tuple(np.append(s, a))         # specify state-action variable

                    Gm = self.gamma * Gm + r            # update total discounted reward
                    C[sa] += W                          # update state-action counter with weight
                    Q[sa] += (W / C[sa]) * (Gm - Q[sa]) # update Q-table via weighted incremental update mechanism
                    pi[s] = np.argmax(Q[tuple(s)])
                    if a != pi[*s]: continue            # exit inner loop (proceed to next episode)
                    W *= 1 / b[sa]

                self.Gzm.append((z, Gm))  # record performance

                # test current policy (as represented by current Q) every test_freq episodes
                if m % self.test_freq == 0:
                    mean, hw = self.evaluate_policy_test(Q, self.num_test_reps)
                    self.GzmTest.append((z, m, mean, hw))

                    # update best scores if necessary
                    self.update_and_print(m, mean, hw, Q)

            # last test of current algorithm replication
            mean, hw = self.evaluate_policy_test(Q, self.num_test_reps)
            self.GzmTest.append((z, num_episodes, mean, hw))

            # update best scores if necessary
            self.update_and_print(m, mean, hw, Q)

        self.total_episodes += num_episodes
        # Update execution time record
        execution_time = time.perf_counter() - time_start
        total_time = (self.total_training_reps * self.avg_execution_time) + execution_time
        self.total_training_reps += replications
        self.avg_execution_time = total_time / self.total_training_reps



"""
Test

num_episodes=int(0.5e3)
replications=5

pol = MCC()
pol.train_off_policy(num_episodes, replications)
pol.show_results()
"""
