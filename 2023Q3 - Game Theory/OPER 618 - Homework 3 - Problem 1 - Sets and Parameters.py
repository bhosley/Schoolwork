# Coded by Dr. Brian J. Lunday, AFIT/ENS on 19 April 2022
# In support of OPER 618 Game Theory & Math Programming, Summer 2022

import pyomo.environ as pyo

m = pyo.ConcreteModel()

# Input sets
m.J = {1,2,3}
m.K = {1,2}

# Input parameter data
u1=[[0,0,0],
   [0, 0, 6], 
   [0, 2, 5],
   [0, 3, 3]]

u2=[[0,0,0],
   [0, 1, 0], 
   [0, 0, 2],
   [0, 4, 3]]