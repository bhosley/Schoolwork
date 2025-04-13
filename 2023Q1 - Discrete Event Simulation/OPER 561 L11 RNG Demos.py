{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Random number generator demos"
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
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Generators from the textbook"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def linear_congruential_method(X_i, a, c, m):\n",
    "    rand_int = (a*X_i + c) % m\n",
    "    return rand_int, rand_int/m  # return both the new seed and the resulting U(0, 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def make_some_random_numbers(input_dict, samples=5):  # just for testing\n",
    "    X_i = input_dict['seed']\n",
    "    for i in range(samples):\n",
    "        # BCNN uses R_i, while Law and others use U_i, for the random number\n",
    "        X_i, R_i = linear_congruential_method(X_i, input_dict['a'], input_dict['c'], input_dict['m'])\n",
    "        print(R_i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# generators from BCNN for possible demo purposes\n",
    "example_7_1 = dict(a=17, c=43, m=100, seed=27)  # period 4\n",
    "example_7_4 = dict(a=7**5, c=0, m=2**31 - 1, seed=123457)  # period long"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "make_some_random_numbers(example_7_1, samples=10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## AweSim RNG"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from numpy import linalg\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib.gridspec as gridspec\n",
    "\n",
    "# LCG parameters\n",
    "a = 781\n",
    "c = 381\n",
    "m = 1000\n",
    "\n",
    "# Initial seed. It will not change during execution\n",
    "Zi = 10\n",
    "\n",
    "# Z is the seed for the next random draw in the sequence. It will change in execution\n",
    "Z = Zi\n",
    "\n",
    "N = 1000\n",
    "U = np.zeros((2, N))\n",
    "\n",
    "\n",
    "\"\"\" Generates the next pseudo-random number from the multiplicative LCG \"\"\"\n",
    "def nextRand():\n",
    "    global Z\n",
    "    Z = (a*Z + c) % m\n",
    "    U = Z / m\n",
    "    return U\n",
    "\n",
    "\n",
    "# Generates the first 1000 pseudo-random numbers in the stream starting with Zi (seed)\n",
    "for i in range(N):\n",
    "    U[0, i] = nextRand()\n",
    "\n",
    "# Lags the RNG output in coupled pairs for x,y graphing\n",
    "for i in range(1, N):\n",
    "    U[1, i] = U[0, i-1]\n",
    "    \n",
    "# Graphs the 2-tuples\n",
    "plt.plot(U[0, :], U[1, :], 'bo')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## RandU RNG"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "\n",
    "randu = dict(a=65539, c=0, m=2**31, seed=314159)  # via http://physics.ucsc.edu/~peter/115/randu.pdf & IBM\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "from mpl_toolkits.mplot3d import Axes3D\n",
    "\n",
    "import numpy as np\n",
    "\n",
    "def plot_random_triples(input_dict, num_triples):\n",
    "    fig = plt.figure(figsize=(9,9))\n",
    "    ax = plt.axes(projection='3d', proj_type='ortho')\n",
    "    \n",
    "    res = np.zeros((num_triples, 3))\n",
    "\n",
    "    X_i = input_dict['seed']\n",
    "    for i in range(num_triples):  # inelegant but whatever\n",
    "        X_i, res[i, 0] = linear_congruential_method(X_i, input_dict['a'], input_dict['c'], input_dict['m'])\n",
    "        X_i, res[i, 1] = linear_congruential_method(X_i, input_dict['a'], input_dict['c'], input_dict['m'])\n",
    "        X_i, res[i, 2] = linear_congruential_method(X_i, input_dict['a'], input_dict['c'], input_dict['m'])\n",
    "                \n",
    "    ax.scatter(*res.T, s=5)  # transpose res then unpack the triples\n",
    "    ax.view_init(30, 30)  # useful starting point for randu\n",
    "    \n",
    "    return ax\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "ax = plot_random_triples(randu, 5000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
 "nbformat_minor": 2
}
