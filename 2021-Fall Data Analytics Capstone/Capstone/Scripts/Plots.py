import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.ndimage.filters import gaussian_filter

df4 = pd.read_csv("trace_4.csv")

#############
#  Heatmap  #
#############

fig, ax = plt.subplots()

def heatplot(x, y, s, bins=1000):
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=bins, range=[[-3, 3], [-3, 3]])
    heatmap = gaussian_filter(heatmap, sigma=s)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    return heatmap.T, extent

img, extent = heatplot(df4['x'], df4['y'], 32)
ax.imshow(img, extent= extent, origin= 'lower', cmap= cm.jet)
ax.axhline(y=0, color='w')
ax.axvline(x=0, color='w')
ax.axis('off')

plt.show()

##############
#  Re-Trace  #
##############

# Target Plot
#