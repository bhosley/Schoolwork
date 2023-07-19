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
m.U1 = pyo.Var(domain=pyo.NonNegativeReals) # Player 1's utility
m.U2 = pyo.Var(domain=pyo.NonNegativeReals) # Player 2's utility
m.p = pyo.Var(m.J,m.K,domain=pyo.NonNegativeReals) # p[j,k]=p1[j]*p2[k]
 
# Model  
m.objfnvalue = pyo.Objective(expr = m.U1+m.U2, sense = pyo.minimize)
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
                      
# Solve model
results=pyo.SolverFactory('cbc').solve(m,tee=False)

# Output results
print('U1 = %.3f' % pyo.value(m.U1))   
print('U2 = %.3f' % pyo.value(m.U2)) 

for j in m.J:
    for k in m.K:
        print('p(',j,',',k,') = %.3f' % pyo.value(m.p[j,k]))