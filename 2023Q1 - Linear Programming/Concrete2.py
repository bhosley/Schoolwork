# Example coded by Brian Lunday on 21 March 2022
import pyomo.environ as pyo

mc2 = pyo.ConcreteModel()

mc2.v={'hammer':8, 'wrench':6, 'screwdriver':4}
mc2.J = mc2.v.keys()

mc2.resourcebounds={'weight': 28, 'cost':20}
mc2.M = mc2.resourcebounds.keys()

mc2.resourceuse = {('weight','hammer'):5, ('weight','wrench'):7, ('weight','screwdriver'):4,
                     ('cost','hammer'):6,   ('cost','wrench'):4,   ('cost','screwdriver'):8}

mc2.x = pyo.Var(mc2.J, within=pyo.NonNegativeReals)

mc2.objfnvalue = pyo.Objective(expr = sum(mc2.v[j]*mc2.x[j] for j in mc2.J),sense = pyo.maximize)

mc2.ResourceConstraints=pyo.ConstraintList()
for i in mc2.M:
    mc2.ResourceConstraints.add(sum(mc2.resourceuse[i,j] * mc2.x[j] for j in mc2.J) <= mc2.resourcebounds[i])

solver = pyo.SolverFactory('cbc')
solver.options['presolve'] = 'off'
solver.options['sec'] = '10'
results = solver.solve(modelc1, tee = True)

print("")
print("The solver terminated with the following decision variable values:")              
for j in mc2.J:
    if(pyo.value(mc2.x[j])>0):
       print("  ", j, format(pyo.value(mc2.x[j]),".2f"))
       
print("")              
if (results.solver.status == pyo.SolverStatus.ok) and (results.solver.termination_condition==pyo.TerminationCondition.optimal):
    print ("The reported solution is optimal!")
elif results.solver.termination_condition == pyo.TerminationCondition.infeasible:
    print ("The reported solution is not feasible.")
else:
    print ("The results of the solution attempt are:", str(results.solver))       