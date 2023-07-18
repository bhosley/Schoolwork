# Coded by Dr. Brian J. Lunday, AFIT/ENS on 19 April 2022
# In support of OPER 618 Game Theory & Math Programming, Summer 2022

import pyomo.environ as pyo

m = pyo.ConcreteModel()

# Input sets
m.J = {1,2,3}
m.K = {1,2}

# Input parameter data
u1=[[0,0,0],
   [0, 0, 6], 
   [0, 2, 5],
   [0, 3, 3]]
u2=[[0,0,0],
   [0, 1, 0], 
   [0, 0, 2],
   [0, 4, 3]]

# Define subsets of supports to test
m.sigma1={1,2,3} # Supports for Player 1 (cannot be empty)
m.notsigma1={} # Actions not in the suupport for Player 1
m.sigma2={1,2}  # Supports for Player 2 (cannot be empty)
m.notsigma2={} # Actions not in the support for Player 2

# Decision Variables
m.v1 = pyo.Var(domain=pyo.NonNegativeReals) # Player 1's utility
m.v2 = pyo.Var(domain=pyo.NonNegativeReals) # Player 2's utility
m.p1 = pyo.Var(m.J,domain=pyo.NonNegativeReals) # p1[j] is the probabilty that Player 1 plays action j
m.p2 = pyo.Var(m.K,domain=pyo.NonNegativeReals) # p2[k] is the probabilty that Player 2 plays action k
m.z = pyo.Var(domain=pyo.NonNegativeReals) # A dummy variable to serve as the objective function
 
# Model  (Formulation from page 99 of the text)
m.objfnvalue = pyo.Objective(expr = m.z, sense = pyo.minimize)
m.UtilityForPlayer1=pyo.ConstraintList()
for j in m.sigma1:
    m.UtilityForPlayer1.add(sum(m.p2[k]*u1[j][k] for k in m.sigma2) == m.v1)
m.UtilityForPlayer2=pyo.ConstraintList()
for k in m.sigma2:
    m.UtilityForPlayer2.add(sum(m.p1[j]*u2[j][k] for j in m.sigma1) == m.v2)
m.DominatingUtilityForPlayer1=pyo.ConstraintList()
for j in m.notsigma1:
    m.DominatingUtilityForPlayer1.add(sum(m.p2[k]*u1[j][k] for k in m.sigma2) <= m.v1)
m.DominatingUtilityForPlayer2=pyo.ConstraintList()
for k in m.notsigma2:
    m.DominatingUtilityForPlayer2.add(sum(m.p1[j]*u2[j][k] for j in m.sigma1) <= m.v2)
m.NullSupportProbabilitiesForPlayer1=pyo.ConstraintList()
for j in m.notsigma1:
    m.NullSupportProbabilitiesForPlayer1.add(m.p1[j] == 0)
m.NullSupportProbabilitiesForPlayer2=pyo.ConstraintList()
for k in m.notsigma2:
    m.NullSupportProbabilitiesForPlayer2.add(m.p2[k] == 0)    
m.ProbabilityDistributionForP1 = pyo.Constraint(expr = sum(m.p1[j] for j in m.sigma1) == 1)   
m.ProbabilityDistributionForP2 = pyo.Constraint(expr = sum(m.p2[k] for k in m.sigma2) == 1)                         

# Solve model
results=pyo.SolverFactory('ipopt').solve(m,tee=False)

# Output results
print('v1 = %.3f' % pyo.value(m.v1)) 
for j in m.J:
    print('p1(',j,') = %.3f' % pyo.value(m.p1[j]))
    
print('v2 = %.3f' % pyo.value(m.v2)) 
for k in m.K:
    print('p2(',k,') = %.3f' % pyo.value(m.p2[k]))