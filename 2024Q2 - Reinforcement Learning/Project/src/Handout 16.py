"""
DSOR 646 - Reinforcement Learning
Dr. Matthew Robbins
Lesson 16 Handout -- SARSA (lambda) with linear tile coding VFA scheme
Farama OpenAI Gymnasium MountainCar-v0 Environment
"""

import gymnasium as gym
import numpy as np
import time
from scipy.stats import t
import matplotlib.pyplot as plt
from tiles3 import tiles, IHT
from sklearn import metrics
import copy

env = gym.make('MountainCar-v0')

print(f"\nFarama OpenAl Gym version: {gym.__version__}")

# Observation and action space
print("The observation space: {}".format(env.observation_space))
print ("The action space: {}".format(env.action_space))

""" Algorithm parameters for tuning """

# VEA coefficient smoothing rule
alpha_a = 1.0               # (*)   # 1.0
alpha_b = 0.5               # (*)   # 0.5
def alpha(n):
    return alpha_a/(1+n)**alpha_b

# eps-greedy stepsize rule
eps_a = 1.0                 # (*)   # 1.0
eps_b = 0.5                 # (*)   # 0.5
def epsilon (n) :
    return eps_a/(1+n)**eps_b

# trace decay parameter
lam_a = 0.8                 # (*)   # 0.8
lam_b = 0.2                 # (*)   # 0.2
def lam(n) :
    return lam_a/(1+n)**lam_b

# VFA tile coding scheme for state-action space
max_size_VFA = 2**10
num_tilings_VFA = 4         # 4
num_tiles_VFA = 4           # 4

# initial q value
qinit = 1.0

# TD error clip (for stability)
Δ_clip = 10

""" Algorithm parameters """

# discount rate
gamma = 0.9999

# range of q-values for environment (for setting qinit)
qrange = [-200, -100]

# number of algorithm runs
Z = 10

# number of episodes
M = int (0.5e3)

# policy evaluation test frequency
test_freq = 25

# number of replications per test
num_test_reps = 30

# random number generator seed manual offset
offset = 0

# dimensionality of state space 
num_state_dims = len(env.observation_space.low)

# discrete action space - number of actions 
num_actions = env.action_space.n

# define reference points in state space for use with VFA
Slow = np.array(env.observation_space.low)
Shigh = np.array(env.observation_space.high)
# overwrite environment infinite boundaries with finite ones
# Slow = np.array([])
# Shigh = np.array([])
Srange = Shigh-Slow
scaleFactor = num_tiles_VFA/Srange  # for use in tiles function
# variables to collect state variable boundary information
# Slow_obs = np.int*np.ones(num_state_dims)
# Shigh_obs = -np.inf*np.ones(num_state_dims)

def phi (s,a,iht_VEA): # returns index numbers of active tiles 
    # utilizes tile coding scheme across entire state space 
    return tiles(iht_VEA, num_tilings_VFA,list(s*scaleFactor),[int(a)])

def Qbar(s,a,w,iht_VFA):
    qhat = 0
    tiles = phi(s,a,iht_VFA)
    for tile in tiles:
        qhat += w[tile]
    return qhat[0]

def gradQbar(s,a,iht_VEA):
    return phi(s,a, iht_VEA)

# computes action that maximizes performance, as represented by approximate
#   Q function, comprised of weight vector w and integer hash table 
def argmaxQbar(s,w,iht):
    Qvals = [Qbar(s,a,w,iht) for a in range(num_actions)]
    return np.argmax(Qvals)

# record each episode's cumulative reward to measure online performance
Gzm = []
GzmTest = []

# Initialize the data structure to hold the top 2Z scores and VFA parameters 
num_best_scores = 2*Z
best_scores = [{'ETDR': -np.inf, 'ETDR_hw': np.inf, 'w': None, 'iht': None} for _ in range(num_best_scores)]

def update_best_scores(mean, hw, w, iht, best_scores):
    # Find the first score that mean is greater than 
    for i in range(len(best_scores)):
        if mean-hw > best_scores[i]['ETDR'] -best_scores[i]['ETDR_hw']:
            # Shift scores and parameters
            best_scores.insert(i, {'ETDR': np.copy(mean), 'ETDR_hw': np.copy(hw), 'w': np.copy(w),'iht': copy.deepcopy(iht)})
            # We only want the top scores, so remove the last one 
            best_scores.pop()
            return True
    return False

# Function for computing confidence interval
def confinterval(data, alpha=0.05):
    n = np.size(data)
    se = np.std(data)/np.sqrt(n)  # standard error
    ts = t.ppf((1-alpha/2), n-1)  # t-score
    mean = np.mean(data)
    halfwidth = ts*se
    return mean, halfwidth

# define test function
def evaluate_policy(w, iht, num_reps, seed_mult=1):
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
            # select action with highest q-value
            action = argmaxQbar(state,w,iht)
            # apply action and observe system information
            state, reward, terminated, truncated, _ = env.step(action)
            # update episode cumulative reward
            Gtest += reward
        test_data[rep] = Gtest
    mean, hw = confinterval(test_data)
    return mean, hw

# start timer for loading problem into memory
tic = time.perf_counter()

# loop through each algorithm run
for z in range(Z):
    # initialize theta vector of basis function weights
    w= qinit*np.ones((max_size_VFA,1))/num_tilings_VFA
    # initialize eligibility trace vector
    zeta = np.zeros ( (max_size_VFA,1))
    # initialize state action counter
    Nsa = np. zeros ((max_size_VFA,1))
    # initialize integer hash table
    iht_VFA = IHT(max_size_VFA)

    print(f"\nSARSA(alpha_a={alpha_a: <3.2f},alpha_b={alpha_b: <3.2f},eps_a={eps_a:<3.2f},eps_b={eps_b:<3.2f}, lam_a rep{z}...")

    # loop through each episode 
    for m in range(M):
        # initialize episode complete flag (when system enters terminal state)
        terminated = False
        truncated = False
        # initialize episode reward
        Gm = 0
        # set random number generator seed
        np.random.seed(int(z+1e6+m+1e5*offset))
        # initialize the system by resetting the environment, obtain state var
        state = env.reset(seed=int(z*1e6+m))[0]
        # select action based on epsilon-greedy exploration mechanism
        if np.random.rand() > epsilon(m):
            # act greedy by exploiting current knowledge
            # take best action at current state using bar
            action = argmaxQbar(state, w, iht_VFA)
        else:
            #act randomly with probability epsilon to explore
            action = np.random.randint(0,num_actions)


        # SARSA main loop (first nm1 transitions until end of episode)
        while not (terminated or truncated):
            # Apply action and observe system information
            next_state, reward, terminated, truncated, _ = env.step(action)
            
            # Update episode cumulative reward
            Gm += reward

            if np.random.rand() > epsilon(m):
                # act greedy by exploiting current knowledge
                # take best action at current state using bar
                nex_action = argmaxQbar(state, w, iht_VFA)
            else:
                #act randomly with probability epsilon to explore
                next_action = np.random.randint(0,num_actions)

            # Compute qhat
            qhat = reward + (1-terminated)*gamma*Qbar(next_state,next_action,w,iht_VFA)

            # compute TD error
            Δ = np.clip(-Δ_clip, qhat - Qbar(state,action,w,iht_VFA),Δ_clip)

            # Update eligibility trace
            zeta = gamma*lam(m)*zeta
            active_tiles = gradQbar(state,action,iht_VFA)
            zeta[active_tiles] += 1

            # update state-action counter
            Nsa[active_tiles] += 1

            # update w vector
            w += alpha(Nsa)*Δ*zeta

            # update state and action
            state = np.copy(next_state)
            action = np.copy(next_action)

            # update state variable boundary information
            # Slow_obs (state < Slow_obs) = state|state < Slow_obs)
            # Shigh_obs|state › Shigh_obs) = state(state › Shigh_obs)

        # record performance
        # print (f"\nEpisode: {m}, Cumulative reward: {Gm}")
        Gzm.append((z,Gm))

        # test current policy (as represented by current w and iht) every test_freq episodes
        if m % test_freq == 0:
            mean, hw = evaluate_policy(w, iht_VFA, num_test_reps)
            GzmTest.append((z,m, mean, hw))

            # update best EETDR scores if necessary
            if update_best_scores(mean, hw, w, iht_VFA, best_scores):
                print(f"Test... Episode: {m:>4}, EETDR CI: {mean:>6.1f} +/- {hw:4.1f}) *** New Top {num_best_scores} Reliable EETDR")
            else:
                print(f"Test... Episode: {m:>4}, EETDR CI: {mean:>6.1f} +/- {hw:4.1f}")

    # last test of current algorithm replication
    mean, hw = evaluate_policy(w, iht_VFA, num_test_reps)
    GzmTest.append((z,M, mean, hw))

    # update best EETDR scores if necessary
    if update_best_scores(mean, hw, w, iht_VFA, best_scores):
        print(f"Test... Episode: {M:>4}, EETDR CI: {mean:>6.1f} +/- {hw:4.1f}) *** New Top {num_best_scores} Reliable EETDR")
    else:
        print(f"Test... Episode: {M:>4}, EETDR CI: {mean:>6.1f} +/- {hw:>4.1f}\n *-------* Current Top 5 Reliable EETDRs: {best_scores[0]['ETDR']:>6.1f}, {best_scores[1]['ETDR']:>6.1f}, {best_scores[2]['ETDR']:>6.1f}, {best_scores[3]['ETDR']:>6.1f}, {best_scores[4]['ETDR']:>6.1f}")


toc = time.perf_counter()
print(f"\nExecuted {Z} algorithm reps in {toc - tic:0.4f} seconds.")

print(f"\nIdentifying superlative policy via testing of policies from Top {num_best_scores} Reliable EETDRs...")

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
    mean, hw = evaluate_policy(score['w'], score['iht'], 2*num_test_reps, 2)
    print(f"\nBest VFA ({ordinal(i+1)}) test... EETDR CI: {mean:>6.1f} +/- {hw:4.1f}")
    mean_values.append(mean)
    hw_values.append(hw)

# determine superlative policy and record its mean and half-width
argmax95CILB = np.argmax(np.array(mean_values)-np.array(hw_values))
maxETDR = mean_values[argmax95CILB]
maxETDRhw = hw_values[argmax95CILB]

# set Qbar VFA equal to best parameters
w = np.copy(best_scores[argmax95CILB]['w'])
iht_VFA = copy.deepcopy(best_scores[argmax95CILB]['iht'])

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
plt.title(f'SARSA(lam) Algorithm Test Performance, {Z} reps, {np.round((toc-tic)/(Z)/60,1)} min/rep\ngamma={gamma}, alpha_a={alpha_a}, alpha_b={alpha_b}, eps_a={eps_a}, eps_b={eps_b}, lam_a={lam_a}, lam_b={lam_b}, q0={qinit} \nMean Max EETDR: {meanMaxTestEETDR:>6.1f} +/- {maxTestHW:4.1f}, Mean Time-Avg EETDR={meanAULC} +/- {hwAULC:4.1f}\nSuperlative Policy EETDR: {maxETDR:>6.1f} +/- {maxETDRhw:4.1f}', fontsize=9)

plt.legend(loc="lower right", fontsize=7)
plt.xlim([-0.05*M, 1.05*M])
plt.ylim([-205, -95])
plt.grid(which='both')
plt.show()