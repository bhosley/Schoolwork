# Coded by Dr. Brian J. Lunday, AFIT/ENS on 19 April 2022
# In support of OPER 618 Game Theory & Math Programming, Summer 2022

import pyomo.environ as pyo
import os
os.environ['NEOS_EMAIL'] = 'brian.lunday+oper618@gmail.com' # Insert your own email address here, please

m = pyo.ConcreteModel()

# Input sets
m.J = {1,2}
m.K = {1,2}

# Input parameter data
u1=[[0,0,0],
   [0, 0, 9], 
   [0, 3, 7]]
u2=[[0,0,0],
   [0, 0, 3], 
   [0, 9, 7]]

# Decision Variables
m.U1 = pyo.Var(domain=pyo.NonNegativeReals) # Player 1's utility
m.U2 = pyo.Var(domain=pyo.NonNegativeReals) # Player 2's utility
m.p1 = pyo.Var(m.J,domain=pyo.NonNegativeReals) # p1[j] is the probabilty that Player 1 plays action j
m.p2 = pyo.Var(m.K,domain=pyo.NonNegativeReals) # p2[k] is the probabilty that Player 2 plays action k
m.p = pyo.Var(m.J,m.K,domain=pyo.NonNegativeReals) # p[j,k]=p1[j]*p2[k]

# Model  
m.objfnvalue = pyo.Objective(expr = 0*m.U1+m.U2, sense = pyo.minimize)
m.UtilityForPlayer1= pyo.Constraint(expr= m.U1==sum(sum(m.p[j,k]*u1[j][k] for j in m.J) for k in m.K))
m.UtilityForPlayer2= pyo.Constraint(expr= m.U2==sum(sum(m.p[j,k]*u2[j][k] for j in m.J) for k in m.K))
m.NEcriteriaP1=pyo.ConstraintList()
for j in m.J:
    for jp in m.J:
        if jp!=j:
            m.NEcriteriaP1.add(sum(m.p[j,k]*u1[j][k] for k in m.K) >= sum(m.p[j,k]*u1[jp][k] for k in m.K))
m.NEcriteriaP2=pyo.ConstraintList()
for k in m.K:
    for kp in m.K:
        if kp!=k:
            m.NEcriteriaP2.add(sum(m.p[j,k]*u2[j][k] for j in m.J) >= sum(m.p[j,k]*u2[j][kp] for j in m.J))
m.ProbabilityDistribution= pyo.Constraint(expr= sum(sum(m.p[j,k] for j in m.J) for k in m.K)==1)
m.JointPDFCalculations=pyo.ConstraintList()
for j in m.J:
    for k in m.K:
        m.JointPDFCalculations.add(m.p[j,k]==m.p1[j]*m.p2[k])
m.ProbabilityDistributionForP1 = pyo.Constraint(expr = sum(m.p1[j] for j in m.J) == 1)   
m.ProbabilityDistributionForP2 = pyo.Constraint(expr = sum(m.p2[k] for k in m.K) == 1)   
                      
# Solve model
#results=pyo.SolverFactory('ipopt').solve(m,tee=False)
solver_manager = pyo.SolverManagerFactory('neos')
results = solver_manager.solve(m, solver = "octeract")

# Output results
print('U1 = %.3f' % pyo.value(m.U1)) 
for j in m.J:
    print('p1(',j,') = %.3f' % pyo.value(m.p1[j]))
    
print('U2 = %.3f' % pyo.value(m.U2)) 
for k in m.K:
    print('p2(',k,') = %.3f' % pyo.value(m.p2[k]))

for j in m.J:
    for k in m.K:
        print('p(',j,',',k,') = %.3f' % pyo.value(m.p[j,k]))