# Written by Brandon Hosley for OPER 610 problem 1.6 (Phase 2) 23 02 23
import pyomo.environ as pyo
model = pyo.AbstractModel()

model.C = pyo.Set()
model.W = pyo.Set(ordered=True)

model.lbs_hour = pyo.Param(model.C)
model.hours_week = pyo.Param()
model.initial_staff = pyo.Param()
model.desired_growth = pyo.Param()

model.demand = pyo.Param(model.C, model.W)
model.d = pyo.Param(model.C, model.W, mutable=True) 

model.x = pyo.Var(model.C, model.W, domain=pyo.NonNegativeReals)
model.i = pyo.Var(model.C, model.W, domain=pyo.NonNegativeReals)
model.t = pyo.Var(model.W, domain=pyo.NonNegativeIntegers)
model.e = pyo.Var(model.W, domain=pyo.PositiveIntegers)

def obj_expression(m):
    return sum(m.e[w] for w in m.W)
model.objectivefunction = pyo.Objective(rule = obj_expression)

def labor_availability(m,w):
    if w == 1:
        return (m.t[w]/3 + sum(m.x[c,w] for c in m.C)) <= m.e[w] 
    else:
        return (m.t[w]/3 + m.t[w-1]/3 + sum(m.x[c,w] for c in m.C)) <= m.e[w]     
model.LaborConstraint = pyo.Constraint(model.W, rule = labor_availability)

def hiring_goal(m):
    return sum(m.t[w] for w in m.W) == m.desired_growth
model.HiringConstraint = pyo.Constraint(rule = hiring_goal)

def training_completion(m,w):
    if((w == 1) or (w == 2)):
        return m.e[1] == m.e[2]
    else:
        return (m.e[w-1] + m.t[w-2]) == m.e[w]
model.TrainingConstraint = pyo.Constraint(model.W, rule = training_completion)

def cheese_pipeline(m,c,w): 
    if w == 1:
        return (m.x[c,w] - m.i[c,w]) == m.d[c,w]
    else:
        return (m.x[c,w] + m.i[c,w-1] - m.i[c,w]) == m.d[c,w]
model.ProductionConstraint = pyo.Constraint(model.C, model.W, rule = cheese_pipeline)
    
def throttle_cheese(m,c,w):
    return pyo.Constraint.Skip if w == 1 else m.i[c,w-1] <= m.d[c,w]
model.SpoilageConstraint = pyo.Constraint(model.C, model.W, rule = throttle_cheese)

inst=model.create_instance('cheese.dat')

for c in inst.C:
    for w in inst.W:
        inst.d[c,w] = ((inst.demand[c,w] * 1000) / (inst.hours_week * inst.lbs_hour[c]))
        
inst.e[1].fix(inst.initial_staff)
inst.t[8].fix(0)
        
inst.pprint()

results=pyo.SolverFactory('glpk').solve(inst)

for w in inst.W.value:
    print(' week ', w, ':')
    print('    ', inst.t[w].value, ' new hires.')
    print('    ', inst.e[w].value, ' trained employees.')
    for c in inst.C.value:
        print('        ', c,' :', inst.x[c,w].value)
print('value :', inst.objectivefunction.expr())
