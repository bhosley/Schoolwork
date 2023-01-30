# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:50:26 2020

@author: lance
"""

# Python code to implement Conway's Game Of Life 
import argparse 
import numpy as np 
import matplotlib.pyplot as plt  
import matplotlib.animation as animation 
  
#set animation update interval
updateInterval = 50

#set simulation parameters
nMajority = 5000
nMinority = 1000
fracHappy = 0.3
gridSize = 100
  
class Agent:
    def __init__(self, r=1, i=0, j=0):
       self.race = r
       self.unhappy = False
       if (self.race==1):
           self.color = 0.5
       elif (self.race==2): 
           self.color = 1.0
       else:
           self.color = 0.0
       self.i = i
       self.j = j
           
def initAgents(a,nMajority,nMinority):
    for i in range(nMajority):
        a.append(Agent(1))
    for i in range(nMinority):
        a.append(Agent(2))
    return a

def placeAgents(agents,grid,gridSize,nMajority,nMinority):
    for k in range(nMajority+nMinority):
        i = np.random.randint(1,gridSize+1,1)
        j = np.random.randint(1,gridSize+1,1)
        while (grid[i,j] != 0):
            i = np.random.randint(1,gridSize+1,1)
            j = np.random.randint(1,gridSize+1,1)
        agents[k].i = i
        agents[k].j = j
        grid[i,j] = agents[k].color
    return [agents,grid]

def checkHappy(agents,grid,nMajority,nMinority,fracHappy):
    uha = []
    numberUnhappy = 0
    for k in range(nMajority+nMinority):
        nSame = 0
        nDifferent = 0
        i = agents[k].i
        j = agents[k].j
        for m in range(-1,2):
            for n in range(-1,2):
                if (grid[i+m,j+n]==agents[k].color):
                    nSame=nSame+1
                elif(grid[i+m,j+n]!=0.0):
                    nDifferent = nDifferent+1
        nSame = nSame - 1
        if(nSame+nDifferent == 0):
            agents[k].unhappy = False
        elif(fracHappy>=(((nSame)/(nSame+nDifferent)))):
            agents[k].unhappy = True
            numberUnhappy = numberUnhappy + 1
        else:
            agents[k].unhappy = False
    # print(numberUnhappy)
    return uha
                
def update(frameNum, img, grid, nMajority, nMinority, gridSize, agents): 
  
    # copy grid since we require 8 neighbors  
    # for calculation and we go line by line  
    newGrid = np.zeros([gridSize+2,gridSize+2]) 

    for k in range(nMajority+nMinority):
        if(agents[k].unhappy):
            i = np.random.randint(1,gridSize+1,1)
            j = np.random.randint(1,gridSize+1,1)
            while (grid[i,j] != 0):
                i = np.random.randint(1,gridSize+1,1)
                j = np.random.randint(1,gridSize+1,1)
        
            agents[k].i = i
            agents[k].j = j
        newGrid[agents[k].i,agents[k].j] = agents[k].color
        
    # check for unhappy agents
    checkHappy(agents,newGrid,nMajority,nMinority,fracHappy)
    # update data 
    img.set_data(newGrid) 
    grid[:] = newGrid[:] 
    return img, 
  
#initialize grid
grid = np.zeros([gridSize+2,gridSize+2])

agents = []
unhappyAgents = []

#instantiate agents
agents = initAgents(agents,nMajority,nMinority)

#place agents
[agents,grid]= placeAgents(agents,grid,gridSize,nMajority,nMinority)

#check for unhappy agents and collect them in an array
unhappyAgents = checkHappy(agents,grid,nMajority,nMinority,fracHappy)

np.random.randint(0,5,3)
           
# set up animation 
fig, ax = plt.subplots() 
img = ax.imshow(grid, interpolation='nearest') 
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, nMajority, nMinority, gridSize, agents, ), 
                              frames = 10, 
                              interval=updateInterval, 
                              save_count=50) 
  
plt.show() 

