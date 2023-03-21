# Example coded by Brian Lunday on 22 March 2022
import pyomo.environ as pyo

from Abstract3model import ma2

instance=ma2.create_instance('Abstract3Data.dat')
instance.dual = pyo.Suffix(direction=pyo.Suffix.IMPORT)
results=pyo.SolverFactory('cplex').solve(instance)

for i in instance.Nodes.value:
    for j in instance.Nodes.value:
        if (i,j) in instance.Arcs and instance.Flow[i,j].value>0:
            print('(',i,',',j,') :', instance.Flow[i,j].value)
print('value :', instance.Obj.expr())

print ("Duals")
for c in instance.component_objects(pyo.Constraint, active=True):
    print (" Constraint",c)
for index in c:
    print (" ", index, instance.dual[c[index]])