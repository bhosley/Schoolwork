# Example coded by Brian Lunday on 21 March 2022
import pyomo.environ as pyo

v = {'hammer':8, 'wrench':6, 'screwdriver':4}
w = {'hammer':5, 'wrench':7, 'screwdriver':4}
c = {'hammer':6, 'wrench':4, 'screwdriver':8}
w_max = 28
c_max = 20

modelc1 = pyo.ConcreteModel()

modelc1.ITEMS = v.keys()
modelc1.x = pyo.Var(modelc1.ITEMS, within=pyo.NonNegativeReals)

modelc1.objfnvalue = pyo.Objective(expr = sum(v[j]*modelc1.x[j] for j in modelc1.ITEMS),sense = pyo.maximize)
modelc1.ConstraintOnWeight = pyo.Constraint(expr = sum(w[j]*modelc1.x[j] for j in modelc1.ITEMS) <= w_max)
modelc1.ConstraintOnCost = pyo.Constraint(expr = sum(c[j]*modelc1.x[j] for j in modelc1.ITEMS) <= c_max)

modelc1.pprint()
results=pyo.SolverFactory('cbc').solve(modelc1)
print(results)

for j in modelc1.ITEMS:
    print("  ", j, pyo.value(modelc1.x[j]))