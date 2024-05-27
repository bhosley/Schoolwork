import numpy as np
from time import perf_counter
from collections import deque

#%rm -r __pycache__/
from HW4_functions import MDPBase, LHS_Experiment

class Momentum(MDPBase):
    name = "Benchmark Momentum Policy"

    def __init__(self, env, **kwargs) -> None:
        super().__init__(env, **kwargs)
        self.algorithm_name = self.name

    def train(self, num_replications, num_episodes, verbose=False):
        time_start = perf_counter()
        for z in range(num_replications):
            print(f"Benchmark Momentum Policy rep {z}...")

            for m in range(num_episodes): # M
                np.random.seed(int(m + 1e6*z + 1e5*self.offset))    # Set rng seed
                terminated,truncated = False,False                  # Episode complete flags
                Gm = 0                                              # Episode reward

                # Benchmark Main Loop
                state_continuous = self.env.reset(seed=int(z*1e6 + m))[0]
                while not (terminated or truncated):
                    position, velocity = state_continuous
                    action = 0 if velocity < 0 else 2
                    state_continuous, reward, terminated, truncated, _ = self.env.step(action)
                    Gm += reward

                if verbose: print(f"In Episode: {m}, Cumulative reward: {Gm}")
                self.Gzm.append((z, Gm))

                if m % self.test_freq == 0:
                    mean, hw = self.evaluate_policy_test(None, self.num_test_reps)
                    self.GzmTest.append((z, m, mean, hw))
                    if verbose:
                        self.update_and_print(m, mean, hw, None)
                    else:
                        self.update_best_scores(mean, hw, None)

            mean, hw = self.evaluate_policy_test(None, self.num_test_reps)
            self.GzmTest.append((z, num_episodes, mean, hw))
            if verbose:
                self.update_and_print(num_episodes, mean, hw, None)
            else:
                self.update_best_scores(mean, hw, None)

        time_elapsed = perf_counter() - time_start
        print(f"Executed {num_replications} algorithm reps in {time_elapsed:0.4f} seconds.")

        self.total_training_reps += num_replications
        self.total_episodes += num_episodes
        total_time = (self.total_training_reps * self.avg_execution_time) + time_elapsed
        self.avg_execution_time = total_time / self.total_training_reps


    def evaluate_policy_test(self, Q, num_test_reps):
        cumulative_rewards = []
        for _ in range(num_test_reps):
            terminated, truncated = False, False
            state_continuous = self.env.reset()[0]
            total_reward = 0
            while not (terminated or truncated):
                position, velocity = state_continuous
                action = 0 if velocity < 0 else 2
                state_continuous, reward, terminated, truncated, _ = self.env.step(action)
                total_reward += reward
            cumulative_rewards.append(total_reward)

        mean_reward = np.mean(cumulative_rewards)
        hw = 1.96 * np.std(cumulative_rewards) / np.sqrt(num_test_reps)  # 95% CI half-width
        return mean_reward, hw


    def find_superlative(self):
        return None, -119, 1.0


import gymnasium as gym

env = gym.make('MountainCar-v0')
benchmark = Momentum(env)
benchmark.train(num_replications=30, num_episodes=100)
benchmark.show_results()