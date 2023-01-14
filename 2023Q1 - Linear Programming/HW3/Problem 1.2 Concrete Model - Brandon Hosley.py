# OPER 610 - Brandon Hosley Problem 1.2 (Phase 2) Due Jan 17 2023

## Preparation

from pyomo.environ import * 
from pyomo.opt import SolverFactory

model = ConcreteModel()

## Variables and Coefficients

model.costs={'Compound1':20,'Compound2':30,'Compound3':20,'Compound4':15}
model.j=model.costs.keys()
model.compositions={'ElementA': {'Compound1':0.35,'Compound2':0.15,'Compound3':0.35,'Compound4':0.25},
                    'ElementB': {'Compound1':0.20,'Compound2':0.65,'Compound3':0.35,'Compound4':0.40},
                    'ElementC': {'Compound1':0.40,'Compound2':0.15,'Compound3':0.25,'Compound4':0.30}}
model.x = Var(model.j, domain = NonNegativeReals)

## Objective Function

model.objective = Objective(expr=sum(model.costs[j]*model.x[j] for j in model.j), sense=minimize)

## Constraints

model.constraints=ConstraintList()
model.constraints.add(sum(model.x[j] for j in model.j) == 1)                               # Ensure Percentage sums to 1
model.constraints.add(sum(model.compositions['ElementA'][j]*model.x[j] for j in model.j) == 0.25) # Percentage Compound A
model.constraints.add(sum(model.compositions['ElementB'][j]*model.x[j] for j in model.j) >= 0.35) # Percentage Compound B
model.constraints.add(sum(model.compositions['ElementC'][j]*model.x[j] for j in model.j) >= 0.20) # Percentage Compound C
model.constraints.add(model.x['Compound1'] >= 0.25)
model.constraints.add(model.x['Compound2'] >= 0.30)

## Solve

solver = SolverFactory('glpk')
sol = solver.solve(model, report_timing=True, tee=True)

## Results

print("The solver terminated with the following decision variable values:")              
for j in model.j:
    if(value(model.x[j])>0):
       print("  ", j, format(value(model.x[j]),".2f"))