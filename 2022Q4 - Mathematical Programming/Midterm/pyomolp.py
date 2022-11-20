from pyomo.environ import * 
from pyomo.opt import SolverFactory

model = ConcreteModel(name=”(My-Pyomo-Model)”)

model.x1 = Var(domain = NonNegativeReals, name = ‘Steel Export’)
model.x2 = Var(domain = NonNegativeReals, name = ‘Machine Export’)
model.x3 = Var(domain = NonNegativeReals, name = ‘Truck Export’)
model.x4 = Var(domain = NonNegativeReals, name = ‘Steel Production’)
model.x5 = Var(domain = NonNegativeReals, name = ‘Machine Production’)
model.x6 = Var(domain = NonNegativeReals, name = ‘Truck Production’)
model.x7 = Var(domain = NonNegativeReals, name = ‘Product X’)

model.objective = Objective(expr = 1225*model.x1 + 2500*model.x2 + 3000*model.x3\
    - 300*model.x4 - 150*model.x5 - 900*model.x6 + 751*model.x7, sense = maximize)

model.constraints = ConstraintList()
model.constraints.add(-1*model.x1 + 1*model.x4 -0.75*model.x5 - 1*model.x6 = 10000); # Steel Output 
model.constraints.add(-1*model.x2 + -0.05*model.x4 + 1*model.x5 - 0.1*model.x6 - 0.3*model.x7 = 0); # Machinery Output
model.constraints.add(-1*model.x3 - 0.08*model.x4 - 0.12*model.x5 + 1*model.x6 = 0);# Truck Output
model.constraints.add(model.x4 <= 300300);# Steel Capacity
model.constraints.add(model.x5 <= 50000);# Machinery Capacity
model.constraints.add(model.x6 <= 550000);# Truck Capacity
model.constraints.add(0.5*model.x4 + 5*model.x5 + 3*model.x6 + 1.5*model.x7 <= 1200000);# Manpower 

solver = SolverFactory(“/opt/ibm/ILOG/CPLEX_Studio1271/cplex/bin/x86–64_linux/cplexamp”)

sol = solver.solve(model)
print(sol)


print(‘x =’, model.x.value)

print(‘The objective value is =’,model.objective())
model.display()