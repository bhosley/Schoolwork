import numpy as np
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt
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

def getSegments(df):
    segs = [[],[],[],[]]
    segs[0] = df.query('time <= @IMPACT_TIME-1')
    segs[1] = df.query('time <= @IMPACT_TIME-0.4' and 'time >= @IMPACT_TIME-1')
    segs[2] = df.query('time <= @IMPACT_TIME' and 'time >= @IMPACT_TIME-0.4')
    segs[3] = df.query('time >= @IMPACT_TIME')
    return segs

def target(ax):
    ax.grid(alpha=0.4)
    ax.patch.set_facecolor('ivory')   
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
        color='whitesmoke', linewidth=0
    )

def polarize(df):
    polar = pd.DataFrame(columns = ['time', 'rho', 'phi'])
    polar['rho'], polar['phi'] = cart2pol(df['x'], df['y'])
    if 'time' in df: 
        polar['time'] = df['time']
    return polar

#############
#  Heatmap  #
#############

plt.figure(0)

img, extent = heatplot(df4['x'], df4['y'], 32)
plt.imshow(img, extent= extent, origin= 'lower', cmap= cm.jet)
plt.axhline(y=0, color='w')
plt.axvline(x=0, color='w')
plt.axis('off')

plt.savefig('../images/heatmap.png')

##############
#  Re-Trace  #
##############

# plt.figure(1)
df4_polar = polarize(df4)
segments = getSegments(df4_polar)
seg_color = ['g','y','b','r']

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
target(ax)

for i in range(0,4):
    ax.plot(segments[i]['phi'], segments[i]['rho'], color=seg_color[i])

plt.savefig('../images/trace.png')

#################
#  Time-Scalar  #
#################

plt.figure(2)
plt.axhspan(0,29.75, color='lightgray')
for i in [2.5, 5.75, 29.75, 77.75]:
    plt.axhline(i, color='darkgray')
for i in range(0,4):
    plt.plot(segments[i]['time'], segments[i]['rho'], color=seg_color[i])

plt.savefig('../images/distance_from_center.png')

#################
#  Plot Points  #
#################

#plt.figure(3)
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
target(ax)

df = pd.read_csv("TargetScan Data.csv")
df_polar = polarize(df)
ax.scatter(x=df_polar['phi'],y=df_polar['rho'])

plt.savefig('../images/points.png')

####################
#  Heatmap Points  #
####################

plt.figure(4)
img, extent = heatplot(df['x'], df['y'], 16)
plt.imshow(img, extent= extent, origin= 'lower', cmap= cm.jet)
plt.axhline(y=0, color='w')
plt.axvline(x=0, color='w')
plt.axis('off')

plt.savefig('../images/point_heats.png')
plt.show()