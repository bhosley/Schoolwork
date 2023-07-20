# Coded by Dr. Brian J. Lunday, AFIT/ENS on 19 April 2022
# In support of OPER 618 Game Theory & Math Programming, Summer 2022

import pyomo.environ as pyo
import os
os.environ['NEOS_EMAIL'] = 'brian.lunday+oper618@gmail.com' # Insert your own email address here, please

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
m.U2 = pyo.Var(domain=pyo.Reals) # Player 2's utility
m.s1 = pyo.Var(m.J,domain=pyo.NonNegativeReals) # s1[j] is the probabilty that Player 1 plays action j
m.r1 = pyo.Var(m.J,domain=pyo.NonNegativeReals) # Player 1's slack variable associated with the utility of playing action j 
m.s2 = pyo.Var(m.K,domain=pyo.NonNegativeReals) # s2[k] is the probabilty that Player 2 plays action k
m.r2 = pyo.Var(m.K,domain=pyo.NonNegativeReals) # Player 2's slack variable associated with the utility of playing action k 
m.z = pyo.Var(domain=pyo.NonNegativeReals) # A dummy variable to serve as the objective function
 
# Model (Formulation from page 91 of the text)
m.objfnvalue = pyo.Objective(expr = m.U1+m.U2, sense = pyo.minimize)
m.UtilityForPlayer1=pyo.ConstraintList()
for j in m.J:
    m.UtilityForPlayer1.add(sum(u1[j][k]*m.s2[k] for k in m.K) + m.r1[j] == m.U1)
m.UtilityForPlayer2=pyo.ConstraintList()
for k in m.K:
    m.UtilityForPlayer2.add(sum(u2[j][k]*m.s1[j] for j in m.J) + m.r2[k] == m.U2)
m.ProbabilityDistributionForP1 = pyo.Constraint(expr = sum(m.s1[j] for j in m.J) == 1)   
m.ProbabilityDistributionForP2 = pyo.Constraint(expr = sum(m.s2[k] for k in m.K) == 1)                         
m.ComplementarySlacknessForPlayer1=pyo.ConstraintList()
for j in m.J:
    m.ComplementarySlacknessForPlayer1.add(m.s1[j]*m.r1[j] == 0)
m.ComplementarySlacknessForPlayer2=pyo.ConstraintList()
for k in m.K:
    m.ComplementarySlacknessForPlayer2.add(m.s2[k]*m.r2[k] == 0)

# Solve model
results=pyo.SolverFactory('ipopt').solve(m,tee=False)
#solver_manager = pyo.SolverManagerFactory('neos')
#results = solver_manager.solve(m, solver = "octeract")

# Output results
print('U1 = %.3f' % pyo.value(m.U1)) 
for j in m.J:
    print('s1(',j,') = %.3f' % pyo.value(m.s1[j]))
print('U2 = %.3f' % pyo.value(m.U2))    
for k in m.K:
    print('s2(',k,') = %.3f' % pyo.value(m.s2[k]))