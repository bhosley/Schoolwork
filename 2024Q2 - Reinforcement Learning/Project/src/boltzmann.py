from SemiGradSARSA import SemiGradSARSA
import numpy as np

class SemiGradSARSA_boltzmann(SemiGradSARSA):
    name = "Semi-gradient n-step SARSA"

    def __init__(self, env, n=1, **kwargs) -> None:
        super().__init__(env, **kwargs)
        self.algorithm_name = f"Semi-gradient {n}-step SARSA with Boltzmann Exploration"
        self.nm1 = n-1
        self.tau            = kwargs.get('tau',1.0)
        self._tau_          = self.tau
        self.cooling_rate   = kwargs.get('cooling_rate',0.000001)


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


from LambdaSARSA import LambdaSARSA
import numpy as np

class LambdaSARSA_boltzmann(LambdaSARSA):
    name = "SARSA (lambda) with linear tile coding VFA scheme and Boltzmann Exploration"

    def __init__(self, env, n=1, **kwargs) -> None:
        super().__init__(env, **kwargs)
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