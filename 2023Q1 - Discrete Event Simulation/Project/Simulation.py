{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Revisiting Schelling's Games\n",
    "Branndon Hosley\n",
    "\n",
    "### Tasks\n",
    "- Implementing a Schelling Model\n",
    "    - Abstract variables\n",
    "    - Collect Data\n",
    "    - Optimize\n",
    "- Variables Concerned\n",
    "    - Population Ratio\n",
    "    - Utility Ratio\n",
    "    - Number of Groups\n",
    "    - Integrationism\n",
    "    - Irregular Utility\n",
    "- Qualitative Analysis\n",
    "- Quantitative Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import Schelling as sc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "baseline = {\n",
    "    1:{\n",
    "    'population':3000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3},\n",
    "    2:{\n",
    "    'population':3000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3}\n",
    "}\n",
    "sc.run_experiment(baseline, filename='Baseline',frames=100)\n",
    "ani = sc.run_animation(baseline, filename='Baseline',frames=100)\n",
    "ani"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "largeMajority = {\n",
    "    1:{\n",
    "    'population':5000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3},\n",
    "    2:{\n",
    "    'population':1000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3}\n",
    "}\n",
    "sc.run_experiment(largeMajority, filename='LargeMajority',frames=100)\n",
    "ani = sc.run_animation(largeMajority, filename='LargeMajority',frames=100)\n",
    "ani"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "largeMajorityLowDensity = {\n",
    "    1:{\n",
    "    'population':4000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3},\n",
    "    2:{\n",
    "    'population':800,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3}\n",
    "}\n",
    "sc.run_experiment(largeMajorityLowDensity, filename='LargeMajorityLowDensity',frames=100)\n",
    "ani = sc.run_animation(largeMajorityLowDensity, filename='LargeMajorityLowDensity',frames=100)\n",
    "ani"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "asymmetricUtility = {\n",
    "    1:{\n",
    "    'population':3000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.5},\n",
    "    2:{\n",
    "    'population':3000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.2}\n",
    "}\n",
    "sc.run_experiment(asymmetricUtility, filename='AsymmetricUtility',frames=100)\n",
    "ani = sc.run_animation(asymmetricUtility, filename='AsymmetricUtility',frames=100)\n",
    "ani"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "lessAsymmetricUtilityLongRun = {\n",
    "    1:{\n",
    "    'population':3500,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.5},\n",
    "    2:{\n",
    "    'population':2500,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3}\n",
    "}\n",
    "sc.run_experiment(lessAsymmetricUtilityLongRun, filename='LessAsymmetricUtilityLongRun',frames=200,reps=2)\n",
    "ani = sc.run_animation(lessAsymmetricUtilityLongRun, filename='LessAsymmetricUtilityLongRun',frames=200)\n",
    "ani"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "lessAsymmetricUtilityLessDenseLongRun = {\n",
    "    1:{\n",
    "    'population':3000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.5},\n",
    "    2:{\n",
    "    'population':2000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3}\n",
    "}\n",
    "sc.run_experiment(lessAsymmetricUtilityLessDenseLongRun, filename='LessAsymmetricUtilityLessDenseLongRun',frames=200,reps=2)\n",
    "ani = sc.run_animation(lessAsymmetricUtilityLessDenseLongRun, filename='LessAsymmetricUtilityLessDenseLongRun',frames=200)\n",
    "ani"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "threeGroups = {\n",
    "    1:{\n",
    "    'population':2000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3 if (t[agent.color]>1) else False},\n",
    "    2:{\n",
    "    'population':2000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3 if (t[agent.color]>1) else False},\n",
    "    3:{\n",
    "    'population':2000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3 if (t[agent.color]>1) else False}\n",
    "}\n",
    "sc.run_experiment(threeGroups, filename='ThreeGroups',frames=100)\n",
    "ani = sc.run_animation(threeGroups, filename='ThreeGroups',frames=100)\n",
    "ani"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "sixGroups = {\n",
    "    1:{\n",
    "    'population':1000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3},\n",
    "    2:{\n",
    "    'population':1000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3},\n",
    "    3:{\n",
    "    'population':1000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3},\n",
    "    4:{\n",
    "    'population':1000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3},\n",
    "    5:{\n",
    "    'population':1000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3},\n",
    "    6:{\n",
    "    'population':1000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3}\n",
    "}\n",
    "sc.run_experiment(sixGroups, filename='SixGroups',frames=100)\n",
    "ani = sc.run_animation(sixGroups, filename='SixGroups',frames=100)\n",
    "ani"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "sixGroupsLongRun = {\n",
    "    1:{\n",
    "    'population':1000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3},\n",
    "    2:{\n",
    "    'population':1000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3},\n",
    "    3:{\n",
    "    'population':1000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3},\n",
    "    4:{\n",
    "    'population':1000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3},\n",
    "    5:{\n",
    "    'population':1000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3},\n",
    "    6:{\n",
    "    'population':1000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/8 > 0.3}\n",
    "}\n",
    "sc.run_experiment(sixGroupsLongRun, filename='SixGroupsLongRun',frames=200,reps=2)\n",
    "ani = sc.run_animation(sixGroupsLongRun, filename='SixGroupsLongRun',frames=200)\n",
    "ani"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "integrationist = {\n",
    "    1:{\n",
    "    'population':3000,\n",
    "    'ufunc': lambda t,agent : (t[0.5]-1) > 2 and t[1] > 1},\n",
    "    2:{\n",
    "    'population':3000,\n",
    "    'ufunc': lambda t,agent : (t[1]-1) > 2 and t[0.5] > 1}\n",
    "}\n",
    "sc.run_experiment(integrationist, filename='Integrationist',frames=100)\n",
    "ani = sc.run_animation(integrationist, filename='Integrationist',frames=100)\n",
    "ani"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "integrationistSparse = {\n",
    "    1:{\n",
    "    'population':2000,\n",
    "    'ufunc': lambda t,agent : (t[0.5]) > 2 and t[1] > 1},\n",
    "    2:{\n",
    "    'population':2000,\n",
    "    'ufunc': lambda t,agent : (t[1]) > 2 and t[0.5] > 1}\n",
    "}\n",
    "sc.run_experiment(integrationistSparse, filename='IntegrationistSparseVeryLong',frames=30000,reps=1)\n",
    "#ani = sc.run_animation(integrationistSparse, filename='IntegrationistSparse',frames=1000)\n",
    "#ani"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "integrationistWithEmpty = {\n",
    "    1:{\n",
    "    'population':3000,\n",
    "    'ufunc': lambda t,agent : (t[0.5]-1) > 2 and (sum(t.values())-t[0.5]) > 2},\n",
    "    2:{\n",
    "    'population':3000,\n",
    "    'ufunc': lambda t,agent : (t[1]-1) > 2 and (sum(t.values())-t[1]) > 2}\n",
    "}\n",
    "sc.run_experiment(integrationistWithEmpty, filename='IntegrationistWithEmpty',frames=100,reps=20)\n",
    "ani = sc.run_animation(integrationistWithEmpty, filename='IntegrationistWithEmpty',frames=100)\n",
    "ani"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "integrationistAsymmetric = {\n",
    "    1:{\n",
    "    'population':5000,\n",
    "    'ufunc': lambda t,agent : (t[0.5]) >= 2 and t[1] > 1},\n",
    "    2:{\n",
    "    'population':1000,\n",
    "    'ufunc': lambda t,agent : (t[1]) >= 2}\n",
    "}\n",
    "sc.run_experiment(integrationistAsymmetric, filename='IntegrationistAsymmetric',frames=100)\n",
    "ani = sc.run_animation(integrationistAsymmetric, filename='IntegrationistAsymmetric',frames=100)\n",
    "ani"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "fiveByNeighboorhoods = {\n",
    "    1:{\n",
    "    'population':3000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/24 > 0.3},\n",
    "    2:{\n",
    "    'population':3000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/24 > 0.3}\n",
    "}\n",
    "sc.run_experiment(fiveByNeighboorhoods, filename='FiveByNeighboorhoods',frames=100,nbrhd=5)\n",
    "ani = sc.run_animation(fiveByNeighboorhoods, filename='FiveByNeighboorhoods',frames=100,nbrhd=5)\n",
    "ani"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "sevenByNeighboorhoods = {\n",
    "    1:{\n",
    "    'population':3000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/48 > 0.3},\n",
    "    2:{\n",
    "    'population':3000,\n",
    "    'ufunc': lambda t,agent : (t[agent.color]-1)/48 > 0.3}\n",
    "}\n",
    "sc.run_experiment(sevenByNeighboorhoods, filename='SevenByNeighboorhoods',frames=100,nbrhd=7)\n",
    "ani = sc.run_animation(sevenByNeighboorhoods, filename='SevenByNeighboorhoods',frames=100,nbrhd=7)\n",
    "ani"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import scipy.stats as stats\n",
    "\n",
    "def binomAt3():\n",
    "    n = stats.binom.rvs(6,0.5,1)\n",
    "    return lambda t,agent : (t[agent.color]) > n\n",
    "utilityFunc = binomAt3\n",
    "\n",
    "binomSym3 = {\n",
    "    1:{\n",
    "    'population':3000,\n",
    "    'ufunc': utilityFunc()},\n",
    "    2:{\n",
    "    'population':3000,\n",
    "    'ufunc': utilityFunc()}\n",
    "}\n",
    "sc.run_experiment(binomSym3, filename='BinomSym3',frames=100)\n",
    "ani = sc.run_animation(binomSym3, filename='BinomSym3',frames=100)\n",
    "ani"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import scipy.stats as stats\n",
    "\n",
    "def binomAt4():\n",
    "    n = stats.binom.rvs(8,0.5,1)\n",
    "    return lambda t,agent : (t[agent.color]) > n\n",
    "utilityFunc = binomAt4\n",
    "\n",
    "binomSym4 = {\n",
    "    1:{\n",
    "    'population':3000,\n",
    "    'ufunc': utilityFunc()},\n",
    "    2:{\n",
    "    'population':3000,\n",
    "    'ufunc': utilityFunc()}\n",
    "}\n",
    "sc.run_experiment(binomSym4, filename='BinomSym4',frames=100)\n",
    "ani = sc.run_animation(binomSym4, filename='BinomSym4',frames=100)\n",
    "ani"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import scipy.stats as stats\n",
    "\n",
    "def binomAt4():\n",
    "    n = stats.binom.rvs(8,0.5,1)\n",
    "    return lambda t,agent : (t[agent.color]) > n\n",
    "utilityFunc = binomAt4\n",
    "\n",
    "binomSym4LongRun = {\n",
    "    1:{\n",
    "    'population':3000,\n",
    "    'ufunc': utilityFunc()},\n",
    "    2:{\n",
    "    'population':3000,\n",
    "    'ufunc': utilityFunc()}\n",
    "}\n",
    "sc.run_experiment(binomSym4LongRun, filename='BinomSym4LongRun',frames=200)\n",
    "ani = sc.run_animation(binomSym4LongRun, filename='BinomSym4LongRun',frames=200)\n",
    "ani"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "baseAt4 = {\n",
    "    1:{\n",
    "    'population':3000,\n",
    "    'ufunc': lambda t,agent : t[agent.color] > 4},\n",
    "    2:{\n",
    "    'population':3000,\n",
    "    'ufunc': lambda t,agent : t[agent.color] > 4}\n",
    "}\n",
    "sc.run_experiment(baseAt4, filename='BaseAt4',frames=100)\n",
    "ani = sc.run_animation(baseAt4, filename='BaseAt4',frames=100)\n",
    "ani"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import scipy.stats as stats\n",
    "\n",
    "def uniformAt3():\n",
    "    n = stats.randint.rvs(0,6,1)\n",
    "    return lambda t,agent : (t[agent.color]) > n\n",
    "utilityFunc = uniformAt3\n",
    "\n",
    "uniform0to6 = {\n",
    "    1:{\n",
    "    'population':3000,\n",
    "    'ufunc': utilityFunc()},\n",
    "    2:{\n",
    "    'population':3000,\n",
    "    'ufunc': utilityFunc()}\n",
    "}\n",
    "sc.run_experiment(uniform0to6, filename='uniform0to6',frames=100,reps=10)\n",
    "ani = sc.run_animation(uniform0to6, filename='uniform0to6',frames=100)\n",
    "ani"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import scipy.stats as stats\n",
    "\n",
    "def bimodal3():\n",
    "    n = stats.binom.rvs(3,0.5,1) + (stats.randint.rvs(0,2,1)-1)*4\n",
    "    return lambda t,agent : (t[agent.color]) > n\n",
    "utilityFunc = bimodal3\n",
    "\n",
    "bimodal3and6 = {\n",
    "    1:{\n",
    "    'population':3000,\n",
    "    'ufunc': utilityFunc()},\n",
    "    2:{\n",
    "    'population':3000,\n",
    "    'ufunc': utilityFunc()}\n",
    "}\n",
    "sc.run_experiment(bimodal3and6, filename='Bimodal3and6',frames=100)\n",
    "ani = sc.run_animation(bimodal3and6, filename='Bimodal3and6',frames=100)\n",
    "ani"
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
   "version": "3.9.6"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
