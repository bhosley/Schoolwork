from support_functions import MDP_Tiled

import numpy as np
from time import perf_counter
from tiles3 import IHT

class LambdaSARSA(MDP_Tiled):
    name = "SARSA (lambda) with linear tile coding VFA scheme"

    def __init__(self, env, **kwargs) -> None:
        super().__init__(env, **kwargs)
        self.algorithm_name = self.name

        """ Tunable Hyperparameters """
        self.lam_a      = kwargs.get('eps_a',0.8)   # Trace decay parameter
        self.lam_b      = kwargs.get('eps_b',0.2)   # Trace decay parameter
        self.Δ_clip     = kwargs.get('clip',10)     # TD error clip (for stability)


    def lam(self,n) :
        return self.lam_a/(1+n)**self.lam_b

    def train(self, num_replications, num_episodes, verbose=False):
        time_start = perf_counter()
        for z in range(num_replications):
            # theta vector of basis function weights
            w = self.qinit*np.ones((self.max_size,1))/self.num_tiles
            zeta = np.zeros((self.max_size,1))      # eligibility trace vector
            Nsa  = np.zeros((self.max_size,1))      # state action counter
            iht_VFA = IHT(self.max_size)            # integer hash table

            print(f"\nSARSA(alpha_a={self.alpha_a: <3.2f},alpha_b={self.alpha_b:<3.2f}," 
                 +f"eps_a={self.eps_a:<3.2f},eps_b={self.eps_b:<3.2f}, lam_a rep{z}...")

            for m in range(num_episodes): # M
                terminated,truncated = False,False                  # Episode complete flags
                Gm = 0                                              # Episode reward
                np.random.seed(int(m + 1e6*z + 1e5*self.offset))    # Set rng seed
                state = self.env.reset(seed=int(z + 1e6 + m + 1e5*self.offset))[0]

                # select action based on epsilon-greedy exploration mechanism
                if np.random.rand() > self.epsilon(m):          # With probability epsilon:
                    action = self.argmaxQbar(state,w,iht_VFA)   # Act greedy, using Qbar
                else:
                    action = self.env.action_space.sample()     # Act randomly to explore

                # SARSA main loop (first nm1 transitions until end of episode)
                while not(terminated or truncated):
                    # Apply action and observe system information
                    next_state, reward, terminated, truncated, _ = self.env.step(action)
                    Gm += reward    # Update episode cumulative reward

                    # select action based on epsilon-greedy exploration mechanism
                    if np.random.rand() > self.epsilon(m):              # With probability epsilon:
                        next_action = self.argmaxQbar(state,w,iht_VFA)  # Act greedy, using Qbar
                    else:
                        next_action = self.env.action_space.sample()    # Act randomly to explore

                    # Compute qhat and TD error
                    qhat = reward + (1-terminated)*self.gamma*self.Qbar(next_state,next_action,w,iht_VFA)
                    Δ = np.clip(-self.Δ_clip, qhat - self.Qbar(state,action,w,iht_VFA),self.Δ_clip)

                    # Update:
                    zeta = self.gamma*self.lam(m)*zeta
                    active_tiles = self.gradQbar(state,action,iht_VFA)
                    zeta[active_tiles] += 1         # Eligibility trace
                    Nsa[active_tiles] += 1          # State-action counter
                    w += self.alpha(Nsa)*Δ*zeta     # w vector
                    state = np.copy(next_state)     # State
                    action = next_action            # Action - np.copy creates an array -> Error

                if verbose: print(f"In Episode: {m}, Cumulative reward: {Gm}")
                self.Gzm.append((z,Gm))

                # test current policy (as represented by current Q) every test_freq episodes
                if m % self.test_freq == 0:
                    mean, hw = self.evaluate_policy(w, iht_VFA, self.num_test_reps)
                    self.GzmTest.append((z, m, mean, hw))

                    # update best scores if necessary
                    if verbose:
                        self.update_and_print(m, mean, hw, w, iht_VFA)
                    else:
                        self.update_best_scores(mean, hw, w, iht_VFA)

            # last test of current algorithm replication
            mean, hw = self.evaluate_policy(w, iht_VFA, self.num_test_reps)
            self.GzmTest.append((z, num_episodes, mean, hw))

            # update best EETDR scores if necessary
            if verbose:
                self.update_and_print(num_episodes, mean, hw, w, iht_VFA)
            else:
                self.update_best_scores(mean, hw, w, iht_VFA)

        time_elapsed = perf_counter() - time_start
        print(f"Executed {num_replications} algorithm reps in {time_elapsed:0.4f} seconds.")

        self.total_training_reps += num_replications
        self.total_episodes += num_episodes
        # Update execution time record
        total_time = (self.total_training_reps * self.avg_execution_time) + time_elapsed
        self.avg_execution_time = total_time / self.total_training_reps