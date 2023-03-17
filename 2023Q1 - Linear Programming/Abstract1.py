# Example coded by Brian Lunday on 22 March 2022
import pyomo.environ as pyo

modela1 = pyo.AbstractModel()

modela1.I=pyo.Set()
modela1.J=pyo.Set()

modela1.value=pyo.Param(modela1.J)
modela1.resourcebounds=pyo.Param(modela1.I)
modela1.resourceuse =pyo.Param(modela1.I,modela1.J)

modela1.x=pyo.Var(modela1.J,domain=pyo.NonNegativeReals)

def obj_expression(m):
    return pyo.summation(m.value,m.x)
modela1.objectivefunction = pyo.Objective(rule=obj_expression,sense = pyo.maximize)

def resource_constraint_rule(m,i):
    return sum(m.resourceuse[i,j] * m.x[j] for j in m.J) <= m.resourcebounds[i]
modela1.ResourceConstraint = pyo.Constraint(modela1.I, rule=resource_constraint_rule)

instance=modela1.create_instance('Abstract1Data.dat')
instance.pprint()

results=pyo.SolverFactory('cbc').solve(instance)

for j in instance.J.value:
    print(j,' :', instance.x[j].value)
print('value :', instance.objectivefunction.expr())