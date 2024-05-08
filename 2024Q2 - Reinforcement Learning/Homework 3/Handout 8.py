"""
DSOR 646 - Reinforcement Learning
Dr. Mathew Robbins
Handout for Lesson 8

Solve OpenAI Gym CartPole-vl Environment via Monte Carlo Control
    (on-policy, every-visit) algorithm

"""

# import required package libraries 
import gymnasium as gym
import numpy as np
import time
from scipy.stats import t
import matplotlib.pyplot as plt
from sklearn import metrics
import collections

# set output precision for numpy
np.set_printoptions(precision=4, suppress=True)

#create Farama OpenAI Gym environment
env = gym.make('CartPole-v1')

print (f"\nFarama-OpenAI Gym version: {gym.__version__}")

# Observation and action space
print("The observation space: {}".format(env.observation_space))
print("The action space: {}".format(env.action_space))

""" Algorithm Parameters for Hyperparameter Tuning (Begin) """

# eps-greedy stepsize rule
eps_a = 0.5     # (*)   #   0.5
eps_b = 0.5     # (*)   #   0.5
def epsilon (n) :
    return eps_a/(1+n)**eps_b

# Q init
qinit = 1.0     # (*)   #   1.0

# number of Intervals per dimension
# e.g., using 11 intervals indicates 12 discrete states per dim
Sintervals = 11 # (*)   #   11

""" Algorithm Parameters for Hyperparamter Tuning (End) """

# range of q-values for environment (for setting qinit)
qrange = (0,500)

#discount rate
gamma = 0.999

# number of algorithm replications
Z = 10

# number of episodes
M = int(0.5e3)

# policy evaluation test frequency
test_freq = 25 # 5% of M

# number of replications per test 
num_test_reps = 30

# random number generator seed manual offset 
offset = 0

# continuous state space -- number of dimensions
num_state_dims = len(env.observation_space.low)

# discrete action space -- number of actions 
num_actions = env.action_space.n

# define reference points for discretizing state space
# Slow = np. array (env.observation_space.low)
# Shigh - np. array (env.observation_space.high)
# overwrite environment infinite boundaries with finite ones
Slow = np .array([-2.5,-4.0,-0.3,-1.9])
Shigh = np.array([2.5, 3.3, 0.3, 3.9])
Srange = Shigh-Slow
Sunit = Srange/Sintervals
Ssize = (Sintervals+1) * np.ones(num_state_dims).astype(int)

# size of state-action space
SAsize = np.append(Ssize,num_actions)

# convert continuous state to discrete representation 
def phi(Scont) : # returns discrete 2D state var representation 
    return np.round((Scont-Slow)/Sunit).astype(int)

# record each episode's cumulative reward to measure online performance
Gzm = []
GzmTest = []

# Initialize the data structure to hold the Top Z scores and VEA parameters 
num_best_scores = Z
best_scores = [{'ETDR': -np.inf, 'ETDR_hw': np.inf, 'Q': None} for _ in range(num_best_scores)]

def update_best_scores(mean, hw, Q, best_scores):
    # Find the first score that mean is greater than
    for i in range (len(best_scores)):
        if mean-hw > best_scores[i]['ETDR'] -best_scores[i]['ETDR_hw']:
            # insert best score and attendant parameters
            best_scores.insert(i, {'ETDR': np.copy(mean), 'ETDR_hw': np.copy(hw), 'Q': np.copy(Q)})
            # We only want the top scores, so remove the last one 
            best_scores.pop()
            return True
    return False

# function for computing confidence interval 
def confinterval(data, alpha=0.05):
    n = np.size(data)               # number of data points
    se = np.std(data)/np.sqrt(n)    # standard error
    ts = t.ppf(1-alpha/2, n-1) # t-score
    mean = np.mean(data)
    halfwidth = ts*se
    return mean, halfwidth

# define test function
def evaluate_policy_test(Q, num_reps=num_test_reps, seed_mult=1):
    # initialize test data structure
    test_data = np.zeros((num_reps))
    # run num_test_reps replications per test
    for rep in range(num_reps):
        # initialize episode complete flag (i.e., when system enters terminal state)
        # done = False
        terminated = False
        truncated = False
        # initialize episode reward
        Gtest = 0
        # initialize the system by resetting the enivronment, obtain state var
        state = env.reset(seed=seed_mult*1000+rep)[0]
        while not (terminated or truncated) :
            # select action with highest q-value
            action = np.argmax(Q[tuple(phi(state))])
            # apply action and observe system information
            state, reward, terminated, truncated, _ = env.step(action)
            # update episode cumulative reward
            Gtest += reward
        test_data[rep] = Gtest
    mean, hw = confinterval(test_data)
    return mean, hw

# start timer for loading problem into memory
tic = time. perf_counter()

# loop through each algorithm replication for current design run
for z in range (Z) :
    # initialize Q-table
    Q = qinit*np.ones(SAsize)*(qrange[1]-qrange[0]) +qrange[0]
    # initialize state-action counter
    C = np. zeros (SAsize)

    print(f"\nMCC (on-policy)(eps_a={eps_a:<3.2f},eps_b={eps_b:<3.2f},q0={qinit}) rep {z}...")

    # loop through each episode
    for m in range(M):
        # initialize episode complete flag (when system enters terminal state)
        terminated = False
        truncated = False
        # generate an episode following policy pi(s|a)
        # set numpy random number generator seed
        np.random.seed(int(z*1e6+m+offset))
        # initialize the system by resetting the environment, setting gym
        #   random number generator seed
        #   want each replication-episode combination to have its own seed
        state = env.reset(seed=int(z*1e6+m+offset))[0]
        # implement epsilon-greedy exploration mechanism
        if np.random.rand() > epsilon(m):
            # act greedy by exploiting current knowledge
            # take best action at current state using Qbar
            action = np.argmax(Q[tuple(phi(state))])
        else:
            # act randomly with probability epsilon to explore
            #action = np.random.randint(num_actions)
            action = env.action_space.sample()

        # initialize state, action, and reward queues
        state_queue = collections.deque([])
        action_queue = collections.deque([])
        reward_queue = collections.deque([])
        # MCC episode generation, forward 100p
        while not (terminated or truncated):
            # record state
            state_queue.append(state)
            # record action
            action_queue.append(action)
            # apply action and observe system information
            state, reward, terminated, truncated, _ = env.step(action)
            # record reward
            reward_queue.append(reward)
            # select action
            # implement epsilon-greedy exploration mechanism
            if np.random.rand() > epsilon(m):
                # act greedy by exploiting current knowledge
                # take best action at current state using Qbar
                action = np.argmax(Q[tuple(phi(state))])
            else:
                # act randomly with probability epsilon to explore
                #action = np.random.randint(num_actions)
                action = env.action_space.sample()

        # initialize episode total discounted reward
        Gm = 0

        # MCC update l-table, backward loop
        while len(state_queue) > 0:
            # define state, action, reward from ends of queues
            s = state_queue.pop()   # pop() method removes last value
            s = phi(s) # discretize state
            a = action_queue.pop()
            r = reward_queue.pop()
            # update total discounted reward
            Gm = gamma*Gm + r
            # specify state-action variable
            sa = tuple(np.append(s,a))
            # update state-action counter
            C[sa] += 1
            # update Q-table via incremental update mechanism
            Q[sa] += (Gm-Q[sa])/C[sa]

        # record performance
        # print (f"\nEpisode: {m}, Cumulative reward: {Gm}")
        Gzm.append((z,Gm))

        # test current policy (as represented by current w and iht) every test_freg episodes
        if m % test_freq == 0:
            mean, hw = evaluate_policy_test(Q)
            GzmTest.append((z, m, mean, hw))

            # update best scores if necessary
            if update_best_scores(mean, hw, Q, best_scores):
                print(f"   Test... Episode: {m:>4}, EETDR CI: {mean:>6.2f} +/- {hw:4.2f} New Top {Z} EETDR 95CILB -- Q recorded")
            else:
                print(f"   Test... Episode: {m:>4}, EETDR CI: {mean:>6.2f} +/- {hw:4.2f}")

    # last test of current algorithm replication
    mean, hw = evaluate_policy_test(Q)
    GzmTest.append((z,M,mean,hw))

    # update best scores if necessary
    if update_best_scores(mean,hw,Q,best_scores):
        print(f"   Test... Episode: {m:>4}, EETDR CI: {mean:>6.2f} +/- {hw:4.2f} New Top {Z} EETDR 95CILB -- Q recorded")
    else:
        print(f"   Test... Episode: {m:>4}, EETDR CI: {mean:>6.2f} +/- {hw:4.2f}\n *------* Current Top 5 Reliable EETDRs: {best_scores[0]['ETDR']:>6.2f}, {best_scores[1]['ETDR']:>6.2f}, {best_scores[2]['ETDR']:>6.2f}, {best_scores[3]['ETDR']:>6.2f}, {best_scores[4]['ETDR']:>6.2f}")


toc = time.perf_counter()
print (f"\nExecuted {Z} algorithm reps in {toc - tic:0.4f} seconds.")

print(f" \nValidation testing of policies with Top {num_best_scores} best reliable EETDRs...")

# create string for ordinal number 
def ordinal(n):
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n%10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix

# initialize list of means and half-widths for testing top policies
mean_values = []
hw_values = []

# loop through top policies stored in best_scores to find superlative policy
for i, score in enumerate(best_scores):
    mean, hw = evaluate_policy_test(score['Q'], 2*num_test_reps,2)
    print(f"\nBest VFA ({ordinal (i+1)}) test...  EETDR CI: {mean:>6.2f} +/- {hw:4.2f}")
    mean_values.append(mean)
    hw_values.append(hw)

# determine superlative policy and record its mean and half-width
indBestCILB = np.argmax(np.array(mean_values)-np.array(hw_values))
maxETDR = mean_values[indBestCILB]
maxETDRhw = hw_values[indBestCILB]

# set Q equai to best parameters
Q = np.copy(best_scores[indBestCILB]['Q'])

"""
plot performance results
"""

npGzmTest = np.array(GzmTest)
size = np.shape(npGzmTest)
TestEETDR = np.reshape(npGzmTest[:,2],(Z,int(size[0]/Z)))

maxTestEETDR = np.max (TestEETDR,axis=1)
meanMaxTestEETDR = np.mean (maxTestEETDR)
maxTestSE = np.std(maxTestEETDR)/np.sqrt(Z)
maxTestHW = t.ppf(1-0.05/2,Z-1)*maxTestSE

avgTestEETDR = np.mean (TestEETDR, axis=0)
avgTestSE = np.std(TestEETDR,axis=0)/np.sqrt(Z)
avgTestHW = t.ppf(1-0.05/2,Z-1)*avgTestSE

AULC = [metrics.auc(np.arange(0,M+1,test_freq), TestEETDR[z,:])/M for z in range(Z)]
meanAULC = np.round(np.mean(AULC),1)
hwAULC = t.ppf(1-0.05/2, Z-1)*np.std(AULC)/np.sqrt(Z)

plt.figure(0)
plt.plot(np.arange(0,M+1,test_freq),avgTestEETDR, marker = 'o', ms = 3, mec = 'k', linewidth = 1, label='Mean EETDR')
plt.plot(np.arange(0,M+1,test_freq),avgTestEETDR+avgTestHW, color='blue', linestyle = '--', linewidth = 0.5, label='95% Halfwidth')
plt.plot(np.arange(0,M+1,test_freq),avgTestEETDR-avgTestHW, color='blue', linestyle = '--', linewidth = 0.5)
plt.xlabel('Episode')
plt.ylabel('Mean Estimated Expected\nTotal Discounted Reward (EETDR)')
plt.title(f'MCC (on-policy) Algorithm Performance, {Z} reps, {np.round((toc-tic)/(Z)/60,1)} min/rep\ngamna={gamma}, eps_a={eps_a}, eps_b={eps_b}, g0={qinit}, |S|/d={Sintervals+1} \nMean Max EETDR: {meanMaxTestEETDR:>6.2f} +/- {maxTestHW:4.2f}, Mean Time-Avg EETDR = {meanAULC:>6.2f} +/- {hwAULC:4.2f}) \nSuperlative Policy EETDR: {maxETDR:>6.2f} +/- {maxETDRhw:4.2f}', fontsize =9)

plt.legend(loc="lower right",fontsize=7)
plt.xlim([-0.05*M, 1.05*M])
plt.ylim([-5,505])
plt.grid(which='both')
plt.show()

# display best policy using greedy-only approach
def displayBestPolicy():
    # initialize environment
    env = gym.make('CartPole-v1', render_mode='human')
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
        state = env.reset(seed=1000+rep+offset)[0]
        while not (terminated or truncated):
            # select action with highest q-value
            action = np.argmax(Q[tuple(phi(state))])
            # apply action and observe system information
            state, reward, terminated, truncated, _ = env.step(action)
            # update episode cumulative reward
            Gtest += reward
        test_data[rep] = Gtest
        print(f"Episode {rep} ETDR: {np.round(Gtest,4)}")
        time.sleep(1)
    env.close()
    mean, hw = confinterval(test_data)
    print (f"\n Rendered episodes... ETDR CI: {np.round(mean,1)} +/- {np.round(hw,1)}")
    return

# uncomment and execute to watch reps
# displayBestPolicy()