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
m.lam = pyo.Var(m.S,initialize=0.1,domain=pyo.NonNegativeReals)

# Formulate model
m.objfnvalue = pyo.Objective(expr = sum(m.lam[s]*m.nu[s] for s in m.S),sense = pyo.maximize)
m.StableCoalitionConstraint=pyo.ConstraintList()
for i in m.I:
    m.StableCoalitionConstraint.add(sum(subset[i][s]*m.lam[s] for s in m.subsetS) == 1)

# Solve model
results=pyo.SolverFactory('cbc').solve(m,tee=False)

# Output results
print('z = ',pyo.value(m.objfnvalue))   
for s in m.subsetS:
    if pyo.value(m.lam[s])>0:
        print('lambda(',s,') = ', pyo.value(m.lam[s]))