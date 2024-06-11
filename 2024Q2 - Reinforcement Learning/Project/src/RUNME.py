"""
Submission for DSOR 646
Brandon Hosley

Executing this script should provide the same style of results as the handouts in class.
Seed can be set here for convenience
"""
SEED = 42



from LambdaSARSA import LambdaSARSA
import numpy as np

class LambdaSARSA_boltzmann(LambdaSARSA):
    name = "SARSA (lambda) with linear tile coding VFA scheme and Boltzmann Exploration"

    def __init__(self, env, n=1, **kwargs) -> None:
        super().__init__(env, offset=SEED, **kwargs)
        self.algorithm_name = self.name
        self.tau            = kwargs.get('tau',2.0)
        self._tau_          = self.tau
        self.cooling_rate   = kwargs.get('cooling_rate',0.001)


    #@override(SemiGradSARSA) # Needs Python >3.12
    def get_action(self, state, policy, epsilon=0) -> int:
        w, iht = policy
        Qvals = np.array([self.Qbar(state,a,w,iht) for a in range(self.num_actions)])
        exp_q = np.clip(np.exp(Qvals / self.tau), 1e-10, 1e10)
        self.tau = self.tau * (1-self.cooling_rate) # Apply Cooling
        probabilities = exp_q / np.sum(exp_q)
        action = np.random.choice(range(self.num_actions), p=probabilities)
        return action

    #@override(MDPBase) # Needs Python >3.12
    def end_episode_callbacks(self) -> None:
        self.tau = self._tau_


import gymnasium as gym
env = gym.make('LunarLander-v2')
lsb = LambdaSARSA_boltzmann(env,
        alpha_a = 0.5,
        alpha_b = 0.5,
        eps_a   = 0.65,
        eps_b   = 0.35,
        lam_a   = 0.75,
        lam_b   = 0.25,
        clip    = 11,
        tau     = 10,
        cooling_rate = 1e-8,
                            )
lsb.train(num_replications=15, num_episodes=300)
lsb.get_results()
lsb.show_results()