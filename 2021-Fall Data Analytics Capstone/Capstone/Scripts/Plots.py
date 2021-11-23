import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.ndimage.filters import gaussian_filter


df4 = pd.read_csv("trace_4.csv")

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

def heatplot(x, y, s, bins=1000):
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=bins)
    heatmap = gaussian_filter(heatmap, sigma=s)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    return heatmap.T, extent

img, extent = heatplot(df4['x'], df4['y'], 64)
ax.imshow(img, extent=extent, origin='lower', cmap=cm.jet)
ax.set_title("Smoothing with  $\sigma$ = %d" % s)