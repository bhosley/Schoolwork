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
m.U2 = pyo.Var(domain=pyo.Reals) # Player 2's utility
m.s1 = pyo.Var(m.J,domain=pyo.NonNegativeReals) # s1[j] is the probabilty that Player 1 plays action j

# Model (Formulation from page 88 of the text, modified for Player 1's strategy decisions to affect Player 2's utility)
m.objfnvalue = pyo.Objective(expr = m.U2, sense = pyo.minimize)
m.LowerBoundsOnUtilityForPlayer2=pyo.ConstraintList()
for k in m.K:
    m.LowerBoundsOnUtilityForPlayer2.add(sum(u2[j][k]*m.s1[j] for j in m.J) <= m.U2)
m.ProbabilityDistributionForP1 = pyo.Constraint(expr = sum(m.s1[j] for j in m.J) == 1)                         
                         
# Solve model
results=pyo.SolverFactory('ipopt').solve(m,tee=False)

# Output results
print('U2 = %.3f' % pyo.value(m.U2)) 
for j in m.J:
    print('s1(',j,') = %.3f' % pyo.value(m.s1[j]))
