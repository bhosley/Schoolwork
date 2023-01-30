from pyomo.environ import * 
from pyomo.opt import SolverFactory

model = ConcreteModel()

model.x1 = Var(domain = NonNegativeReals)
model.x2 = Var(domain = NonNegativeReals)

model.objective = Objective(expr = 3*model.x1 + 4*model.x2, sense = minimize)

model.constraints = ConstraintList()
model.constraints.add(model.x1 + 2*model.x2 <=  6)
model.constraints.add(2*model.x1 + model.x2 <=  4) 

solver = SolverFactory('glpk')
sol = solver.solve(model, report_timing=True, tee=True)
print(sol)