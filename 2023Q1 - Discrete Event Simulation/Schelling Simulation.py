# -*- coding: utf-8 -*-
"""

@author: Hosley
"""

import numpy as np 
from math import floor
from collections import Counter
import matplotlib.pyplot as plt  
import matplotlib.animation as animation 

'''
If using this script in an .ipynb import:
    from IPython.display import HTML

and uncomment the following line in the run_animation function:
    ani = HTML(ani.to_jshtml())
'''


class Agent:
    def __init__(self, membership, numTeams, utility_function, i=0, j=0):
       self.team = membership
       self.utility_function = utility_function
       self.unhappy = False
       self.color = membership/numTeams
       self.i = i
       self.j = j


def initAgents(agent_list,demographic):
    numTeams = len(demographic)
    for key,value in demographic.items():
        for _ in range(value['population']):
            agent_list.append(Agent(key,numTeams,value['utility function']))
    return agent_list


def placeAgents(agents,grid,gridSize,):
    open_cells = np.argwhere(grid[1:gridSize+1,1:gridSize+1]==0)
    for agent in agents:
        # select a random opening o and get coordinates
        o = np.random.randint(0,len(open_cells))
        i = open_cells[o][0]+1    # index correction
        j = open_cells[o][1]+1    # from argwhere shift
        # migrate agent to cell (i,j)
        agent.i = i
        agent.j = j
        grid[i,j] = agent.color
        # remove opening from list of openings
        open_cells = np.delete(open_cells,o,0)
    return [agents,grid]


def checkHappy(agents,grid,nbrhd=3):
    '''
    This function returns the count of unhappy agents.
    It mutates agents by taking the agent list and corresponding 
    grid state and updates the happiness attribute of each agent 
    instance based on the neighborhood N x N size.
    '''
    unhappy_agent_count = 0
    dim = floor(nbrhd/2) # The length of the neighborhood in each direction
    for agent in agents:
        neighbors_list = []
        i = agent.i
        j = agent.j
        try:
            # Gather a list of the agent's neighbors
            for m in range(int(i-dim),int(i+dim+1)):
                for n in range(int(j-dim),int(j+dim+1)):
                    neighbors_list.append(grid[m,n])
            # Tally: a dictionary of types and counts of neighbors
            tally = Counter(neighbors_list)
            # Check tally against agent's utility function
            if(agent.utility_function(tally,agent)):
                agent.unhappy = False
            else:
                agent.unhappy = True
                unhappy_agent_count += 1
        except IndexError:
            agent.unhappy = True
            unhappy_agent_count += 1
    return unhappy_agent_count


def update(frameNum,grid,gridSize,agents,x,y,nbrhd=3,img=None,line=None):  
    # copy grid since we require 8 neighbors  
    # for calculation and we go line by line  
    newGrid = np.zeros([gridSize+2,gridSize+2]) 
    # find the list of open cells
    open_cells = np.argwhere(grid[1:gridSize+1,1:gridSize+1]==0)
    for agent in agents:
        if(agent.unhappy and len(open_cells)>0):
            # select a random opening and move
            o = np.random.randint(0,len(open_cells))
            i = open_cells[o][0]+1    # index correction
            j = open_cells[o][1]+1    # from argwhere shift
            agent.i = i
            agent.j = j
            # delete the opening from list
            open = np.delete(open_cells,o,0)
        newGrid[agent.i,agent.j] = agent.color
        
    # check for unhappy agents
    n = checkHappy(agents,newGrid,nbrhd)
    # update data 
    if img: img.set_data(newGrid) 
    grid[:] = newGrid[:] 

    x.append(frameNum)
    y.append(n)
    if line: line.set_data(x,y)
    return img, x, y, line

#run single trial with animation
def run_animation(demographic=None,gridSize=100,frames=50,nbrhd=3,filename='test'):
    demographics = demographic or {
        1:{'population':5000,'tolerance':0.3},
        2:{'population':1000,'tolerance':0.3}}

    #initialize grid
    grid = np.zeros([gridSize+2,gridSize+2])

    #instantiate agents
    agents = []
    agents = initAgents(agents,demographics)

    #place agents
    [agents,grid]= placeAgents(agents,grid,gridSize)
    #data collection
    x,y =[],[]
    # set up animation 
    fig, (ax1,ax2) = plt.subplots(1,2) 
    fig.tight_layout(h_pad=4)
    img = ax1.imshow(grid, interpolation='nearest') 
    line, = ax2.plot([], [], lw=3)
    height = sum([demo['population'] for demo in demographics.values()])
    width = frames
    ax2.set(xlim=(0,width), ylim=(0,height), aspect=width/height)
    #ax2.set_yscale('log')
    ax1.set_title('Field', pad=20)
    ax2.set_title('Total Unhappiness', pad=20)
    ani = animation.FuncAnimation(fig,update,
                                fargs=(grid,gridSize,agents,x,y,nbrhd,img,line,), 
                                frames = frames, 
                                interval=100, 
                                repeat_delay = 9000)  
    # ani = HTML(ani.to_jshtml())
    '''
    # Uncomment to save the figure as an image
    extent = ax1.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig('images/{}.png'.format(filename), bbox_inches=extent.expanded(1.22,1.15).translated(-0.17,-0.1))
    '''
    return ani


'''
EXAMPLE USE
'''


parameters = {
    1:{
    'population':3000,
    'utility function': lambda t,agent : (t[agent.color]-1)/8 > 0.3}, 
    # Agent is happy if more than 30% of 8 neighbors is the same
    2:{
    'population':3000,
    'utility function': lambda t,agent : (t[agent.color]-1)/8 > 0.3}
}

ani = run_animation(parameters, filename='filename',gridSize=100,frames=100,nbrhd=3)
plt.show()