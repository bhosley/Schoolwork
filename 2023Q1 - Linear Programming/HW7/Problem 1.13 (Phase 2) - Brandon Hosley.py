#!/usr/bin/env python
# coding: utf-8

# # OPER 610
# ## Problem 1.13 (Phase 2)
# ### Brandon Hosley

import numpy as np
from pyomo.environ import * 
from pyomo.opt import SolverFactory

model = ConcreteModel()


# ## Definitions
# 
# Sets:
# - Products: $P = \{1,2,3\}$
# - Machines: $M = \{1,2,3,4\}$
# 	
# Parameters:
# - $c_{pm}$: Production Cost (a matrix drawn from the first table)
# - $t_{pm}$: Hours to produce units of product (a matrix drawn from the second table)
# - $u_p$   : Units of product $p$ required
# - $h_m$   : Hours machines $m$ available

# Labels for products and machines
model.P = Set(initialize=range(3))
model.M = Set(initialize=range(4))

# VARS
model.x = Var(model.P, model.M, domain=NonNegativeReals)

# Production constants
model.c = np.array([[4,4,5,7],
                    [6,7,5,6],
                    [12,10,8,11]])

model.t = np.array([[0.3,0.25,0.2,0.2],
                    [0.2,0.3,0.2,0.25],
                    [0.8,0.6,0.6,0.5]])     

# Scenario input/outputs
model.u = np.array([3000,6000,4000])
model.h = np.array([1500,1200,1500,2000])

# ## Objective Function
# 
# $\operatorname{min}\quad \sum_{p\in P} \sum_{m\in M} c_{pm}x_{pm}$

model.OBJ = Objective(expr=sum(model.x[p,m]*model.c[p,m] for p in model.P for m in model.M), sense=minimize)


# ## Constraints
# 
# $\sum_{m\in M} x_{pm} = u_p  \qquad \text{for } p\in P $
# $\sum_{p\in P} t_{pm}x_{pm}  \leq h_m  \quad \text{for } m\in M $
#         
# *Non-negativity constrained above*

model.constraints = ConstraintList()

# Meet production goals
for p in model.P:
    model.constraints.add(sum(model.x[p,m] for m in model.M) == model.u[p])
    
# Machine operating time limits
for m in model.M:
    model.constraints.add(sum(model.x[p,m]*model.t[p,m] for p in model.P) <= model.h[m])

# ## Solve

solver = SolverFactory('glpk')
sol = solver.solve(model, report_timing=True, tee=True)
model.pprint()

print("The solver terminated with the following decision variable values:")              
for x in model.x:
    if(value(model.x[x])>0):
       print("  ", x, format(value(model.x[x]),".2f"))