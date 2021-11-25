from matplotlib import colors
import numpy as np
from numpy.core.fromnumeric import size
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
from scipy.ndimage.filters import gaussian_filter

IMPACT_TIME = 22.7708

df4 = pd.read_csv("trace_4.csv")

###############
#  Functions  #
###############

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return rho, phi

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return x, y

def heatplot(x, y, s, bins=1000):
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=bins, range=[[-85, 85], [-85, 85]])
    heatmap = gaussian_filter(heatmap, sigma=s)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    return heatmap.T, extent

def target(ax):
    ax.grid(alpha=0.2)   
    ax.axes.get_xaxis().set_ticks([])
    ax.axes.get_yaxis().set_ticklabels([])
    ax.set_ylim([0, 77.75])

    rings = [2.5, 5.75]
    for i in range(0,8):                            # Ring values
        y = ((8-i)*8) + 5.75
        rings.append(y)
        for d in [0,0.5*np.pi,np.pi,1.5*np.pi,]:    # Value directions           
            ax.annotate(str(i+1), xy=(d, y+4),      # y+4 for centering
                ha='center', va='center', size='x-small') 
            
    ax.axes.get_yaxis().set_ticks(rings)
    ax.fill_between(
        np.linspace(0, 2*np.pi, 100),    # Theta fill range
        0, 29.75,                        # Radius fill range
        color='grey', alpha=0.25, linewidth=0
    )

#############
#  Heatmap  #
#############

fig, ax = plt.subplots()

img, extent = heatplot(df4['x'], df4['y'], 32)
ax.imshow(img, extent= extent, origin= 'lower', cmap= cm.jet)
ax.axhline(y=0, color='w')
ax.axvline(x=0, color='w')
ax.axis('off')

#plt.show()

##############
#  Re-Trace  #
##############

df4_polar = pd.DataFrame(columns = ['time', 'x', 'y'])
df4_polar['rho'], df4_polar['phi'] = cart2pol(df4['x'], df4['y'])
df4_polar['time'] = df4['time']

seg_color = ['g','y','b','r']
segments = [[],[],[],[]]
segments[0] = df4_polar.query('time <= @IMPACT_TIME-1')
segments[1] = df4_polar.query('time <= @IMPACT_TIME-0.4' and 'time > @IMPACT_TIME-1')
segments[2] = df4_polar.query('time <= @IMPACT_TIME' and 'time > @IMPACT_TIME-0.4')
segments[3] = df4_polar.query('time > @IMPACT_TIME')

fig, ax = plt.subplots()
ax = fig.add_subplot(111, polar=True)
target(ax)

for i in range(0,4):
    ax.plot(segments[i]['phi'], segments[i]['rho'], color=seg_color[i])

#plt.show()

##############
#  Re-Trace  #
##############

fig, ax = plt.subplots()
for i in range(0,4):
    ax.plot(segments[i]['time'], segments[i]['rho'], color=seg_color[i])
for i in [2.5, 5.75, 29.75]:
    ax.axhline(i, color='gray')

plt.show()
'''
'''