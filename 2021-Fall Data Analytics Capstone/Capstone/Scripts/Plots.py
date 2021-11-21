import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df1 = pd.read_csv("trace_1.csv")

plt.plot(df1['x'], df1['y'])
plt.show()

df4 = pd.read_csv("trace_4.csv")
heatmap, xedges, yedges = np.histogram2d(df4['x'], df4['y'], bins=10)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
plt.imshow(heatmap.T, extent=extent, origin='lower')
plt.show()