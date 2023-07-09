{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Implementation in Python:\n",
    "\n",
    "####  Import Data\n",
    "Let us use Pandas to examine a useful, albiet trivial, data set."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
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
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "      <th>4</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>145</th>\n",
       "      <td>6.7</td>\n",
       "      <td>3.0</td>\n",
       "      <td>5.2</td>\n",
       "      <td>2.3</td>\n",
       "      <td>Iris-virginica</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>146</th>\n",
       "      <td>6.3</td>\n",
       "      <td>2.5</td>\n",
       "      <td>5.0</td>\n",
       "      <td>1.9</td>\n",
       "      <td>Iris-virginica</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>147</th>\n",
       "      <td>6.5</td>\n",
       "      <td>3.0</td>\n",
       "      <td>5.2</td>\n",
       "      <td>2.0</td>\n",
       "      <td>Iris-virginica</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>148</th>\n",
       "      <td>6.2</td>\n",
       "      <td>3.4</td>\n",
       "      <td>5.4</td>\n",
       "      <td>2.3</td>\n",
       "      <td>Iris-virginica</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>149</th>\n",
       "      <td>5.9</td>\n",
       "      <td>3.0</td>\n",
       "      <td>5.1</td>\n",
       "      <td>1.8</td>\n",
       "      <td>Iris-virginica</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       0    1    2    3               4\n",
       "145  6.7  3.0  5.2  2.3  Iris-virginica\n",
       "146  6.3  2.5  5.0  1.9  Iris-virginica\n",
       "147  6.5  3.0  5.2  2.0  Iris-virginica\n",
       "148  6.2  3.4  5.4  2.3  Iris-virginica\n",
       "149  5.9  3.0  5.1  1.8  Iris-virginica"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv('https://archive.ics.uci.edu/ml/'\n",
    "        'machine-learning-databases/iris/iris.data', header=None)\n",
    "df.tail()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This data set contains the measurements of 150 Iris flowers belonging to three species. It is a <b> labeled </b> data set which means that in addition to the measurements, each sample is labeled with the actual the species name as well.  Such labeled datasets are essential for supervised machine learning tasks.  Each measurement (column) is called a <b> feature </b>.  The dataset then has the following features  [Sepal length, Sepal width, Petal length, Petal width, and class label] According to our prior vector notation an individual flower would be a 5 dimensional vector $x^{(j)}$, where the \"3rd\" feature (labeled 2 above due to Pythons 'lovely' zero indexing!) would be $x_3$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "For actual implementation we will import the data set using NumPy, and we will only use Pedal Length and Pedal Width (columns 2 and 3) to enable easy visualization (IRL classification can be done on many features simulatanously, but obviously cannot be graphed in 2D)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Class labels: [0 1 2]\n"
     ]
    }
   ],
   "source": [
    "from sklearn import datasets\n",
    "import numpy as np\n",
    "\n",
    "iris = datasets.load_iris()\n",
    "X = iris.data[:, [2, 3]]\n",
    "y = iris.target\n",
    "\n",
    "print('Class labels:', np.unique(y))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Split Data\n",
    "Let us split the data into a training set and a test set.<br>\n",
    "Notes: <br>\n",
    "1) 'test_size =.2'-- We can choose the size of the test set via this user defined parameter, we choose 20% <br>\n",
    "2) 'random_state=1' -- The training data set is shuffled prior to be used, else we would bias our training against class 2  samples since they are bottom of the list.  This fixed random seed allows us to reproduce results.<br>\n",
    "3) 'stratify=y' -- This splits both the training and test data sets such that they proportionally mirror the class labels percentages from original data set. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "####  Feature Scaling \n",
    "We saw in class that Gradient Descent algorithms (https://en.wikipedia.org/wiki/Gradient_descent) behave very badly when the sublevel sets for the convex function are highly elliptical (equivilently data is poorly conditioned).  For some datasets it is easy to scale the features to precondition the data and enable faster gradient descent.  This is typically done by standardizing the data using the estimators $\\hat{\\mu_i}$ and $\\hat{\\sigma_i}$ for each feature $i$. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler \n",
    "\n",
    "sc = StandardScaler() #assign the standardscaler class to the variable sc for ease of use\n",
    "sc.fit(X_train) # The StandardScaler fit function finds the mean and standard deviation for us to allow fitting\n",
    "\n",
    "# here we transform the data and rename transformed data\n",
    "X_train_std = sc.transform(X_train) \n",
    "X_test_std = sc.transform(X_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Training our Perceptron\n",
    "We are now going to leverage the built in tools in the SciKit-Learn API to train, test and display the behavior of our Adaline perceptron.  For extensive details on all options for this class see: <br>\n",
    "https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html\n",
    "<br>\n",
    "<br>\n",
    "<b>First </b> we train (i.e fit our perceptron) on the standardized training data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Perceptron(eta0=0.1, max_iter=40, random_state=1)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import Perceptron\n",
    "\n",
    "ppn = Perceptron(max_iter=40, eta0=0.1, random_state=1)\n",
    "ppn.fit(X_train_std, y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Evaluating our Percepton\n",
    "\n",
    "Now that we have trained our percepton we want to test how it is performing.  There are multiple ways of doing this.  We will show a few different. <br>\n",
    "<b> First: </b> We will look at the number of misclassified samples.  This is perhaps not the most informative however as 3 misslcassified  out of 5 test samples is quite different meaning then 3 missclaissfied out of 5,000 test samples.  So, <br>\n",
    "<b> Second: </b> We will use a generic Sci-Kit Learn built in tool to output the accuracy percentage. <br>\n",
    "<b> Third: </b> We will use the perceptron classifier built in tool to outout accuracy percentage <br>\n",
    "<b> Fourth: </b> We will look at the resulting scatter plot map of points and the linear seperator to see why we are not getting good classification."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Misclassified samples: 1\n"
     ]
    }
   ],
   "source": [
    "# First Look at the number of misclassified samples\n",
    "\n",
    "y_pred = ppn.predict(X_test_std)\n",
    "print('Misclassified samples: %d' % (y_test != y_pred).sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Generic Accuracy: 0.98\n",
      "Perceptron Accuracy: 0.98\n"
     ]
    }
   ],
   "source": [
    "#Second: Sklearn has a built in metrics module we could use for any classifier which compares test output vs predicted output \n",
    "from sklearn.metrics import accuracy_score\n",
    "print('Generic Accuracy: %.2f' % accuracy_score(y_test, y_pred))\n",
    "\n",
    "#Third:  Every sklearn classifier also has a built in score method for outputing accuracy\n",
    "print('Perceptron Accuracy: %.2f' % ppn.score(X_test_std, y_test))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<b> Visualize output </b>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib.colors import ListedColormap\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):\n",
    "\n",
    "    # setup marker generator and color map\n",
    "    markers = ('s', '^', 'o', '^', 'v')\n",
    "    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')\n",
    "    cmap = ListedColormap(colors[:len(np.unique(y))])\n",
    "\n",
    "    # plot the decision surface\n",
    "    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1\n",
    "    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1\n",
    "    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),\n",
    "                           np.arange(x2_min, x2_max, resolution))\n",
    "    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)\n",
    "    Z = Z.reshape(xx1.shape)\n",
    "    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)\n",
    "    plt.xlim(xx1.min(), xx1.max())\n",
    "    plt.ylim(xx2.min(), xx2.max())\n",
    "\n",
    "    for idx, cl in enumerate(np.unique(y)):\n",
    "        plt.scatter(x=X[y == cl, 0], \n",
    "                    y=X[y == cl, 1],\n",
    "                    alpha=0.8, \n",
    "                    c=colors[idx],\n",
    "                    marker=markers[idx], \n",
    "                    label=cl, \n",
    "                    edgecolor='black')\n",
    "        \n",
    "\n",
    "    # highlight test samples\n",
    "    if test_idx:\n",
    "        # plot all samples\n",
    "        X_test, y_test = X[test_idx, :], y[test_idx]\n",
    "\n",
    "        for idx, cl in enumerate(np.unique(y_test)):\n",
    "            plt.scatter(X_test[y_test == cl, 0],\n",
    "                        X_test[y_test == cl, 1],\n",
    "                        c=colors[idx],\n",
    "                        edgecolor='black',\n",
    "                        alpha=1.0,\n",
    "                        linewidth=1,\n",
    "                        marker='o',\n",
    "                        s=100, \n",
    "                        label='test set')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAagAAAEYCAYAAAAJeGK1AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAABNQklEQVR4nO3deVhV5fbA8e9iEEEUFTQxnDIbLM3UnC31lkOmWWmDmVqZaVb3WqbWr1EbTE1vpjk3aWRp5tDg0DVScyA1U69m5oDzzRFEFAHf3x/7HATkDMA5nAOsz/OcR87e++z9Quni3Xu9a4kxBqWUUsrfBPh6AEoppVRuNEAppZTySxqglFJK+SUNUEoppfySBiillFJ+KcjXA8iLqHLlTM0rrvD1MDzuyOl0JAIqRIT7eihKKVXotm3adtwYUynn9iIVoGpecQUbxo3z9TC84p1dfxNYLZ2KN1WjXc3rfD0cpZQqNLVDaifktl1v8fmJF+tU5voJpzn5+wHm/bCSo+lHfT0kpZTyKQ1QfqTL0LoMLV2V1G8DWf3dVuZt/MPXQ1JKKZ/RAOWHXulanqHzVsDBA8xbuFxnU0qpEqlIPYPKTVpAAAcjIzkfHOzroXjW0KF0AU6fu4hsN/wddJoypfL+PQaEBBASHUJAkP4uopQqWop8gDoYGUnZ6GhqliuHiPh6ON5x9ixHQ0sBEBpRitJS2q2PGWM4dfIUJ4+cJLRaqDdHqJRSHlfkf60+HxxMZHEOTgBlylAlIJiMw4GcS7xA0oXzbn1MRKhQsQIXUy96eYBKKeV5RT5AAcU7OGVxZUwAGYcDyTif5vZnSsrPRilV/BSLAFWSXBkTgDlvOHU6ye2ZlFJKFUUaoDxkyY8/cu0tt3B1w4aMGj/eq9eKLh1M6b/TyUi5wKmkM6QZ92dUSilVVGiA8oCMjAwGvfACP8ydy/Z16/ji66/Z/od31zCVrxJKlYBgLp4WkhPPcSpFZ1NKqeKlyGfx5UW7du1IOnbssu3lKlVixYoV+T5v/MaNXH3VVVxVsyYAD957Lwu//56613m/ZFHV8oFw4jRHK5Tj1IULhEeEEizFLOVeKVUilagAlXTsGBuioi7b3jiXoJUXh44codqVV2a+j6lalfUbNxbonHkSGUkV4PDpDJI5B6UyqBDmXiq6Ukr5K73F5wHGmMu2+SJ7rmr5QKqcSoILFzh1OonzRm/7KaWKrhI1g/KWmKpVOXDoUOb7g4cPU7VKFd8MxjabOnTwIue4wLnADN+MQymlCkhnUB5wS8OG7Nq9m70JCVy4cIE58+fTtVMnn47pypgAazZldJGuUqpo0gDlAUFBQUwcPZoO993H9U2bcn+3btxw/fW+HhZERmLOG86mnGPFPq2MrpQqWkrULb5ylSrlmhBRrtJljRzz7M727bmzffsCn8fToksHc/jMRU7uPcC8HX/TvdOtvh6SUkq5pUQFqIKkkhdlYeWCGZpclZGLTjPvwnKIqUb3Rtq1Vynl3/QWXwmifaaUUkWJBqiSplcvq2vvsjDt2quU8msaoEqonLOpP1I1UCml/IsGqJLMNps681ok25YcYF5cvK9HpJRSmTRAKUa+G8LQLQchMVFnU0opv6EBygMee/ppKtepw43Nm/t6KPnXpMml2dQ2Xw9GKaU0QHlE34ceYsm8eb4ehkc0idxtPZf6YaWvh6KUKuFKZIA6fuIEne/vzYmTJz1yvltbtqRihQoeOZevdRla18ry+zaQeQuXawUKpZTPlMgANf3TOazfeIZpn3zh66H4LXuW38nfrdmUrplSShU2nwUoEakmIj+JyA4R+a+I/LMwrnv8xAk+/WIZVSpP5NMvlnlsFlUs2ddMfRuoa6aUUoXOlzOodOB5Y8z1QDNgkIjU9fZFp386h7T0uyhd+lrS0u/SWZQbtAKFUsoXfBagjDFHjDGbbF+fAXYAVzr/VMHYZ09lwx8BoGz4IzqLcleWNVOrv9uqa6aUUl7nF8+gRKQmcDOw3pvXsc+egoKstu9BQVEemUU99PjjNG/fnp1//UXMDTcwc9YsTwzXL+maKaVUYfF5NXMRCQe+Bv5ljEnKZX9/oD9A9QK2xVge9wvp6Uc5dvyLHNur8OJzg/J93i9mzizQuIqcJk0YCrwyLJVtHGBbRBLd2zTx9aiUUsWMTwOUiARjBafPjTHzczvGGDMNmAbQuE4dU5DrrVgUW5CPqxxGvhsC8Qd5p0IQK2r+Qbua2sJDKeU5vsziE2AmsMMYM85X41AF1KQJKTMiOPn7AV0zpZTyKF8+g2oJPAK0E5HNttedPhyPyqeR74bomimllMf57BafMWY1IL66vvKwXr0YCoxcdJrVF7ZCzGnt2quUKhC/yOJTxYeumVJKeYoGKOV5OddMaQUKpVQ+aIDygAMHD9K2Sxeub9qUG5o35/0pU3w9JL+QuWZKu/YqpfJBA5QHBAUF8d6bb7Jj/XrWLVvGpBkz2P6H/mMMZO8zpV17VT4k7E5gxJARNI5pTJ3QOjSOacyIISNI2J3g66EpLytxAWrJjz/Spe9D1PtHS7r0fYglP/5Y4HNGV6lCw5tuAqBs2bJcf801HDpypMDnLU7ss6mMbWc1SCm3xS2Jo1vrbhwOOsygJYMYc3QMg5YM4nDQYbq17kbckjhfD1F5kc8rSRSmJT/+yMiZ73HnC514oN6DJGxNYOSY9wDoePvtHrnGvv37+W3LFpo2auSR8xUrTZrw4uzZjK7WjhX7dGGvci5hdwKDHxvMo58/Sq0mtTK3R9WKovMrnanboS6DHx7MglULqFG7RrbP/rzsZ2I/juVgwkFiasRQ76Z6bP19a+b7no/25Lb2txX2t6TyqETNoCbNnsmdL3TiqpuvIjAokKtuvoo7X+jEpNmeKVWUnJzMfb178+933qFcuXIeOWex06sX1084rWumlEufTv6Upr2bZgtOWdVqUoumjzTl0ymfZtv+87KfmfLhFFo804IhS4fQ4NEGzF8wn8pNKzNk6RBaPNOCKR9O4edlPxfGt6EKoEQFqH0H9lOjXvbftGrUq8G+A/sLfO60tDTu69OHh3v04N4uXQp8vuIsa9dezfJTjiyas4imvZo6PabpI01ZNGdRtm2xH8fScWhHat1ci8CgQMKvDKfbm93YuXYngUGB1Lq5Fh2HdiT2Yy195u9KVICqWa06CVuzP1hN2JpAzWrVC3ReYwyPP/MM119zDc8Nyn/R2ZJG10wpZxJPJFKhWgWnx1SIqUDiicRs2w4mHKR6vUt/py9cuEDNxjU5sf9E5rbq9apzMOGgZwesPK5EBahBvR7n+zE/sOe3PWSkZ7Dntz18P+YHBvV6vEDn/WXdOmZ9+SUrVq6kQevWNGjdmu+XLfPQqIs5e9feZWE6m1LZRERGcOrAKafHnDp4iojIiGzbYmrEsH/rpbsipUqVYt+GfURWj8zctn/rfmJqxHh2wMrjSlSShD0RYtKEmcw58CU1q1XnlcefL3CCRKvmzTGnnP9FUs690rU8zP6W0d3bMe/gAW7sWI3rQjSJoiTr+mBX1s9eT+dXOjs8Zv2s9XR9sGu2bT0f7cmU0VPoOLQj1etVJ/lQMgteXUDLB1uSkZ7B/q37WTJ6CQOeGuDtb0EVUIkKUGAFKU9l7CkPs9Xz0z5TRU/OrLmCZslNHDWRpd8u5eT/TlK3Q91cEyX2xu9l/az1LFi1INt2+3VjP4jlq4SviKkRw73d7mXr+q2M/WosMTViGPDUAM3iKwJKXIBS/s/eZ2p0fZi3cLnOpvycPWvOPmPZv3U/U0Zb1VTyEwQmjprI/AXzeWDiA5xLPMf0h6bT9OGmtHy0JRViKnDq4CnWz1rP+lnrGf/R+MtSzO3X1QBU9GmAUv4pR9fewzeh66b8VNasOeBSltwHsfkKEnNj53LfuPu4uvnVAAz5cQiL31zM6NajSU9NJyIygq4Pds11/ZMqXkpUkoQqeka+G8KZ1yI5ueNvXw9FOZAzaw4KliWXnJRMzcY1M99XqlWJ3lN6ExYRxq6UXWw4sIFXx7yqwakE0BmU8nsj3w1h5KJzzLuwHGKqaZ8pP1MxsiLTB05ne9x2kk8kEx4ZTt02dakYWTHX4xN2J/Dp5E9ZNGcRiScSM2dEfQb2oUbtGoSXC2ffhn2ZM6hje4+x+M3FpCSmUCe0zmXHq+LL4QxKRBq68apXmINVJZeumfJPcUvi2BK/hTJVyvDPJf9k7NGx/HPJPylTpQxb4rdcVivPndp6PXr2YMHLC/hr7V9sXbKVsbePpfyV5Rm6aqjW4ithxBiT+w6RM8CvOO96W8sYU9ML48pV4zp1zIZx47Jt21G1KtfXru3W53fv3cvEiROJnTuX48nJRIWH07NHD55++mlq18q9nIorpxMTiZ07l6f69cvX5/89eTL9+/QhLCwsX5+3i1u9mlLBwbRoevnK+x27d3P94cMFOr8/GbnoNCHtU3Q25WMJuxPo1rrbZbXy7PbG72XKfVNo1LIRTVs2Zf0v69n4y0YGfD3A4fEfP/wxC1YtYPHcxXzxyRec/N9JBs4f6PL4fbv3Oc0i9HSWYV748tpFRe2Q2huNMY1zbnd2i+9XY0w7ZycVkRUFHlkh+WH5cnr37csTaWmsSUujBpBw5gwzZ82i2Zw5fPbJJ3S64448n/d0YiIfzpxZoADV6/77PRKgwsuUyTVAFTe6Zso/uFMrr1W/VpxOOM38BfMJLRtK6ydau1Vb79Uxr3Ly+EkOBx12efw7L71DYmqiwyxCT2cZ5oUvr10cOLzF5yo4uXuMP9i9dy+9+/ZlUUoKb6elURsrMtcG3k5LY1FKCr379mX33r15Pvfw119n9759NGjdmhdeeQWAMRMmcEu7dtRv2ZLX3nkHgLNnz9L5/vu5qVUrbmzenC/nz2fC1KkcPnqUtl260DaX+n3DX3+dus2aUb9lS4bYzn3s+HHu692bW9q145Z27fhl3Tr27d/PlI8/ZvzkyTRo3ZpVa9bk90dVdGTp2qt9pnzDnVp5zXs3Z+fqnXR7sxt7N+2l2SPNnB6ftbaeu7X4Vv9ndbbaezlr7eWszVeYtfh8ee3iwOEMSkQaOvugMWaT54fjHRMnTuSJtDSaO9jfHOiXlsakSZMYN3Zsns496vXX2bZjB5tXrQJg2YoV7Nqzh/j//AdjDF0feoiVv/zCsRMnqBodzXdffQVAYmIiERERjJs0iZ8WLyYqMjLbeU+eOsU3333HH/HxiAinE616Y/8cPpzBAwfSqnlz9h84QIfu3dmxfj0DHn2U8DJlGPLMM3kaf1Gna6Z8x91aeSmnUqjZuCYXzl7IU209d89//uz5XLMIv0qw/q45yjK07/cmX167OHCWZv6e7TUJWA9MA6bbvp7g/aF5TuzcuTyelub0mH5pacR+VfD/aZb99BPLVqzg5ltvpeFtt/HHrl3s2rOHenXr8mNcHMNee41Va9YQERHh9DzlypaldEgI/Z59lvmLFxMWGgrAjz//zNNDh9KgdWu69uxJ0pkznDlzpsDjLtK0a69PuFsrL6xCGPs27KNUmVJ5qq3n7vlLlymdrfYeZK+1l7M2X8793uTLaxcHzm7xtTXGtAUSgIbGmMbGmEbAzcBfhTVATzienIyrZNTqtuMKyhjDi4MHs3nVKjavWsVfmzbx+COPcM3VV7MxLo56devy4ogRjBg92ul5goKCiP/Pf7ivSxcWfPcdHbt3B+DixYusXbYs8/yHtm+nbNmyBR53cZCta+/C5fyRqoVnvcleK8+ZtZ+t5dpW17Lg5QXUaliLdbPWOT0+a209d86/ftZ6Wv2jFUtGL2Hvb3vJSM9g7297WTJ6CT0f7QlYtfmc7fcmX167OHBnoe51xpit9jfGmG1AA6+NyAuiwsNJcHHMfttxeVU2PJwzWQJbh3bt+Ojzz0m2bTt0+DB/HzvG4SNHCAsNpdcDDzDkmWfY9PvvuX7eLjk5mcSkJO5s355/v/MOm7da/wnat23LxOnTM4+zb3d0nhKnSRNerFOZ1GVhHD7i68EUb30G9mH9Z+vZG5/7s9u98XtZPWM1ISkh3NvtXiqWrsiq6aucHr9+1nr6DOjDz8t+ZtfOXaycttLp8Sunr+RsyllaNmvJmg/WMLbDWNZ8sCZbrb3b2t/GgKcGONxfUD8v+5knH3qSzi068+RDT2ZrhOjtaxd37izU3SEiM4DZgAF6ATu8OioP69mjBzNnzeJtJ7f5ZgQH0/P++/N87siKFWnZtCk3Nm9Op9tvZ8zIkez480+at28PQHh4OLOnTuWvPXt44dVXCQgIIDg4mMnvWa3m+/ftS6cePYi+4gp+Wrw487xnkpO5++GHOX/+PMYYxr/9NgAT3n2XQS+8QP2WLUnPyODW5s2ZMn48XTp2pHufPiz8/ns+ePddWrdokefvpTh5JelbRv/ejnm/H6BV53pUCari6yEVOzVq12D8R+MZ/PBgmj7SlKaPNL2sVt6HsR/SpmMbAJ7maeKWxDk9fvxH49m3e5+V+fZiR2753y251uL75eNfWP/5egbMHEDEFRGZ1ckd/cPvrdp87mTpaV3A/HO4DirzAJHSwEDgVtumlcBkY8x5L4/tMvldB7V7716atWrFopSUXBMl1gJdw8JYt3p1vtdD+bPitg4qL3TNlPcl7E7g0ym5VIYYkHulB1fHP/nQk7R4pkVmbb+/9/7N/Lfns2XJFlJTUgkJC6F+x/rc+9K9VK5VGYC9v+1lzQdrmPrF1EL93nOO1ZdjKcocrYNyGaAARCQUqG6M2emNwbmrIAt17eug+qWl0S8tjepYt/VmBAczIzg43+ugioKSHKAAmD2b0d2tFRE6m/J/nVt0ZsjSIQQGBWZuy0jPYGyHsXy35juX+/1prMo9jgKUy2dQItIV2Awssb1vICKLPD5CL+t0xx2sW72a1N69aVm2LKEitCxbltTevVm3enWxDU6KbGumVn+3VbP8/EzC7gRGDBlB45jG1Amtw76d+5g+cDp/771UINhZVt7fe/9m+sDp7Nu5jzqhdWgc05gRQ0aQsNvVk+eC0yw973InSeI1oAlwGsAYsxmo6bUReVHtWrUYN3YsR/fvJ/3kSY7u38+4sWOL5W09dTl7lh+JiZrl5ydyq8035OchlKlShjfavcHmJZudZuVtXrKZN9q9QZkqZRjy85BCr9WnWXre5c4zqPXGmKYi8psx5mbbti3GmPqFMsIsClqLr6Qq8bf4cvHKsFTKvnECIiK0a68P/LzsZ2Z8MMNlbb7J906m4hUVad6qOWfOnsmsZ1fvpnp5qu3n6arnWevrhZYOJSA4gLNnzmqtvXzKTy0+u20i0hMIFJE6wLNACailo4ozewWKdyoEMS9xORVvqqYNEQuJPfNNIsRlbb7WT7TmdMJpNm3bRMsHW/LgtAfZv3U/S0YvISIsglv73+p2bT9Pjz9r5t6S0UsY+vxQDUwe5s4tvmeAG4BUIBZIBP7lxTEpVThsa6aun3Cakyd8PZiSw16fbnvcdpe1+bLW8tu5dme2enarflzlVq0+e20/T9H6eoXHnQDVCHjVGHOL7fUyUNfL4/KK3Xv38tTzL1Gu+jUEVIykXPVreOr5l/JVJNbudGIiH86Yke/P/3vyZFJSUvL9ebu41atZs975qnuVuy5VN1l9pn5YqX2mCoG9Pl3yieQ81fI7sf/SbxHV61Un9Wxqnmr7eYqnOwgrx9wJUEuBFSJyRZZt+f8X2Ud+WL6c+q3aM2NWBGfOrMWYVM6cWcuMWRHUb9WeH5Yvz9d57e028uvfkyeTcu5cvj9vF7d6NWviNTstX2xZfqnfBlpZfhs1eSKrnFl2N0ffTJcWXWhYtWGuWXM5j8+53575Fh4ZnqdafpHVLxVU3r91PyFlQvJU289TNHOv8LgToHYCY4A4EbGXJ3DWxNDv7N67l+59nyIlZRFpae9AloYbaWnvkJKyiO59n9J2GyWcdu29XM4su8c+f4x0k06VllV4Ztkzl2XNffDWBy475toz3+q2qeuyNl/WWn7XNr82W6Zc69tbu1Wrz17bz1M0c6/wuJPFt8kY09CWIPEl8BHwmDHGaTsOb8hvFt9Tz7/EjFkRtuCUu+Dg4fTvfYaJY9/K05j27d/PXQ88wLa1awGr3ca8RYuYOn58ZruNoc8+y7ETJ1jyn/8w/f33gUvtNmrWr8+Gn37Ktd1G8/bts7XbKB8RQc9+/Xjq8ccva7fx+qhRDtttaBZf3mVm+ZXgChQ5O+Ye33uc8e3H0+/zfg6z5j6850N6TurJzd1uznV/1g647mTxZe3Iu/X3rdm60tasXdNlR9/8ZvG56oKrWXyeVZAsPgEwxuwSkdbAx0Chp5gXxOy580hLW+v0mLS0J5j1VYs8B6icsrbbAEg+e5Zde/bQunlzhrzyCsNee427OnRwWSsva7uNzu3bc1eHDoDVbmP7zksFPbTdhndk9pmCEtu1N2fH3FXTV9G8d3PnWXf9WrPv1325BqicWXW3tb/NZW2+rLX8cuOqFuD4j8bnKzi5W19PO+Z6l8tbfPa1T7avzxpj7geu8sTFReQjEflbRLZ54nyOJCefADcabljHFYy22yhGSnifqZwdbTd+vZFmvZxn3bXo24JNXzvuZZozq65NxzYsWLWAqherMqnTJF6o+gKTOk2i6sWqLFi1wGlw8sTnc5OXLD3N6PMuZx11hxpjRouIo+aEz3rg+p8AE4HPPHAuh8LDIzlzJgHr2ZMj+wkPj3SyP3e5tdt45e23ebhHD8LDwzl0+DDBwcGkp6dTsUIFej3wAOHh4XwSG5vt8zlv8SUnJ5Ny7hx3tm9Ps1tu4eqG1h1Ve7uNF561fvybt26lQb16lA0PJ0lnUl6Rc81USZlN5exoe/bEWbey5s6eOOt0f86suhq1a/DqmFfzvVapoJ/PKS9dcLVjrnc5m0HZW2psdPAqMGPMSuCkJ87lTK8e3QkOdp54GBw8nUfu757nc2dtt/HCK6/Qvl07enbvTvP27anXogXd+/blTHIyW7dvp8k//kGD1q156733eHnIEOBSu42cSRJnkpO568EHqd+yJbd17pyt3caGzZup37IldZs1Y8pHHwHQpWNHvvn2W02S8JYsa6ZKymwqZ0fbMpFl3MqaKxNZxun+oFJBhVYrLz/ykqWnGX3e5VY1c68OQKQm8K0x5kYH+/sD/QGqV6rUKCFHSre77Tbqt2pPSsoicNBwIyysK1tWLyuWdfk0ScLz3tn1N5Xuii7W1SdGDBnB4aDDdH6lMwDfvPQNwaHB3PXKXQ4/s+i1RWSkZ3DPW/fkun/xG4tJPp5MucrlWP+Z9YwoP7fhvMlRpYjc+k3l5VjlWJ6TJERkMVaDwlwZYzybu+n4OtOAaWBl8eXnHLVr1WLeJx/SvW9X0tIeJy3tCbA13AgOnk5w8EzmffJhsQxOyjtSZkRwstoB5p2g2Gb59RnYh26tu1G3Q93MskPj24/nhg43OMyaWzVjFT0n5Z5uvTd+L+tmr2PwssFE1Yqiboe6DH54sFdq5eXkKisvK/v22A9i+SrhK2JqxDgMOHk5VuWdwxmUiNh/wvcCVbA66gI8BOwzxrzkkQG4mEFlVdBisbv37mX8pBnM+moeycknCA+P5JH7uzN4UL9iHZx0BuUlJaDPVNySOAY/dilL7ujOo8QOiqXZw81o8WiL7B1uZ6/n1v63snL6yss64K6dtZZ1s9bx8IcPU/eOS4VovhvxHVUvVvVorbycdJbj//LdsFBEVhpjbnW1Lb8KM0CVVBqgvKu4d+3N2QE3uHQwkdUjSTqWRMqpFIJDg7n+9utp+WhLrmt9Hcf2HmPxm4vZtmQbGRcyKBNZhob3NaR1v9ZE1YrKdu7je48zqdMkNhzY4LXxa9db/5fvhoVAJRHJTCsXkVpAJU8MSkS+wOq4fq2IHBSRxz1xXqUKU84KFMWtz5Q9S27DgQ3sStlFretqMWLVCD746wNmnphJVK0oek3pRbnK5QCoVKsSvaf0Ju18GmOOjGHkHyO55617LgtO4J1aeTlp7byiy52Fuv/CKnO0x/a+JrakhYIyxjzkifMo5XO9ejEUqwLFNg6wLSKp2PSZStidwKeTL82gSoWVYvrA6dz70r1UrlWZsPJhzB4wm12rdpFyKoUykWWo06oOwSHBnDpwKtfAZJefWnk5xxMRGUHXB7vSZ2CfXJ9l2TPtss6gsmba5fV8qvA4nUGJSAAQAdQB/ml7XWuMWVYIY1OqyCluXXtddbxd8M4CDv5+kAoxFRi8bDBjj47lX0v+RfkryxMQGMB3I79zev681srLbTyuOug6q52Xn/OpwpOvZ1C+4okkifenTeHzr+dx+sRpykeW5+H7uvPP/gPynSRxOjGR2Llzeapfv3x9/t+TJ9O/Tx/CwsLy9Xm7uNWrKRUcTIuml/fH0WdQvlGUu/ZOHDWR2I9jOfX3KQbOH5hr1t5vC34jdlAsT33zlNOOuA9NfMhlbb7FcxczN3YuyUnJhJcL55Ymt2TroJvX2nv7du/LlrVX76Z6hVrLT+VNQZIkXgHOYRWKzVwibozx+gLbnAoSoH5YvpyeA5+gSe+mNOnVhArVKnDqwCniZ8cT/9l6YidPp9Mdd+R5TDmLxeaVo2KxeaXFYv3XO7v+JvDGMkUmSE0cNZH5C+ZToXoFompFcderua97+ualbwgsFUjX1x3PgBa/vpg1H6+h1eOtHNbK27Z5G/MXzKfbm92o2bgmP0/9mQ3zNnDPK/dwU9ubLnXQDYmAWmSuy8rNdyO+g32QmJroMmsv5zovR+fzdpahKliSxGPAIGAll6pIeC/lxgt2791Lz4FP0Ofzvtz5yp1E1YoiMCiQqFpR3PnKnfT5vC89Bz6h7TaUV7y4fpl1y6+I9JmaGzuXu0fezV+//OW04+3GrzfSoo/zosfN+zQnJCTEaa28ubFz6fZmN65ufjVBwUHs27iPe966hzJVy+Srg+7q/6x2qz5ezlqDjs7n6Y68yn0ukySMMUV+gdD706bQJEtV5pxqNalFk0eaMGH6VN5/e1Sezj3q9dfZtmMHm1etAqx2G7v27CH+P//JbLex8pdfOHbiBFWjo/nuK6tGl73dxrhJk/hp8eJc221889132dptAPxz+HAGDxx4WbuNAY8+6nAGpXysVy+G2tZMzTt4wO/XTCUnJVOtQTXOnnRee8/d2nxJp5Kc1spLTkqmZuOame9PHjhJjVtq8Peff2duy0sH3fNnz7tVHy9nrUFH5/N2lqFyzJ0ZFCJyo4jcLyK97S9vD8yTPv96Hk16Ob+90uSRpnz+9dwCXytru42Gt93GH7t2sWvPHurVrcuPcXEMe+01Vq1ZQ0SE88ylrO025i9eTFhoKGC123h66FAatG5N1549td1GUWHv2rssrNC79rrqcJtTmbJl2PvrPspUdF57z93afK6y9MLLhbNvw77M9xWrVSTh1wQCAi/985SXDrqly5R2qz5ezlqD+R2/8h6XAUpEXgM+sL3aAqOBQilz5CmnT5x26zel0x74TUnbbShnCnvNVH6y1GpWu5qFry6idos6TjveNrqvEWs+dX472Z0svR49e7Dg5QX8tfYv0tPSqdmoJt/83zecPXw2Xx10W/2jlVsdb7s+2NUnHXmV+9xZB9UduAn4zRjzqIhcATgvDe5nykeWd2s9Rvl8/Kak7TZUnhXSmqmE3QkMfmzwZVlqUbWi6PxKZ4e18C5mBJN44AKJR/9ix4//5YaOudfeq9mkJrGDYql3Zz2HWXDrZ61nwaoFTsf59PCnAZj7XPYsvh1f7GD5qOWZ9e3sWXf22oDOrrdv9z6X9fFy1hrM7/iV97iTxRdvjGkiIhuxZlBngG3GmBsKY4BZ5TeL79kXh7EzdB93vnKnw2O+H/Ed16VelednUAA9+/Vjy3//S6fbb2fMyJG8P2UKMz6zWlyFh4cze+pU/tqzhxdefZWAgACCg4OZ/N57NL75Zj6YNo1JM2YQfcUV/LR4ceY5jxw9yt0PP8z58+cxxjDkmWfo89BDHD9xgkEvvMCOnTtJz8jg1ubNmTJ+PH/+9Rfd+/QhICCAD959N1vHXs3i82Px8Yyub9168nSfKU9kqeWsxZc1C++Xj34hI60SgcHHaPlYS4dZep6sVu5sPPm5nqfPp/KnIGnmHwIvAQ8CzwPJwGZjzKPeGKgz+Q1Qu/fupfEdbenzeV+Hvyl9+vAnbFj+U7EsGqsByv95Y81U45jGDFoyyOmdA3dq4eWsxRcRGUGHuzuwevkuQsM+5lzKo7RqX4elC5Zmr8QwwDuVGHIbT0Gu5+nzqbzLd4DKdrBV2LWcMWaLB8fmNo+sg3qkCU2y/KYUP2s98bPi870OqijQAFVExMfzToWaBFZLp+JN1Qrca6pOaB3GHB1DYFCgw2My0jJ4oeoL7ErZladzf/juTOZ+Uo5y5f9F0ul/06NvEk8N01KaKn/yvA5KRBrmfAEVgSDb10VKpzvuYMPyn7gu9Somd/qQoVWHMrnTh1yXehUblv9UbIOTKkKydO09+fsBVuwrWAKFu1lq5SqU49Vn3+SmqKZcXboON0U15dVn33SY5Xfy+Enmz15JWHgvAMLCezF/9kpOnXB+LaXyylmSxHu2P0sDjYHfAQHqA+uBVt4dmvuMMYiIy+Nq16rF+2+PytdzpqLK1x2TVd51GVqX+GGp8MYB/oiG8oHl3f5s1vVV9iw1Z8+g1n66lnNn0/jyoytIT1sH1CD5TAJffjSD+bN6MPGL0Zc9g5kz8xsy0u8iKMi6dRgUFEVK+l18MWO+zqKURzkMUMaYtgAiMgfob4zZant/IzCkcIbnWum0NE4kJRFZrpxbQaokMcZwIimJ0mlpvh6KyqOR74bwyrBINq5NI8jNyX1g+dNUjDxN1WjrfevHWzP4H4OdZqmtnL6KtHOzgR5Z9tQmPe0d0tO68tRDnZm0ZgzX17k+M/itWRFPevoxTh7/Itv5fl5Sno1rNjH2ozepEOl8WUdB5aVDriq63Ekzv84enACMMdtEpIH3hpQ3MSdOcBCrBJC6XOm0NGJOnPD1MFRexMezOC6cJpFA22GQ7ubHvofUq/ZwJHPLddz9yL+Z8eBgmvVuSvM+l569rv10Pas/Wk166t1kD05ZNScttT/TX/6Re1+K5sYbTwPw8qLBuR795dgFfDNxOxOmTOWBId3c/W7znLmYW4fcKaOnAGiQKmbcCVA7RGQGVst3A/QCdnh1VHkQfPEitY4d8/UwlPKYxXHh0KYtNMlbNp91+FXZtjVodxWtr7+N+QtHM7rVWNJSLxAcUoq2bXtD2kbMxXecnvNixhNsXdGSOxp8wcY/9jg87uyZk3w/bQehpSfz/bSnqBr1JGHhrmdRQVWOsq38H9zosp/2JdNnTqfdkHZE3xRNGmlE3xRNuyHtmP7BdK647Ypsx3oybV8VPncC1KPAQKxeUGAVjZ3stREpVYItHr3d+iKPwcmZ6OjaVI68looRbxEe/hzJyeOoHAkXLpwGXKVRV+fcueO5Br+s5v60gCDuITysHsnJ93Do15/p0eM514NLv4r473Ea/HI6sOMUFWOuJuXUpezEijFXc2DHAjbOuxSQQq77g238QcWCNQrIVdVoDX6FwZ1iseeB8baXUspb4uOh6rXQq5dHT7t27Td88cU7pKefxXp8XIrZs0MwJgQIAaKAnsDTQM4lG/sJDXW8jgogKek4K1Z8S2ioVYw1NLQ3K1bcT4cOfShXznV0cBX8coqpcjUn/jxKjfqXPpOwfQ8xVa6mQVSW8xy/ivh4q7KAp52883uvBL+6MeX9upBwYXMZoESkJfA61q9amccbY9z/P0op5dzs2Sw+3BCqeva0c+aMIDb2XayOOU9i3Z3vizGP2d7XABKAmUAz4DOgU+bnAwNn0KZNz5ynzWbp0s/IyLiLwMAo22eiyMi4i6VLP3VvFpVHHdoOYuF7I+nw/J3E1K3Bwe0JLH3ve+5u+8plx3pwIprd8Ts9HvzCWqxh9YnTwGkPntVSMZICr6vzBXcqSfwBDMbqA5Vh326MKfQn77kt1FWqSLMlRAAwdFieP56UdJzx459k8OBpl81WtmxZwcsvdwF+BJoDu7GC0CLb+5zWYtWBXoc1k1pLSEhXJkxYR3R0bQ4d2smwYR15991lHP3fbpb+NIm/j+0j+UwSZ0+mERxuuGguECClMOfDqV79et56yzu9lDZuWpJ5/cqVatKh7SAaNezolWsVdfHxVvALLH/aK+e/8caC3+50tFDXnWdQicaYHwp0daWUY1WvzPdtvaVLP+PPP0/lOluZOnUY1szJHowmAk+Qe3DCtv1x4G0CAysTFDSD4cM/Izq6tu18w0lKqsiYsX0oV03oMOROYuo+wF+b/ss3b31B03vacGuv2y/NaNo8la/vyR2NGnbUgOSmJk2A9BbghUTn+HjYhnW70xvcCVA/icgYYD6Qat9ojNnklREpVVLYb+u1uSZfH7c/+6lQYTIrVgy87JnPgQPbgTlZPhELuOq2/ARQj7Zt+9Kjx7rM4HTo0E62bdtKcPB8/j79D+4ZOzDzGVBEjTDuHnkPq6f+Qtu+HahR/yo6PH8nS8dO0iBSzDVpAhx3XIS7oNxpWNgUq5LE21jVJd4DxnptREqVEFZwyns6uZ392U+pUtdmPvPJ7hzZs/SO407WHlwgOvrqzOAE1uzp4sWeBATUxxBCSNSlDLq09FRqNqrJiYOXfkWPqVuDv4/ty9f3pZSdO1l8bQtjIEqVJItHb7du7eUzODnLnNu373fb7b3SZM/Sq4iVEOGsuPJ+IIQvvniHL798i7S004SEVCQ1FQIDhwIg3EDCtn1cEV2d4ODSBAeFsG/jPiJjLmX7HdyeQOVKNfP1vSll584tPkSkM3AD1v/xABhjRnhrUEoVa7NnAw0LlE7uKHNuzJiH+f33VVjPnuaQPUvvAjAdcFaLcjrwIOnpkcBHwELOn78emEp6elfgMy4mDeY/7z9HSEhpbr6tJYkJKSx86xua3tOGjPQMp1l1SuWFO1l8U4AwrGaFM7A67MYbYwq9KqRm8akizY2MPWdZeVn93/915ejR7C1ULlxIIjHxEJey9nKaC/R1sv/yLL7L39+BSBlE0ikTKVSqFE3lSjWpXa0puw+s91hWnWbplSxdu0q+s/haGGPqi8gWY8wbIvIeVsKEUioPFseFu8zYc5aVl1Vu6duDBt1CYmI3HGfp9QC+AjoC/YEBWM+c9mP97jkDax2U/RZgc6AfMAkYBzQnMPAZOnRIZcAA7/2iuHHTEhbGjczMEjy4PYGF740E0CBVwriTJHHO9meKiFQF0oDi13ZWKS/KLGHkJDhlz8r7lqSkvC01tLL2nnRx1CgglTJlYoF6QCjQEitBdx1ZF+la+mFl/1kyMvoRFxeLNy39aRIdnr+TGvWvIjAo8FJW4E+TvHpd5X/cCVDfikh5YAywCdhH9txVpZQz8fHWzMnFQlzXWXmu5Mzay42VpXfvvc9jBaXzwFGsGVJuyRPVyb6AxqrN501/H9tHTN3s34dmBZZM7tziG22MSQW+FpFvsRIlznt3WEoVE26WMMqZlQe1+OKL/sya9TLWX7dQqlWry5NPvkv9+u04cmQ3CxZMJC4ulvPnjxMSUhFrNrQSaOfkSvuBUFas+BaRSIxxJ6svKtt7V7X5CqpypZoc3J6QrdaeZgWWTO7MoNbavzDGpBpjErNuU0rlbvHo7VZwGjrMZcZe1qy8EydGcPRoL9LTHwW2YmXfbeHAgba8/HIXxo17hGefbcayZaGcO7cGY1I5f34d8BRwL+Cs8MsUIiKuICPjLsqWfRgru8+ZGVgp6hZ3avMVVIe2g1j63vckbNlDRnoGCVv2sPS97+nQdpBXr6v8j8MZlIhUAa4EQkXkZqx27wDlsLL6lFKOxMcD4SQNeJzxb9znMitv8+Y4MjIOc+zYFAeZeLWB0cA9xMXdDnxCzi641l34e4G7gHgunxmtBT6kfPkbSEmJJSDgHFYKehccZ/XNwHo2Zb0PCprB3Xevy+VYz7EnQiwdO4m/j82hcqWa3N32FU2QKIGc3eLrgJWTGoNVPcIeoM4AL3l3WEoVYZkljNrmOSvPdSZec6yZ0lpy74TbHKuFWy+sHqP2LL3JwGRKlarMrbc+SI8ezzF37jjmzfuUCxc6AQPJyOiX5fgpwMe2FwQGvnhZbT5v0lp7Cpzc4jPGfGqrItHXGNPOGNPW9upqjNE0c6UcsAenpOuuynNWnnuZeAPImll3uYFYbTVaYj2Xag5MITLyGqpUWcKKFd9y6NCfrFjxLZUqfUVU1PW0bZtIWFhLREIpXbo51av/TOnSIHIPYWEt6dAhlQkT1tGoUc4sP6W8x50kiRgRKYc1c5oONASGG2OWeXVkShU1mQkRVgmjpXPHkZFxF6Gh15Kc7G5/JHcz8Zxl0lUHkrnUVygNKE1w8COUKmWNZerUYZlju3ChB9HRMGfOUXe+S6UKjTtJEo8ZY5KA9kBlrPsHzmqlKFXyxMdfKv7aq1eWrLzegL1WnjuzqFCs50LO5Mysc7XfytwrVeouAEqVeoht27Zmvnd/bEoVLncClP3Z053Ax8aY37NsU0rZSxhlKf7qrMusM9Wq1QWmurjgFLJm1l1uRo7904GbSE7+FoDkZOHixZ6Z790dm1KFzZ0AtVFElmEFqKUiUha46ImLi0hHEdkpIn+JyHBPnFOpQvfnn5eVMLKy8mJJTGyc+crIiGXz5jinp+rV6yWs0kKOVnJYmXiOkyjsmXeDsryfiMhfnDkzhsTExpw50wSYmfnePrYNG5byxhv36UxK+Q13nkE9DjQA9hhjUkQkEus2X4GISCDW38Q7gIPAryKyyBizvaDnVqqwWCWMLm86mN9W5wcP7qVUqcpcuHA7VrZe1np5U4APadPmXtaufYr09E1OM+9EhmLMZNq1e4h//Wu6y2vPnTuOBQu+dfNZmVLe53AGZVsHhTHmojFmkzHmtO39CWPMlqzH5FMT4C9jzB5jzAWs8kl3F+B8ShWu+Hjrz6HD8t3XKSv7c6sqVZYQGXkNVasuw6qXFwLUIyZmBW++uZjnnpvFhAnraNv2NCINgFBEGhATsyIz8y40tAVhYfOIjp7Pzp27Xc6KCloHUClvcHaL73s3Pu/OMY5cCRzI8v6gbVs2ItJfRDaIyIZjiYkFuJxSHjR79qXnTh6StRZfcPAjVK58FVWqvMnVV1+kSpU3adv2YerXt8oYRUfXJjq6Dldc8QZXX53OFVe8Qdu2D/PVV8dZuDCd7t2HUbbs05Qpc4dbz5cKXgdQKc9zFqBuEpEkJ68zwBUFuHZuiRaXNacyxkwzxjQ2xjSuFBFRgMspdcnuI0d4avJHlHugLwF3d6PcA315avJH7D5yxOVnM0sY2TL2PCFn1l+pUp1tmXZWskPOTDtnWYJ5zSDMf8ahUt7lbKFuoDGmnJNXWWNMQX59PAhUy/I+Bjjs4FilPOaHjRup/+xwZiy7ljPn4jEmlTPn4pmx7FrqPzucHzZudPxhD9/Ws8uZ9Zec/J0t087anzPTzlmWYF4zCPObcaiUt7nV8t1LfgXqiEgt4BDwIM5zZ5UqsN1HjtB91ARSUr8jZ627tIxRpGXcTfdRndkyYRS1o6OzfzhrOrmH2DvopqScJSPjOKdOfUZS0hGMESCQM2c+ITCwcubxmzdXpUeP5zJr9yUmZq8osXmzVTbd0b7ckh+cnUuTJZQv+SxAGWPSReRpYCkQCHxkjPmvr8ajSob3FvxAWnp/nNW6S0t/gvELf2DigMey7XGnI25e2Wv1det2V2Z9vAULvs1870h+swS9fS6lPMmddVBeY4z53hhzjTGmtjHmLV+ORZUMs+NWkpbxhNNj0jL6Mytu1aUN8fFWOrmHg1POzDl7fTzNpFPK4laAEpFAEakqItXtL28PTClvSD5/Gndq3SWfO219ab+t58GECLucmXP2+niaSaeUxeUtPhF5BngN+B+XKkgYoL4Xx6WUV4SXLs+Zc667yIaHls/2zOlItUgWTB6c2cG2dOko2rTpSbduT+er/UTODrpW1t6HVK06GYCgoNbMn/8Ac+eOIjX1RIGvp1RR5M4M6p/AtcaYG4wx9WwvDU6qSOrV5laCA51XVQgOnMYjbVpnljDaeH3kZR1sz51bw7JloTz7bDM2bnTWwTZ3zrL2zp79gUOH7uTs2R6cP7/WI9dTqihyJ0AdAHSFrCoWnu/WieCgaTirdRccNJ3BXGDx4YYciQpj1KjepKYuIiPjbayZVxBQm4yMt0lNXcSoUb05cmQ3AIcO7aRXr1ocOrQr17MnJR3njTfuY8OGZdlq9Z05MwaYSVJSQ44cuR9jFgHv5nq9kSMfYNeuDZ79wSjlh5yVOnpORJ4D9gBxIvKifZttu1JFTu3oaOYNf5awkM4EBw4DdmP1S9pNcOAwwkI6M++eDmxPuhWGDmPB3lWkpz+Bs6y/9PR+LFw4CYCpU4eTlFSRqVOH5nq0PWuvceP2zJy5IfP19ddHWLDgEHfc8QCBgc84vd7Fi086PL9SxYmzGVRZ22s/sBwolWVbuPeHppR3dGrUiC0TRtG/w5+UC2tKgIRSLqwp/Tv8yZZ/NCf9YIPMtU5xcbFkZDzu9HwZGf2Ii4vl0KGdbNu2leDgj9m2betlsyh36t25cz0YwK5dv2qWnyr2nFWSeMMY8waw3f51lm07Cm+ISnle7ehoJg54jMQ5H5Ox8BsS53xMh6Rm1swpS8be+fPHcSfr79y540ydOpyLF3sSEFCfixd7XjbLcafenbvXM+acZvmpYs+dZ1AvurlNqaLLQQmj0qWjcKfDbUhIRbZt20pg4EAAAgMHZptFuVvvzt3riUTqWilV7Dl7BtVJRD4ArhSRCVlenwDphTZCpbzNSQmjNm16Ehg40+nHAwNnUKZMRdvsySqPFBAQnW0W5W69O3euBzMoV+5hXSulij1nM6jDwEbgvO1P+2sR0MH7Q1OqcDgrYdSt29MEBU3HWdZfUNAMUlLOADNJS7sy8wUz2bXrN8D9DrvuXA8mEhi43K0OvUoVZWLMZR0ush8gEmyMSSuk8TjVuE4ds2HcOF8PQxUX9pkTWLf2HNi48QdGjepNenq/bB1sAwNnEBQ0g+HDP6NRo04eG1ZhX08pX+vaVTYaYxrn3O6wkoSIbMXWn0nk8tZNulhXFWlZSxi5aJvRqFEnJkxYx8KFk4iLa8m5c8cJDbUqO9x99zqPV3Yo7Osp5a8czqBExJ5KNMj25yzbnw8DKcaYEV4e22V0BqU8xRvFX5VS+ZPnGZQxJgFARFoaY1pm2TVcRH4BCj1AKeURs2dD1S4anJTyc+6kmZcRkVb2NyLSAijjvSEp5UWzZ1vt2q+5xtcjUUq54E7DwseBj0Qkwvb+NPCY48OV8kOZCRENnSZEKKX8h8sAZYzZCNwkIuWwnllp4VhV9Pz5J7R53mVChFLKfzjL4utljJmdszCsPaPPGKPZCqpIWDx6O9AQ9K6eUkWKsxmU/TlT2cIYiFJeER8PhOttPaWKIGdZfFNtX75rjDlfSONRynOclDBSSvk/d5IktonI/4BVwErgF30OpYqEP//UdHKlijB3kiSuFpHqQGvgLuBDETltjGng7cEplS/ZMvY0OClVVLkMUCISA7TEClA3Af8FVnt5XErlTx5KGCml/Js7t/j2A78CbxtjBnh5PEoVSOYzJw1OShV57lSSuBn4DOgpImtF5DMRcdWTWqnCN3u21tdTqhhx5xnU7yKyG9iNdZuvF3Ar4Kqrmiridh85wsQFC4iNi+P4+fNElS5NzzZteLpbN2pHR/t6eNnZSxi10cVOShUX7jyD2gCEAGuwnj3dai8kq4qvHzZupPeoUTyRns6ajAxqAAnnzjFz2TKarVjBZ8OH06lRI18PU0sYKVWMufMMqpMx5pjXR6L8xu4jR+g9ahSLUlNpnmV7beDtjAy6ZGTQddQo1k2Y4B8zKb2tp1Sx5PIZlAankmfiggU8kZ6eLThl1Rzol57OpIULC3NYl5s925o9aWVypYold5IkVAkTGxfH4xkZTo/pl5FBbFxc4QzIgcWHbbf1NGNPqWLJnVt8qoQ5fv48NVwcUx04fu5cYQznclrCSKkSwVk183udfdAYM9/zw1H+IKp0aRLOnaO2k2P2A1GhoYU1pOy0hJFSJYKzGVQXJ/sMoAGqmOrZpg0zly3jbSe3+WYEBtKzTZvCGxRoCSOlShhn1cwfLcyBKP/xdLduNFuxgi4ZGbkmSqwFJmZkUHPdOhr/+ivlIiJYMc777cG0hJFSJYtbz6BEpDNwA1Davs0YM8Jbg1K+VTs6ms+GD6frqFH0S0+nX0YG1bFu680AZojwVZUqdCpjtQxrnOj94vZW00E0OClVgrjM4hORKcADwDOAAD3A5TN0VcR1atSIdRMmkNqhAy3DwggVoYEIqRERrKtePTM4FQp7CSNdiKtUieJOmnkLY0xv4JQx5g2sZTDVvDss5Q9qR0czbsAAjs6ZQ/rChVwbFcW4SpWoHRxceIOwlzDStU5KlTju3OKz5xKniEhV4ARQqyAXFZEewOvA9UATY8yGgpxPucdVbT1X+1MzMhj899/EnjnDcWOIEqFn2bKkBnlhtYKWMFKqxHNnBvWtiJQHxgCbgH3AnAJedxtwL1aHXlUIfti4kWbPPkvosmWsOXeOVGNYc+4cocuW0ezZZxkxZ47L/ftOniQ0KYk1xpAKrDGG0KQk9p08yQ8bN3p+0HpbT6kSTYwxzg8QCTHGpNq/xkqUOG/fVqCLi8QBQ9ydQTWuU8dsKIRsseJm95EjNHv22ctq69nNBfoCP4LDrL3bgU+wHkDmtr9rSAhXV6lCWkrKZfvznOWXWZlcM/aUKgm6dpWNxpjGObe7c29mLdAQwBaUUkVkk32bt4lIf6A/QPVKlQrjksWOq9p6a4BB5B6csG1/Cut/hNwClL0236z//Y+DMTGX7c9rlp8GJ6UUOK8kUQW4EggVkZuxMvgAygFhrk4sIj8CVXLZ9X/GGLerjBpjpgHTwJpBufs5dUlsXBxrnCy6jcUKUs4MAFoCjuZB/TIymHjxYv4GaJe1hJEGJ6VKPGczqA5Yd35iyP7vUhLwkqsTG2NuL9DIlMe4qq13HNfrBqrbjnO2P8XF7WKXtISRUioLZ5UkPgU+FZH7jDFfF+KYlIe5qq0XBSSA69p7LvaHiTg5wgktYaSUyoU7WXy/iMhMEfkBQETqisjjBbmoiNwjIgexHl98JyJLC3I+5VzPNm2YGRjoeD8w1cU5ptiOc2RGYCARISH5GB2Xbutpxp5SKgt3AtTHwFKgqu39n8C/CnJRY8w3xpgYY0yIMeYKY0yHgpxPOfd0t25MDwpirYP9LYBJ4HD/WuBDHCdRrAVmBAVR7YoraJyYeNmrXESEw7FlljDS23pKqRzcyeKLMsZ8JSIvAhhj0kXEeTc75VfstfXueOMNngH6QfbaesAwoKttX879E4FhPXvyWGwsmxzs/2r4cDo1apS3gcXHQ9VrNTgppXLlzgzqrIhEYrXYQESaAd6vDqo8qlOjRpQRITUggPpAKFZWXiqwDnjV9meqbXsoUB9IjYigZsWKvPrgg9SsWJHUiAhaBgRYnw8IyNyf5+Bkb9eulFIOuDODeg5YBNQWkV+ASkB3r45KeUWQCOOCg3k/NZVULv+PXxsrXXMckIYVpMZVqpS5jikkMJBxFSsyLsd6tDytc9ISRkopN7kMUMaYTSJyG3At1lqoncaYNK+PTHmNPWtvAfAWcN72KmV7BWKtJQgBYnbv5rgxBHTtSmngltOnebdSJdqFuVwK51jVK/W2nlLKJXfabZQGngVGAm8Ag2zbVBHVMyCAdli39foBW7GmyOFYC3I3YN3q2wr0NIZw2/6tQNu0NLocPsyIEyfyfmH7bT2tTK6UcoM7t/g+A84AH9jePwTMIveqN6oQtXvuOZJyub1mr313ZY8ekHZpspty8SJVUlNJwpoK22vv7QYeBRaTPVOvNjAauAcrgWJdlve3nzrF+6dOUTogAGztN1yNR0sYKaXywp0Ada0x5qYs738Skd+9NSDlvqTERDbkksKd+UwoLY1DWXo3VUlN5ShQEWvmZA9GE4EncF6Lrx9WKvo4LtXm+7lUKeKrV8+8nsPxHD5spZNrCSOlVB64k8X3my1zDwARaQr84r0hKW87DzyZ5X0s4GrldT/bcXYDgP9euOD6YidOcC6jlDVz0udOSqk8cGcG1RToLSL7be+rAztEZCtgjDH1vTY65RXnyV57Lz+1+KpzqZOlQ2fPcjotDEIydOaklMozdwJUR6+PQhWq0mSvvWfP6gPrdl8sVjCKwipv9HSW4+z2Y6WhO3P6TAAEl4IgXdetlMo7l7f4jDEJzl6FMUjlWaWxauvZ9cQqT98MK+iswcriW2N73wx4key1+KYAN5Qq5fAap4/a5leRFT02bqVUyeLODEr5qXIREdkWyR48dYrAixcJCAig8eOPk2HL2ksDSgcEkIrVoCsFq7bevVgJD11sr5wddWsDb9v23Y6V5QeXavNdGRqardZe5nhSUzmXFgDlykHiMUIiKnvvh6CUKrZctnz3J9ry3bnGjz/uMKtvw8yZme9vGTSIGgcO8DNW8sP/gMrAKCfnHoZ1268iVnAa1rMnrz744OUH2tu162JcpZSbCtLyXRUz2w8cYI7t60nAl8AWF5/pD9QDbqxencX9+9Ou/uW5MVZlcl3rpJTyDA1QJdA5rKy9IKx1Te/jXhbfBRHiJ07M/QCtTK6U8jB31kGpYiaUS1l7kD2Lz5H9QFSog7w9rUyulPICDVAlUN1q1bJ10O0JzHR0sM2MwEB6tmmT677MEkY6e1JKeZDe4itGcmb1Zd2e1btPPkmXl1/mHqysvaexUsm7kHu5I3vH3HV33519h711hpYwUkp5gQaoYmSFmxmO7erXZ1jPntweG8tTWGWLPsIKUI/a3md2zA0MZEZQEJ8NH07t6OhLJ7EHJ02IUEp5iQaoEurVBx+kVd26DJ82jQ/37+ccVv+nOeHhfJyWxukLF4gKDaVnmzasu/tuDU5KqUKnAaoEa1e/vuOsPCf0tp5SqjBokoTKm9mzrT81IUIp5WUaoJT74uOtjL2hw3w9EqVUCaABSrnHvtap6pW+HolSqoTQZ1DKJS1hpJTyBQ1QyjktYaSU8hG9xacc0xJGSikf0hmUciizhJHe1lNK+YAGKHU5+0Jc0OCklPIZDVAqO60SoZTyE/oMSmWjVSKUUv5CA5S6ZPZsbdWulPIbGqCUZfZsKylCg5NSyk/oM6iSLjMhQksYKaX8iwaoku7PP6HN8/rMSSnldzRAlWCZJYyu8fVIlFLqchqgSqr4eCBcb+sppfyWT5IkRGSMiPwhIltE5BsRKe+LcZRYWplcKVUE+CqLbzlwozGmPvAn8KKPxlFytWmrGXtKKb/mk1t8xphlWd6uA7r7YhwlTtaMvV6aFKGU8m/+8AzqMeBLRztFpD/QH6B6pUqFNabiR0sYKaWKGK8FKBH5EaiSy67/M8YstB3zf0A68Lmj8xhjpgHTABrXqWO8MNQSQUsYKaWKGq8FKGPM7c72i0gf4C7gH8YYDTzeNHs2VO2iz5yUUkWKr7L4OgLDgK7GmBRfjKHEsJcwukYXOymlihZfPYOaCIQAy0UEYJ0xZoCPxlI8aQkjpVQR56ssvqt9cd0SRUsYKaWKOH/I4lMepiWMlFLFgQao4kpv6ymlijgNUMWJ/bmTljBSShUD2rCwOPnzT+2Iq5QqNnQGVRxky9jT4KSUKh40QBV1WsJIKVVM6S2+Ik5LGCmliisNUEXZ7Nn6zEkpVWxpgCqqtISRUqqY02dQRY2WMFJKlRAaoIqaP//UyuRKqRJBA1QRklnCqI3e1lNKFX8aoIoava2nlCohNEAVBVrCSClVAklRamYrIseABF+Pw4Eo4LivB+Gn9GfjmP5sHNOfjWPF7WdTwxhTKefGIhWg/JmIbDDGNPb1OPyR/mwc05+NY/qzcayk/Gx0HZRSSim/pAFKKaWUX9IA5TnTfD0AP6Y/G8f0Z+OY/mwcKxE/G30GpZRSyi/pDEoppZRf0gCllFLKL2mA8iARGSMif4jIFhH5RkTK+3pM/kJEeojIf0XkoogU+/RYd4hIRxHZKSJ/ichwX4/HX4jIRyLyt4hs8/VY/I2IVBORn0Rkh+3v0z99PSZv0gDlWcuBG40x9YE/gRd9PB5/sg24F1jp64H4AxEJBCYBnYC6wEMiUte3o/IbnwAdfT0IP5UOPG+MuR5oBgwqzv/faIDyIGPMMmNMuu3tOiDGl+PxJ8aYHcaYnb4ehx9pAvxljNljjLkAzAHu9vGY/IIxZiVw0tfj8EfGmCPGmE22r88AO4BiWwNNA5T3PAb84OtBKL91JXAgy/uDFON/aJTniUhN4GZgvY+H4jVaLDaPRORHoEouu/7PGLPQdsz/YU3FPy/MsfmaOz8blUly2aZrPpRbRCQc+Br4lzEmydfj8RYNUHlkjLnd2X4R6QPcBfzDlLBFZq5+Niqbg0C1LO9jgMM+GosqQkQkGCs4fW6Mme/r8XiT3uLzIBHpCAwDuhpjUnw9HuXXfgXqiEgtESkFPAgs8vGYlJ8TEQFmAjuMMeN8PR5v0wDlWROBssByEdksIlN8PSB/ISL3iMhBoDnwnYgs9fWYfMmWTPM0sBTrQfdXxpj/+nZU/kFEvgDWAteKyEERedzXY/IjLYFHgHa2f2M2i8idvh6Ut2ipI6WUUn5JZ1BKKaX8kgYopZRSfkkDlFJKKb+kAUoppZRf0gCllFLKL2mAUkWWiPQVkapuHPeJiHR3d7sHxvVSlq9rulOV2zaWvSIywMkxDTyZUmz7+U0s4Dn2iUiU7es1nhyTiAwWkf0FHaMqujRAqaKsL+AyQPnAS64PydULxhhna+caAD5b8yIiTivPGGNaePJ6xpjxwKuePKcqWjRAKb9gm2n8ISKf2vppzRORMNu+RiLys4hsFJGlIhJtm/k0Bj63LVYMFZFXReRXEdkmItNsq+7dvf5l17BtjxORd0UkXkT+FJHWtu1hIvKVbaxfish6EWksIqOAUNuY7LUYA0Vkuq1/zzIRCXVjPD1s38fvIrLSVm1iBPCA7dwPiEgTEVkjIr/Z/rzW9tm+IjJfRJaIyC4RGZ3lvI/avo+fsRZ92rd3sX0Pv4nIjyJyhW3767af5TLgMxGJtH0Pv4nIVLLUFBSRZNufI7IsIj0kIh/btvey/Rw3i8hUsVqOOByTUhhj9KUvn7+AmljFUlva3n8EDAGCgTVAJdv2B4CPbF/HAY2znKNilq9nAV1sX38CdM/lmp8A3d24xnu2r+8EfrR9PQSYavv6RqziwI1t75NzfF/pQAPb+6+AXo7GkuX9VuBK29flbX/2BSZmOaYcEGT7+nbg6yzH7QEigNJAAlbdv2hgP1AJKAX8Yj8fUIFLC/f7ZfmeXwc2AqG29xOAV21fd7b9N4vK+X3b3kcAW4BGwPXAYiDYtu9DoLezMeX2PeurZL20WKzyJweMMb/Yvp4NPAsswQoAy20TokDgiIPPtxWRoUAYUBH4L9Y/iq5c6+Ia9oKcG7ECDkAr4H0AY8w2Edni5Px7jTGbczmHM78An4jIV1mun1ME8KmI1MEKFMFZ9v3HGJMIICLbgRpAFBBnjDlm2/4lcI3t+BjgS9vMsRSwN8u5Fhljztm+vhWr8STGmO9E5FRuA7PNXj8HxhtjNorI01iB6lfbzzgU+Bto6mRMqoTTAKX8Sc66WwbrFtJ/jTHNnX1QREpj/Vbe2BhzQERex5o9uMPVNVJtf2Zw6e+M27cPs3zefg6Xt/iMMQNEpCnWLGWziDTI5bCRwE/GmHvE6g0U5+Sa9nE7qm32ATDOGLNIRNpgzZzszuYcnqvx2z5/0Bjzse29AJ8aY7J1mRaRbm6eT5VA+gxK+ZPqImIPEg8Bq4GdQCX7dhEJFpEbbMecwSrOC5eC0XGxeuXkJTvP2TUcWQ3cbzu+LlAvy740sVoi5JuI1DbGrDfGvAocx7pFl/X7BWsGdcj2dV83TrseaGN7jhQM9HBwrj5OzrESeNg2xk5YtwZzjv0u4A6sGbDdf4DuIlLZdkxFEanhYkyqhNMApfzJDqCP7XZZRWCysdqhdwfeFZHfgc2APVvsE2CKiGzGmjFMx3p2swCrnYVbXFzDkQ+xgtoWrBYrW4BE275pwJYsSRL5MUZEtoqVor4S+B34CahrT5IARgPviMgvWLclnTLGHMGa2awFfgQ2Zdn9OjBXRFZhBURH3gBuFZFNQHus50c5PY+VXWlPiBhhjNkOvAwss/3MlgPRLsakSjitZq78gu0W1bfGmBt9PRZ32DLQgo0x50WkNtYM4RpbsMvP+T7B+v7neXCYRZ6I9MW6bfu0r8eiCp8+g1Iqf8KAn2y3pQQYmN/gZJMIjBSRKON8LVSJISKDgQFY3WNVCaQzKKWUUn5Jn0EppZTySxqglFJK+SUNUEoppfySBiillFJ+SQOUUkopv/T/ObqfDvBF220AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "X_combined_std = np.vstack((X_train_std, X_test_std))\n",
    "y_combined = np.hstack((y_train, y_test))\n",
    "\n",
    "plot_decision_regions(X=X_combined_std, y=y_combined,\n",
    "                      classifier=ppn, test_idx=range(105, 150))\n",
    "plt.xlabel('petal length [standardized]')\n",
    "plt.ylabel('petal width [standardized]')\n",
    "plt.legend(loc='upper left')\n",
    "\n",
    "plt.tight_layout()\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "So we can see that <b> NO </b> linear seperator exists that will perfectly seperate these classes because flower class 1 and flower class 2 overlap.  Applying kernal tricks or non-linear seperators may work, however Perceptrons are for our purposed just stepping stones to full up Neural Networks."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
