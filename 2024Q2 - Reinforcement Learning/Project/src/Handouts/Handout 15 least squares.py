"""
DSOR 646 - Reinforcement Learning
Dr. Matthew Robbins
Lesson 15 Handout -- Least Squares Policy Iteration
Farama OpenAI Gymnasium MountainCar-v0 Environment
"""

import gymnasium as gym
import numpy as np
import time
from scipy.stats import t
import matplotlib.pyplot as plt
from sklearn import metrics

# Farama OpenAI Environment
env = gym.make('MountainCar-v0')
print(f"\nFarama Foundation Gymnasium version: {gym.__version__}\n")

# Observation and action space
print("The observation space: {}".format(env.observation_space))
print("The action space: {}".format(env.action_space))

""" Algorithm parameters for tuning """

# episode-based weight smoothing
alpha_a = 0.25                  # 0.25
alpha_b = 0.75                  # 0.75
def alpha(n):
    return alpha_a/(1+n)**alpha_b

# episode-based eps-greedy stepsize rule
eps_a = 1.0                     # 1.0
eps_b = 0.25                    # 0.25
def epsilon (n) :
    return eps_a/(1+n)**eps_b

## define memory experience replay buffer
mem_buffer_size = 2**11     # 2**11

# number of experiences needed to perform batch update of VFA
n_batch_size = 2**9         # 2**9

# regularization parameter
eta = 1e-6                  # 1e-6

""" Algorithm parameters """

# discount rate
gamma = 0.99

# number of algorithm runs
Z = 5

# number of episodes
M = int(0.1e3)

# policy evaluation test frequency 
test_freq = 25

# number of replications per test
num_test_reps = 30

# seed offset for manual testing
offset = 0

# dimensionality of state space 
num_state_dims = len(env.observation_space.low)

# discrete action space - number of actions 
num_actions = env.action_space.n
num_action_dims = 1
num_sa_dims = num_state_dims*num_action_dims # num_sa_dims = num_state_dims+num_action_dims

# define reference points in state space for use with VFA
Slow = np.array(env.observation_space.low)
Shigh = np.array(env.observation_space.high)
# overwrite environment infinite boundaries with finite ones
# Slow = np.array([])
# Shigh = np.array([])
Srange = Shigh-Slow

"""
IMPLEMENT LSPI ALGORITHM
"""
# define state-action value function approximation linear model
    # Fourier cosine basis functions, Laquerre polynomials, or a tile coding VEA approach will likely attain improved performance compared to simple polynomials
def phi(s,a):
    # Simple 2nd order polynomial with interactions 
    # sa = np.hstack(((s-Slow) /Srange, a- 1))
    # Simple 4th order polynomial with interactions 
    sa = np.hstack(((s-Slow)/Srange,((s-Slow)/Srange)**2,a-1))
    sa2 = np.matrix(sa).T*np.matrix(sa)
    up_tri_sa2 = np.triu(sa2)
    sa2_flat = up_tri_sa2[np.triu_indices_from(up_tri_sa2)]
    return np.hstack((1, sa, sa2_flat))

# batch computation of phi-values 
def batchPhi(s_batch,a_batch):
    return np.array([phi(s, a) for s, a in zip(s_batch, a_batch)])

# compute VFA quantity at state-action pair given weight vector w
def Qbar(s,a,w):
    return np.dot(w,phi(s,a))

# batch computation of action that maximizes ETDR 
def batchArgmaxQbar(s_arrays, w):
    # Compute Qvals for each combination of s and a
    Qvals = np.array([[Qbar(s, a, w) for a in range(num_actions)] for s in s_arrays])
    # Find the maximum value for each row (i.e., each s array)
    max_actions = np.argmax(Qvals, axis=1)
    return max_actions

# computation of action that maximizes ETDR
def argmaxQbar(s,w):
    Qvals = [Qbar(s,a,w) for a in range(num_actions)]
    return np.argmax(Qvals)

# record each episode's cumulative reward to measure online performance
Gzm = []
GzmTest = []

# number features
num_features = len(phi(env.reset()[0],0))

# regularization matrix
Eta = eta*np.eye(num_features)

# Initialize the data structure to hold the top 2Z scores and VFA parameters 
num_best_scores = 2*Z
best_scores = [{'ETDR': -np.inf, 'ETDR_hw': np.inf, 'w': None, 'iht': None} for _ in range(num_best_scores)]

# record score it it is a top score (s.e., better 95CILB)
def update_best_scores(mean, hw, w, best_scores):
    # Find the first score that mean is greater than 
    for i in range(len(best_scores)):
        if mean-hw > best_scores[i]['ETDR']-best_scores[i]['ETDR_hw']:
            # Shift scores and parameters
            best_scores.insert(i, {'ETDR': np.copy(mean), 'ETDR_hw': np.copy(hw), 'w': np.copy(w)})
            # We only want the top scores, so remove the last one 
            best_scores.pop()
            return True
    return False

# Function for computing confidence interval
def confinterval(data,alpha=0.05):
    n = np.size(data)               # number of data points
    se = np.std(data)/np.sqrt(n)    # standard error
    ts = t.ppf((1-alpha/2), n-1)    # t-score
    mean = np.mean(data)
    halfwidth = ts*se
    return mean, halfwidth

# define test function
def evaluate_policy(w,num_reps, seed_mult=1):
    # initialize_test_data_structure
    test_data = np.zeros((num_reps))
    # run num_test_reps replication per test
    for rep in range(num_reps):
        # initialize episode conditions
        terminated = False
        truncated = False
        # Initialize episode reward
        Gtest = 0
        # Initialize the system by resetting the environment, obtain state var
        state = env.reset(seed=seed_mult*1000+rep)[0]
        while not (terminated or truncated):
            # take action according to current policy, using theta
            action = argmaxQbar(state,w)
            # apply action and observe system information
            state, reward, terminated, truncated, _ = env.step(action)
            # update episode cumulative reward
            Gtest += reward
        test_data[rep] = Gtest
    mean, hw = confinterval(test_data)
    return mean, hw

# start timer for executing algorithm
tic = time.perf_counter()

# execute each algorithm rep
for z in range(Z):
    # initialize memory replay buffer counter
    mem_buffer_counter = 0
    # initialize SARnSd tuple memory buffer components
    mem_buffer_states = np.zeros((mem_buffer_size, num_state_dims), dtype=np.float32)
    mem_buffer_actions = np.zeros(mem_buffer_size, dtype=np.int32)
    mem_buffer_rewards = np.zeros(mem_buffer_size, dtype=np.float32)
    mem_buffer_next_states = np.zeros((mem_buffer_size, num_state_dims), dtype=np.float32)
    mem_buffer_done_flags = np.zeros(mem_buffer_size, dtype=np.int32)

    # initialize theta vector of basis function weights
    w = np.zeros(num_features)

    print(f"\nLSPI(alpha_a={alpha_a:<3.2f}, alpha_b={alpha_b:<3.2f}, eps_a={eps_a:<3.2f}, eps_b={eps_b:<3.2f} rep {z}...")

    # loop through each episode 
    for m in range(M):
        # initialize episode complete flag (when system enters terminal state)
        terminated = False
        truncated = False
        # initialize episode reward
        G = 0
        # set random number generator seed
        np.random.seed(int(z+1e6+m+1e5*offset))
        # initialize the system by resetting the environment, obtain state var
        state = env.reset(seed=int(z+1e6+m+1e5*offset))[0]
        # LSPI main loop, implementing trajectory following state sampling
        while not(terminated or truncated):
            # select action based on epsilon-greedy exploration mechanism
            if np.random.rand() > epsilon(m):
                # act greedy by exploiting current knowledge
                # take best action at current state using Qbar 
                action = argmaxQbar(state,w)
            else:
                # act randomly with probability epsilon to explore
                action = np.random.randint(0,num_actions)

            # apply action and observe system information 
            next_state, reward, terminated, truncated, _ = env.step(action)

            # Update episode cumulative reward
            G += reward

            # store unite experience in memory replay buffer, increment counter 
            index = mem_buffer_counter % mem_buffer_size 
            mem_buffer_states[index, :] = state 
            mem_buffer_actions[index] = action 
            mem_buffer_rewards[index] = reward 
            mem_buffer_next_states[index, :] = next_state 
            mem_buffer_done_flags[index] = terminated 
            mem_buffer_counter += 1

            # update state
            state = np.copy(next_state)

        # update policy -- select n_batch_size experiences and w solving regression problem
        if mem_buffer_counter >= n_batch_size:
            # sample memory buffer, collecting a batch of SARnSd transitions
            # determine indexes of experiences used to update policy 
            max_memory = min(mem_buffer_size, mem_buffer_counter)
            batch_indexes = np.random.choice(np.arange(max_memory), n_batch_size, replace=False)

            # specify batches
            states_batch = mem_buffer_states[batch_indexes, :]
            actions_batch = mem_buffer_actions[batch_indexes] 
            rewards_batch = mem_buffer_rewards[batch_indexes] 
            next_states_batch = mem_buffer_next_states[batch_indexes, :]
            done_flags_batch = mem_buffer_done_flags[batch_indexes]

            # compute matrices and vectors for normal equation
            Phi_curr = np.matrix(batchPhi(states_batch, actions_batch))
            next_actions_batch = batchArgmaxQbar(next_states_batch, w)
            Phi_next = np.matrix(batchPhi(next_states_batch, next_actions_batch))
            r = np.matrix(rewards_batch).T
            # ensure terminal state-action pairs have zero value
            Phi_next[done_flags_batch==1,1:] = 0
            # determine w by solving normal equation with L2 regularization 
            what = np.ravel(np.linalg.solve(Phi_curr.T*(Phi_curr-gamma*Phi_next)+Eta, Phi_curr.T*r))

            # Polyak averaging
            w = (1-alpha(m))*w + alpha(m)*what

        # record performance 
        # print (f"\nEpisode: {m}, Cumulative reward: {Gm}")
        Gzm.append((z,G))

        # test current policy (as represented by current w and iht) every test_freq episodes
        if m % test_freq == 0:
            mean, hw = evaluate_policy(w, num_test_reps)
            GzmTest.append((z, m, mean, hw))

            # update best EETDR scores if necessary
            if update_best_scores(mean, hw, w, best_scores):
                print(f"Test... Episode: {m:>4}, EETDR CI: {mean:>6.1f} +/- {hw:4.1f}) *** New Top {num_best_scores} Reliable EETDR")
            else:
                print(f"Test... Episode: {m:>4}, EETDR CI: {mean:>6.1f} +/- {hw:4.1f}")

    # last test of current algorithm replication
    mean, hw = evaluate_policy(w, num_test_reps)
    GzmTest.append((z,M, mean, hw))

    # update best EETDR scores if necessary
    if update_best_scores(mean, hw, w, best_scores):
        print(f"Test... Episode: {M:>4}, EETDR CI: {mean:>6.1f} +/- {hw:4.1f}) *** New Top {num_best_scores} Reliable EETDR")
    else:
        print(f"Test... Episode: {M:>4}, EETDR CI: {mean:>6.1f} +/- {hw:>4.1f}\n *-------* Current Top 5 Reliable EETDRs: {best_scores[0]['ETDR']:>6.1f}, {best_scores[1]['ETDR']:>6.1f}, {best_scores[2]['ETDR']:>6.1f}, {best_scores[3]['ETDR']:>6.1f}, {best_scores[4]['ETDR']:>6.1f}")

toc = time.perf_counter()
print(f"\nExecuted {Z} algorithm reps in {toc - tic:0.4f} seconds.")

env.close()

print (f"\nValidation testing of policies with Top {num_best_scores} best EETDRs...")

# create string for ordinal number
def ordinal(n):
    suffix = ('th', 'st', 'nd', 'rd', 'th')[min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix

# initialize list of means and half-widths for testing top policies
mean_values = []
hw_values = []

# loop through top policies stored in best_scores to find superlative policy
for i, score in enumerate(best_scores):
    mean, hw = evaluate_policy(score['w'], 2*num_test_reps, 2)
    print(f"\nBest VFA ({ordinal(i+1)}) test... EETDR CI: {mean:>6.1f} +/- {hw:4.1f}")
    mean_values.append(mean)
    hw_values.append(hw)

# determine superlative policy and record its mean and half-width
    # superlative policy is one with highest 95% confidence Interval lower bound
    # estimated ETDR
indBestCILB = np.argmax(np.array(mean_values)-np.array(hw_values))
maxETDR = mean_values[indBestCILB]
maxETDRhw = hw_values[indBestCILB]

# VFA parameter-values representing superlative policy for algorithm design
    # run, across all replications
w = np.copy(best_scores[indBestCILB]['w'])

"""
plot performance results
"""
npGzmTest = np.array(GzmTest)
size = np.shape(npGzmTest)
TestEETDR = np.reshape(npGzmTest[:,2],(Z,int(size[0]/Z)))

maxTestEETDR = np.max(TestEETDR, axis=1)
meanMaxTestEETDR = np.mean(maxTestEETDR)
maxTestSE = np.std(maxTestEETDR) / np.sqrt(Z)
maxTestHW = t.ppf(1-0.05/2, Z-1) * maxTestSE

avgTestEETDR = np.mean(TestEETDR, axis=0)
avgTestSE = np.std(TestEETDR, axis=0)/np.sqrt(Z)
avgTestHW = t.ppf(1-0.05/2, Z-1) * avgTestSE

AULC = [metrics.auc(np.arange(0,M+1,test_freq), TestEETDR[z,:])/M for z in range(Z)]
meanAULC = np.round(np.mean(AULC),1)
hwAULC = t.ppf(1-0.05/2, Z-1) * np.std(AULC)/np.sqrt(Z)

plt.figure(0)
plt.plot(np.arange(0,M+1,test_freq), avgTestEETDR, marker = 'o', ms = 3, mec = 'k', linewidth = 1, label='Mean EETDR')
plt.plot(np.arange(0,M+1,test_freq), avgTestEETDR+avgTestHW, color = 'blue', linestyle = '--', linewidth = 0.5, label='95% Halfwidth')
plt.plot(np.arange(0,M+1,test_freq), avgTestEETDR-avgTestHW, color = 'blue', linestyle = '--', linewidth = 0.5)
plt.xlabel('Episode')
plt.ylabel('Mean Estimated Expected\nTotal Discounted Reward (EETDR)')
plt.title(f'SARSA(lam) Algorithm Test Performance, {Z} reps, {np.round((toc-tic)/(Z)/60,1)} min/rep\ngamma={gamma}, alpha_a={alpha_a}, alpha_b={alpha_b}, eps_a={eps_a}, eps_b={eps_b},\nMean Max EETDR: {meanMaxTestEETDR:>6.1f} +/- {maxTestHW:4.1f}, Mean Time-Avg EETDR={meanAULC} +/- {hwAULC:4.1f}\nSuperlative Policy EETDR: {maxETDR:>6.1f} +/- {maxETDRhw:4.1f}', fontsize=9)

plt.legend(loc="lower right", fontsize=7)
plt.xlim([-0.05*M, 1.05*M])
plt.ylim([-205, -95])
plt.grid(which='both')
plt.show()
