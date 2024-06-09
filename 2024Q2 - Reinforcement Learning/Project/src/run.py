from LambdaSARSA import LambdaSARSA
from LSPI import LSPI
from SemiGradSARSA import SemiGradSARSA
import gymnasium as gym

env = gym.make('LunarLander-v2')
lam_sarsa = LambdaSARSA(env)
lam_sarsa.train(num_replications=5, num_episodes=100)
#lam_sarsa.get_results()
lam_sarsa.show_results()
#lam_sarsa.display_best_policy()
#print(lam_sarsa.find_superlative())

#lspi = LSPI(env)
#lspi.train(num_replications=5, num_episodes=100)
#lspi.get_results()
#lspi.show_results()
#lspi.display_best_policy()
#   KeyError: 'Q'
#print(lspi.find_superlative())

#sg_sarsa = SemiGradSARSA(env)
#sg_sarsa.train(num_replications=5, num_episodes=100)
#sg_sarsa.get_results()
#sg_sarsa.show_results()
#sg_sarsa.display_best_policy()
#print(sg_sarsa.find_superlative())