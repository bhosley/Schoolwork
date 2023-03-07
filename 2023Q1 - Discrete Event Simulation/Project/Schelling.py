import numpy as np 
import matplotlib.pyplot as plt  
import matplotlib.animation as animation 
# Uncomment to display in .ipynb
from IPython.display import HTML


class Agent:
    def __init__(self, membership, numTeams, h=0.3, i=0, j=0):
       self.team = membership
       self.homophily = h
       self.unhappy = False
       self.color = membership/numTeams
       self.i = i
       self.j = j


def initAgents(a,demographic):
    numTeams = len(demographic)
    for key,value in demographic.items():
        for _ in range(value['population']):
            a.append(Agent(key,numTeams,h=value['tolerance']))
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


def checkHappy(agents,grid):
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
        nBoth = nSame + nDifferent
        if(nBoth == 0):
            agent.unhappy = False
        elif(agent.homophily >=(((nSame)/(nBoth)))):
            agent.unhappy = True
            numberUnhappy = numberUnhappy + 1
        else:
            agent.unhappy = False
    return uha, numberUnhappy


def update(frameNum, img, grid, gridSize, agents,x,y,line):  
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
    _,n = checkHappy(agents,newGrid)
    # update data 
    img.set_data(newGrid) 
    grid[:] = newGrid[:] 

    x.append(frameNum)
    y.append(n)
    line.set_data(x,y)
    return img, line


def run_experiment(demographic=None,gridSize=100,withAnimation=False):
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
    move,unhappiness =[],[]
    #run trials without animations
    if not withAnimation:
        _ =+ 1
    #run trials with animation
    else:   
        # set up animation 
        updateInterval = 50
        fig, (ax1,ax2) = plt.subplots(1,2) 
        img = ax1.imshow(grid, interpolation='nearest') 
        line, = ax2.plot([], [], lw=3)
        ax2.set(xlim=(0,50), ylim=(0,200), aspect='0.25')
        ax1.set_title('Field')
        ax2.set_title('Total Unhappiness')
        ani = animation.FuncAnimation(fig, update, fargs=(img, grid,gridSize, agents,move,unhappiness,line, ), 
                                    frames = 50, 
                                    interval=updateInterval, 
                                    save_count=50) 
    
        #plt.show() 

        # uncomment to display in .ipynb
        return HTML(ani.to_jshtml())

# demographic -> label: [population,tolerance]
demographics = {
    1:{
    'population':4000,
    'tolerance':0.3},
    2:{
    'population':1000,
    'tolerance':0.3},
    3:{
    'population':1000,
    'tolerance':0.3}
}
run_experiment(demographics,withAnimation=True)