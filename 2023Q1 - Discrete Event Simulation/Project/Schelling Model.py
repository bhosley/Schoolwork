# -*- coding: utf-8 -*-
"""
@author: Hosley
"""
import numpy as np 
import matplotlib.pyplot as plt  
import matplotlib.animation as animation 
# Uncomment to display in .ipynb
# from IPython.display import HTML

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
    for _ in range(nMajority):
        a.append(Agent(1))
    for _ in range(nMinority):
        a.append(Agent(2))
    return a

def placeAgents(agents,grid,gridSize,):
    open = np.argwhere(grid[1:gridSize+1,1:gridSize+1]==0)
    for agent in agents:
        # select a random opening and move
        o = np.random.randint(0,len(open))
        i = open[o][0]+1    # index correction
        j = open[o][1]+1    # from argwhere shift
        agent.i = i
        agent.j = j
        grid[i,j] = agent.color
        # remove opening from list
        open = np.delete(open,o,0)
    return [agents,grid]

def checkHappy(agents,grid,fracHappy):
    uha = []
    numberUnhappy = 0
    for agent in agents:
        nSame = 0
        nDifferent = 0
        i = agent.i
        j = agent.j
        for m in range(int(i-1),int(i+2)):
            for n in range(int(j-1),int(j+2)):
                if (grid[m,n]==agent.color):
                    nSame=nSame+1
                elif(grid[m,n]!=0.0):
                    nDifferent = nDifferent+1
        # correct for self counting
        nSame = nSame - 1
        if(nSame+nDifferent == 0):
            agent.unhappy = False
        elif(fracHappy>=(((nSame)/(nSame+nDifferent)))):
            agent.unhappy = True
            numberUnhappy = numberUnhappy + 1
        else:
            agent.unhappy = False
    # print(numberUnhappy)
    return uha
                
def update(frameNum, img, grid, gridSize, agents): 
  
    # copy grid since we require 8 neighbors  
    # for calculation and we go line by line  
    newGrid = np.zeros([gridSize+2,gridSize+2]) 
    # find the list of open cells
    open = np.argwhere(grid[1:gridSize+1,1:gridSize+1]==0)
    for agent in agents:
        if(agent.unhappy):
            # select a random opening and move
            o = np.random.randint(0,len(open))
            i = open[o][0]+1    # index correction
            j = open[o][1]+1    # from argwhere shift
            agent.i = i
            agent.j = j
            # delete the opening from list
            open = np.delete(open,o,0)
        newGrid[agent.i,agent.j] = agent.color
        
    # check for unhappy agents
    checkHappy(agents,newGrid,fracHappy)
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
[agents,grid]= placeAgents(agents,grid,gridSize)
           
# set up animation 
fig, ax = plt.subplots() 
img = ax.imshow(grid, interpolation='nearest') 
ani = animation.FuncAnimation(fig, update, fargs=(img, grid,gridSize, agents, ), 
                              frames = 50, 
                              interval=updateInterval, 
                              save_count=50) 
  
plt.show() 

# uncomment to display in .ipynb
# HTML(ani.to_jshtml())