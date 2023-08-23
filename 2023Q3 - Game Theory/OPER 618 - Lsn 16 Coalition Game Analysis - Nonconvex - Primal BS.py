# Coded by Dr. Brian J. Lunday, AFIT/ENS on 20 April 2022
# In support of OPER 618 Game Theory & Math Programming, Summer 2022

import pyomo.environ as pyo

m = pyo.ConcreteModel()

# Input sets
m.I = {1,2,3} # pllayers
m.S = {1,2,3,4,5,6,7,8}
m.subsetS = {2,3,4,5,6,7,8}

# Dictionary of subset membership
subset =[[0,0,0,0,0,0,0,0,0],
         [0,0,1,0,0,1,1,0,1],
         [0,0,0,1,0,1,0,1,1],
         [0,0,0,0,1,0,1,1,1],]

# Define parameters
m.nu = {1:0,2:0.2,3:0.25,4:0.3,5:0.8,6:0.85,7:0.9,8:1}

# Define decision variables
m.x = pyo.Var(m.I,domain=pyo.NonNegativeReals)

# Formulate model
m.objfnvalue = pyo.Objective(expr = sum(m.x[i] for i in m.I),sense = pyo.minimize)
m.StableCoalitionConstraint=pyo.ConstraintList()
for s in m.subsetS:
    m.StableCoalitionConstraint.add(sum(subset[i][s]*m.x[i] for i in m.I) >= m.nu[s])

# Solve model
results=pyo.SolverFactory('cbc').solve(m,tee=False)

# Output results
print('z = ',pyo.value(m.objfnvalue))   
for i in m.I:
    print('x(',i,') = ', pyo.value(m.x[i]))
         