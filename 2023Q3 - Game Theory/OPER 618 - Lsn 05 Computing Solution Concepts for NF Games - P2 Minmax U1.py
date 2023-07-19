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

# Decision Variables
m.U1 = pyo.Var(domain=pyo.Reals) # Player 1's utility
m.s2 = pyo.Var(m.K,domain=pyo.NonNegativeReals) # s2[k] is the probabilty that Player 2 plays action k

# Model (Formulation from page 88 of the text)
m.objfnvalue = pyo.Objective(expr = m.U1, sense = pyo.minimize)
m.LowerBoundsOnUtilityForPlayer1=pyo.ConstraintList()
for j in m.J:
    m.LowerBoundsOnUtilityForPlayer1.add(sum(u1[j][k]*m.s2[k] for k in m.K) <= m.U1)
m.ProbabilityDistributionForP2 = pyo.Constraint(expr = sum(m.s2[k] for k in m.K) == 1)                         
                         
# Solve model
results=pyo.SolverFactory('cbc').solve(m,tee=False)

# Output results
print('U1 = %.3f' % pyo.value(m.U1)) 
for k in m.K:
    print('s2(',k,') = %.3f' % pyo.value(m.s2[k]))