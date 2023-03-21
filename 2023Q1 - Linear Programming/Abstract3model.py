# Example coded by Brian Lunday on 22 March 2022
import pyomo.environ as pyo

ma2 = pyo.AbstractModel()

ma2.Nodes=pyo.Set()
ma2.Arcs=pyo.Set(dimen=2)

ma2.Flow = pyo.Var(ma2.Arcs, domain=pyo.NonNegativeReals)
ma2.FlowCost = pyo.Param(ma2.Arcs)
ma2.FlowUB = pyo.Param(ma2.Arcs)
ma2.Supply = pyo.Param(ma2.Nodes)

def Obj_rule(m):
    return pyo.summation(m.FlowCost, m.Flow)
ma2.Obj = pyo.Objective(rule=Obj_rule, sense=pyo.minimize)

def FlowBalance_rule(m,i):
    return m.Supply[i] + sum(m.Flow[j, i] for j in m.Nodes if (j,i) in m.Arcs) == \
           sum(m.Flow[i,j] for j in m.Nodes if (i,j) in m.Arcs)           
ma2.FlowBalanceConstraint = pyo.Constraint(ma2.Nodes, rule=FlowBalance_rule)

def FlowUB_rule(m,i,j):
    return m.Flow[i,j] <= m.FlowUB[i,j]
ma2.FlowUBConstraint = pyo.Constraint(ma2.Arcs, rule=FlowUB_rule)