{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Accept-Reject Random Variate Generation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib notebook \n",
    "# run before imports; enable interactive mode"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "import random\n",
    "\n",
    "import numpy as np\n",
    "import scipy.stats \n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Standard Normal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 3 instantiations of Random object to create \"independent\" streams\n",
    "r1 = random.Random()\n",
    "r2 = random.Random()\n",
    "r3 = random.Random()\n",
    "\n",
    "c = (2*math.sqrt(math.e)) / math.sqrt(2*math.pi)\n",
    "\n",
    "# Generates pdf of interest\n",
    "X = np.zeros((4, 1000))\n",
    "\n",
    "for i in range(1000):\n",
    "    X[0, i] = 0.005 * i  # horizontal step\n",
    "    X[1, i] = scipy.stats.halfnorm.pdf(X[0, i], 0, 1)\n",
    "#     X[2, i] = scipy.stats.expon.pdf(X[0, i], 0, 1)\n",
    "#     X[3, i] = c * X[2, i]\n",
    "\n",
    "num_accepted = 0\n",
    "num_rejected = 0\n",
    "accepted = np.zeros((2, 1))\n",
    "rejected = np.zeros((2, 1))\n",
    "count = 0\n",
    "\n",
    "while num_accepted < 1000:\n",
    "    count = count + 1\n",
    "    Y = -math.log(r1.random())\n",
    "    Z = r2.random() * c\n",
    "    if Z < math.e**(-((Y-1)**2) / 2):\n",
    "        num_accepted = num_accepted + 1\n",
    "        if(r3.random() >= 0.5):\n",
    "            Y = -Y\n",
    "        accepted = np.append(accepted, [[Y], [0]], 1)\n",
    "    else:\n",
    "        num_rejected = num_rejected + 1\n",
    "        rejected = np.append(rejected, [[Y], [c]], 1)\n",
    "\n",
    "# Prints generated variates to a file. Delete comment on next line for file\n",
    "# np.savetxt(\"<YOUR PATH NAME HERE>/NormVariateGeneration.txt\", accepted[0, 1:], fmt='%.4f')\n",
    "        \n",
    "# Plots of interest\n",
    "fig, ax = plt.subplots()\n",
    "\n",
    "ax.plot(X[0, :], X[1, :], 'k-')\n",
    "ax.plot(accepted[0, 1:], accepted[1, 1:], 'go')\n",
    "ax.plot(rejected[0, 1:], rejected[1, 1:], 'rx')\n",
    "\n",
    "print('rejected: ', num_rejected, '   accepted: ', num_accepted)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Beta(4, 3) Distribution"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "r1 = random.Random()\n",
    "r2 = random.Random()\n",
    "\n",
    "c = 2.0736\n",
    "  \n",
    "# Generate pdf of interest\n",
    "X = np.zeros((2, 1000))\n",
    "\n",
    "for i in range(1000):\n",
    "    X[0, i] = 0.001 * i\n",
    "    X[1, i] = scipy.stats.beta.pdf(X[0, i], 4, 3)\n",
    "\n",
    "    \n",
    "def f(x):\n",
    "    if x < 0:\n",
    "        return 0\n",
    "    elif x > 1:\n",
    "        return 1\n",
    "    else:\n",
    "        return scipy.stats.beta.pdf(x, 4, 3)\n",
    "\n",
    "\n",
    "num_accepted = 0\n",
    "num_rejected = 0\n",
    "accepted = np.zeros((2, 1))\n",
    "rejected = np.zeros((2, 1))\n",
    "count = 0\n",
    "\n",
    "while num_accepted < 100:\n",
    "    count = count + 1\n",
    "    Y = r1.random()\n",
    "    Z = r2.random() * c\n",
    "    if Z < f(Y):\n",
    "        num_accepted += 1\n",
    "        accepted = np.append(accepted, [[Y], [0]], 1)\n",
    "    else:\n",
    "        num_rejected += 1\n",
    "        rejected = np.append(rejected, [[Y], [c]], 1)\n",
    "\n",
    "fig, ax = plt.subplots()\n",
    "\n",
    "ax.plot(X[0, :], X[1, :], 'c-')\n",
    "ax.plot(accepted[0, 1:], accepted[1, 1:], 'go')\n",
    "ax.plot(rejected[0, 1:], rejected[1, 1:], 'rx')\n",
    "\n",
    "print('rejected: ', num_rejected, '   accepted: ', num_accepted)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
