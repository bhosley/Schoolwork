







import gymnasium as gym
import numpy as np
import time
from scipy.stats import t
import matplotlib.pyplot as plt
from sklearn import metrics
import collections

env = gym.make('MountainCar-v0')

print(f"\nFarama OpenAI Gym version: {gym.__version__}")

# Observation and Action Space
print("The observation space: {}".format(env.observation_space))
print("The action space: {}".format(env.action_space))

## Important Algorithm parameters to tune

# Learning Rate
alpha_a = 1.0
alpha_b = 0.5
def alpha(n):
    return alpha_a/(1+n)**alpha_b

# Eps-Greedy stepsize rule
eps_a = 1.0
eps_b = 0.5
def epsilon(n):
    return eps_a/(1+n)**eps_b

# Q initialization
qinit = 0.5

# Number of steps for computing n-step returns; nm1 = 0 indicat4es 1-step return
nm1 = 1

# Number of intervals per dimension
# e.g., using 11 intervales indicates 12 discrete states per dim
Sintervals = 11

## Algorithm Parameters

# Discount rate 
gamma = 0.999

# Range of q-values for environment
qrange = [-200,-100]

# Number of algorithm replications
Z = 4 #Z = 10

# Number of Episodes
M = int(0.5e3) #M = int(0.5e3)

# Policy Evaluation test frequency
test_freq = 25

# Number of replications per test
num_test_reps = 30

# Seed offset for manual testing
offset = 0 

# Continuous state space
num_state_dims = len(env.observation_space.low) 

# Discrete Action Space
num_actions = env.action_space.n                

# Define reference points for dicretizing state space
Slow = np.array(env.observation_space.low)
Shigh = np.array(env.observation_space.high)
Srange = Shigh - Slow
Sunit = Srange/Sintervals
Ssize = (Sintervals + 1)*np.ones(num_state_dims).astype(int)

# Size of State Action Space
SAsize = np.append(Ssize,num_actions)

# Convert continuous state to discrete representation
def phi(Scont):  
    return np.round((Scont-Slow)/Sunit).astype(int) # Smax = Srange/Sunit # temp =  #return np.minimum(temp, Smax).astype(int)

# record each episode's cumulative reward to measure online performance
Gzm = []
GzmTest = []

# Initialize the data structure to hold the Top 2 scores and VEA parameters 
num_best_scores = 2*Z
best_scores = [{'ETDR': -np.inf, 'ETDR_hw': np.inf, 'Q': None} for _ in range(num_best_scores)]

def update_best_scores(mean, hw, Q, best_scores):
    # Find the first score that is less than
    for i in range(len(best_scores)):
        if mean - hw > best_scores[i]['ETDR']-best_scores[i]['ETDR_hw']:
            # Insert best score and attendent parameters
            best_scores.insert(i, {'ETDR': np.copy(mean), 'ETDR_hw': np.copy(hw), 'Q': np.copy(Q)})
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
def evaluate_policy_milestone_test(Q, num_reps=num_test_reps, seed_mult=1):
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
            action = np.argmax(Q[tuple(phi(state))])
            # apply action and observe system information
            state, reward, terminated, truncated, _ = env.step(action)
            # update episode cumulative reward
            Gtest += reward
        test_data[rep] = Gtest
    mean, hw = confinterval(test_data)
    return mean, hw

# start timer for loading problem into memory
tic = time.perf_counter()

# perform each algorithm replication
for z in range(Z):
    # initialize Q-table
    Q = qinit*np.ones(SAsize) * (qrange[1] - qrange[0]) + qrange[0]
    # initialize state-action counter
    C = np.zeros(SAsize)

    print(f"\n{nm1+1} - step SARSA(alpha_a = {alpha_a:<3.2f}, alpha_b={alpha_b:<3.2f}, eps_a={eps_a:<3.2f}, eps_b={eps_b:<3.2f}, |S|/d {Sintervals}, qinit={qinit}, rep {z}...")
    
    
    for m in range(M):
        # initialize episode complete flag (when system enters terminal state)
        terminated = False
        truncated = False
        # Initialize episode reward
        Gm = 0
        # Set random number generator seed
        np.random.seed(int(z*1e6+m+1e5*offset))
        # Initialize the system by resetting the environment, obtain state var
        state_continuous = env.reset(seed=int(z*1e6+m))[0]
        # Transform continuous state to discrete representation via aggregation
        state = phi(state_continuous)
        # Initialize state array, records of states
        state_queue = collections.deque([state])
        # Compute number of times state has been visited
        cs = np.sum(C[tuple(state)])
        # Select action based on epsilon-greedy exploration mechanism
        if np.random.rand() > epsilon(cs):
            # Act greedy by exploiting current knowledge
            # using Q
            action = np.argmax(Q[tuple(state)])  
        else:
            # Act randomly with probability epsilon to explore
            action = np.random.randint(0, num_actions)
        # Initialize action array, record of actions
        action_queue = collections.deque([action])
        # Initialize reward array, record of rewards
        reward_queue = collections.deque([])

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
            qhat = np.dot(reward_queue, gamma**np.arange(len(reward_queue))) + \
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
                qhat = np.dot(reward_queue, gamma**np.arange(len(reward_queue))) + \
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
    mean, hw = evaluate_policy_milestone_test(score['Q'], 2*num_test_reps, 2)
    print(f"#{i+1} candidate superlative policy ({ordinal(i+1)}) test... EETDR CI: {mean:>6.1f} +/- {hw:4.1f}")
    mean_values.append(mean)
    hw_values.append(hw)

# determine superlative policy and record its mean and half-width
maxETDR = np.max(mean_values)
argmaxETDR = np.argmax(mean_values)
maxETDRhw = hw_values[argmaxETDR]

# Q-values representing superlative policy for algorithm design run
Q = np.copy(best_scores[argmaxETDR]['Q'])

"""
plot performance results
"""
npGzmTest = np.array(GzmTest)
size = np.shape(npGzmTest)
TestEETDR = np.reshape(npGzmTest[:,2], (Z, int(size[0]/Z)))

maxTestEETDR = np.max(TestEETDR, axis=1)
meanMaxTestEETDR = np.mean(maxTestEETDR)
maxTestSE = np.std(maxTestEETDR) / np.sqrt(Z)
maxTestHW = t.ppf(1-0.05/2, Z-1) * maxTestSE

avgTestEETDR = np.mean(TestEETDR, axis=0)
avgTestSE = np.std(TestEETDR, axis=0)/np.sqrt(Z)
avgTestHW = t.ppf(1-0.05/2, Z-1) * avgTestSE

print(np.arange(0,M+1,test_freq).shape)
print(np.linspace(0,M+1,Z).shape)
#print(np.arange(0,M+1,(M+1)/TestEETDR.shape[0]).shape)
print(TestEETDR.shape) # Z by 
AULC = [metrics.auc(np.arange(0,M+1,test_freq), TestEETDR[z,:])/M for z in range(Z)]
meanAULC = np.round(np.mean(AULC),1)
hwAULC = t.ppf(1-0.05/2, Z-1) * np.std(AULC)/np.sqrt(Z)

plt.figure(0)
plt.plot(np.arange(0,M+1,test_freq), avgTestEETDR, marker = 'o', ms = 3, mec = 'k', linewidth = 1, label='Mean EETDR')
plt.plot(np.arange(0,M+1,test_freq), avgTestEETDR+avgTestHW, color = 'blue', linestyle = '--', linewidth = 0.5, label='95% Halfwidth')
plt.plot(np.arange(0,M+1,test_freq), avgTestEETDR-avgTestHW, color = 'blue', linestyle = '--', linewidth = 0.5)
plt.xlabel('Episode')
plt.ylabel('Mean Estimated Expected\nTotal Discounted Reward (EETDR)')
plt.title(f'{nm1+1}-step SARSA Algorithm Test Performance, {Z} reps, {np.round((toc-tic)/(Z)/60,1)} min/rep\ngamma={gamma}, alpha_a={alpha_a}, alpha_b={alpha_b}, eps_a={eps_a}, eps_b={eps_b}, |S|/d={Sintervals}, qinit={qinit} \nMean Max EETDR: {meanMaxTestEETDR:>6.1f} +/- {maxTestHW:4.1f}, Mean Time-Avg EETDR={meanAULC} +/- {hwAULC:4.1f}\nSuperlative Policy EETDR: {maxETDR:>6.1f} +/- {maxETDRhw:4.1f}', fontsize=9)

plt.legend(loc="lower right", fontsize=7)
plt.xlim([-0.05*M, 1.05*M])
plt.ylim([-205, -95])
plt.grid(which='both')
plt.show()

"""
display superlative policy (sans exploration)
"""
def displayBestPolicy():
    env = gym.make('MountainCar-v0', render_mode='human')
    # number of runs to show
    num_reps_show = 10
    # initialize test data structure
    test_data = np.zeros((num_reps_show))
    for rep in range(num_reps_show):
        terminated = False  # initialize episode complete flags (e.g., when system enters terminal state)
        truncated = False
        Gtest = 0  # initialize episode reward
        state_continuous = env.reset(seed=1000+rep+offset)[0]
        state = phi(state_continuous)
        while not (terminated or truncated):
            action = np.argmax(Q[tuple(state)])  # select action with highest q-value
            state_continuous, reward, terminated, truncated, _ = env.step(action)
            state = phi(state_continuous)
            Gtest += reward
        test_data[rep] = Gtest
        print(f"Episode {rep} ETDR: {np.round(Gtest, 4)}")
        time.sleep(1)
    env.close()
    mean, hw = confinterval(test_data)
    print(f"\n Rendered episodes...ETDR CI: {np.round(mean, 1)} +/- {np.round(hw,1)}")
    return

# Uncomment and execute to watch rendered runs
#displayBestPolicy()

