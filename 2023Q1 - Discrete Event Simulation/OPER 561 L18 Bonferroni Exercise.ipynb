{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "fa739e98",
   "metadata": {},
   "source": [
    "# Bonferroni Exercise \n",
    "\n",
    "Consider a case where we are performing validation of an agent-based model examining the hunt for U-Boats in the Bay of Biscay during WWII. The output from the model is contained in the code cells below.\n",
    "\n",
    "There are 2 metrics of interest: U-Boats sighted and U-Boats killed. The model was run under 2 separate scenarios to capture the ability of the model to represent the technological innovations employed by the Axis and Allied powers during this campaign. Each scenario was replicated 20 times. \n",
    "\n",
    "-----------------------"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fd755755",
   "metadata": {},
   "source": [
    "_(Select a cell by clicking it, then use Ctrl+Enter or Shift+Enter to run that cell. You can also use the Run button in the toolbar.)_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ba3c058d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from io import StringIO\n",
    "from scipy import stats"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "67b30a98",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Replication</th>\n",
       "      <th>Scenario 1 Kills</th>\n",
       "      <th>Scenario 1 Sightings</th>\n",
       "      <th>Scenario 2 Kills</th>\n",
       "      <th>Scenario 2 Sightings</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>108</td>\n",
       "      <td>28</td>\n",
       "      <td>287</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>129</td>\n",
       "      <td>26</td>\n",
       "      <td>332</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>129</td>\n",
       "      <td>28</td>\n",
       "      <td>304</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>150</td>\n",
       "      <td>30</td>\n",
       "      <td>318</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "      <td>128</td>\n",
       "      <td>28</td>\n",
       "      <td>345</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Replication  Scenario 1 Kills  Scenario 1 Sightings  Scenario 2 Kills  \\\n",
       "0            1                 2                   108                28   \n",
       "1            2                 5                   129                26   \n",
       "2            3                 3                   129                28   \n",
       "3            4                 3                   150                30   \n",
       "4            5                 4                   128                28   \n",
       "\n",
       "   Scenario 2 Sightings  \n",
       "0                   287  \n",
       "1                   332  \n",
       "2                   304  \n",
       "3                   318  \n",
       "4                   345  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "csv_data = \"\"\"Replication,Scenario 1 Kills,Scenario 1 Sightings,Scenario 2 Kills,Scenario 2 Sightings\n",
    "1,2,108,28,287\n",
    "2,5,129,26,332\n",
    "3,3,129,28,304\n",
    "4,3,150,30,318\n",
    "5,4,128,28,345\n",
    "6,2,143,38,358\n",
    "7,3,147,39,341\n",
    "8,3,130,43,347\n",
    "9,5,184,28,357\n",
    "10,5,168,37,373\n",
    "11,4,102,34,312\n",
    "12,3,159,37,334\n",
    "13,2,107,25,282\n",
    "14,2,116,27,288\n",
    "15,4,131,31,334\n",
    "16,4,120,37,343\n",
    "17,3,120,29,357\n",
    "18,4,149,30,376\n",
    "19,5,156,34,344\n",
    "20,4,130,32,338\n",
    "\"\"\"\n",
    "\n",
    "csv_StringIO = StringIO(csv_data)\n",
    "df = pd.read_csv(csv_StringIO)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c076e9a6",
   "metadata": {},
   "source": [
    "___________\n",
    "\n",
    "__Task:__ Brainstorm methods for validating the model, with an emphasis on statistical tests. Write your thoughts in the cell below. Indicate any additional data you might need."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "fd69c65c",
   "metadata": {},
   "source": [
    "Conducting a t-test to determine the probability of the two scenarios having statistically significant differences in thier results.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "973a1d1a",
   "metadata": {},
   "source": [
    "----------------\n",
    "\n",
    "<div style=\"height:350px\">&nbsp</div>\n",
    "\n",
    "For this activity, we will validate the model via confidence intervals based on the t-test, using the $\\alpha = 0.1$ level of significance. We'll need reference values to validate against. See the \"True Values\" below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4d9501ac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Scenario 1 Kills</th>\n",
       "      <th>Scenario 1 Sightings</th>\n",
       "      <th>Scenario 2 Kills</th>\n",
       "      <th>Scenario 2 Sightings</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>True Values</th>\n",
       "      <td>3</td>\n",
       "      <td>135</td>\n",
       "      <td>32</td>\n",
       "      <td>319</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Scenario 1 Kills  Scenario 1 Sightings  Scenario 2 Kills  \\\n",
       "True Values                 3                   135                32   \n",
       "\n",
       "             Scenario 2 Sightings  \n",
       "True Values                   319  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "true_df = pd.DataFrame([[3, 135, 32, 319]], \n",
    "                       columns=['Scenario 1 Kills', 'Scenario 1 Sightings', 'Scenario 2 Kills', 'Scenario 2 Sightings'], \n",
    "                       index=['True Values'])\n",
    "true_df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "11254083",
   "metadata": {},
   "source": [
    "Recall the equation for a confidence interval:\n",
    "\n",
    "$\\bar{Y} \\pm t_{\\alpha/2,n-1}\\frac{S}{\\sqrt{n}}$\n",
    "\n",
    "Defining some terms we need for our confidence intervals..."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "bf503f4b",
   "metadata": {},
   "outputs": [],
   "source": [
    "alpha = 0.10\n",
    "R = 20  # number of replications (a.k.a. `n`)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "6aeba24a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.729132811521367\n"
     ]
    }
   ],
   "source": [
    "tcrit = stats.t.ppf(1 - alpha/2, R-1)  # equivalent to Excel's =T.INV.2T(alpha, R-1)\n",
    "\n",
    "print(tcrit)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "54c998fa",
   "metadata": {},
   "source": [
    "And we could start calculating the confidence intervals one at a time.\n",
    "\n",
    "To help stay organized and consistent, we can use a function to build confidence intervals, one column of data at a time."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "05317a04",
   "metadata": {},
   "outputs": [],
   "source": [
    "from math import sqrt\n",
    "\n",
    "def build_confidence_interval(data, alpha):\n",
    "    \"\"\"Returns the (lower, upper) bounds of a 100*(1-alpha)% confidence interval, based on the t-test, and the half-width.\n",
    "    \n",
    "    Args:\n",
    "      data (pd.Series) - the input data as a specific column from a dataframe\n",
    "      alpha (float) - level of significance between 0 and 1\n",
    "      \n",
    "    Returns: lower bound, upper bound, interval half-width\n",
    "      \n",
    "    \"\"\"\n",
    "    R = len(data)\n",
    "    tcrit = stats.t.ppf(1 - alpha/2, R-1)\n",
    "    \n",
    "    Y_bar = data.mean()\n",
    "    S = data.std()  # this function the sample st.dev by default\n",
    "    \n",
    "    H = tcrit * S / sqrt(R)\n",
    "    \n",
    "    lower, upper = Y_bar - H, Y_bar + H\n",
    "    \n",
    "    return lower, upper, H    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e2ed1b4d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3.0935134304106535, 3.9064865695893465, 0.4064865695893465)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "build_confidence_interval(df['Scenario 1 Kills'], alpha)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dd96b5c0",
   "metadata": {},
   "source": [
    "__Task:__ Construct confidence intervals for the remaining features of the data.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ab01fb67",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(127.01012237019306, 143.58987762980698, 8.289877629806956)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "build_confidence_interval(df['Scenario 1 Sightings'], alpha)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "4e06c65e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(30.104700307483252, 33.995299692516745, 1.945299692516746)"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "build_confidence_interval(df['Scenario 2 Kills'], alpha)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a8608f9a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(322.95855776711164, 344.04144223288836, 10.541442232888329)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "build_confidence_interval(df['Scenario 2 Sightings'], alpha)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "05a81901",
   "metadata": {},
   "source": [
    "__Task:__ What do we think about the model and its validity? At what total confidence are we making that decision?"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "4393d0a8",
   "metadata": {},
   "source": [
    "Scenerio 2 sightings and Scenario 2 kills fall jsut outside the coreesponding confidence intervals.\n",
    "The overall confidence is 60%."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9a55c989",
   "metadata": {},
   "source": [
    "----------------\n",
    "\n",
    "<div style=\"height:250px\">&nbsp</div>\n",
    "\n",
    "Recall our friend Bonferroni _(BCNN Eq. 12.16, p. 476)_. In order to make our model validity determination at the desired 90% confidence level, we need to change some things."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "390e1303",
   "metadata": {},
   "source": [
    "__Task:__ Construct joint confidence intervals on all four data features."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b587dbae",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "135a4591",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6e47429",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ec46478",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f55a4a6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "1ab6fce3",
   "metadata": {},
   "source": [
    "__Task:__ Now, what do we think about the model and its validity? At what total confidence are we making that decision?\n",
    "\n",
    "How does your interpretation of these results differ from the initial (non-Bonferroni) results?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c87dc34a",
   "metadata": {},
   "source": [
    "_your thoughts here (double click the cell to start editing)_\n"
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
  "vscode": {
   "interpreter": {
    "hash": "aee8b7b246df8f9039afb4144a1f6fd8d2ca17a180786b69acc140d282b71a49"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
