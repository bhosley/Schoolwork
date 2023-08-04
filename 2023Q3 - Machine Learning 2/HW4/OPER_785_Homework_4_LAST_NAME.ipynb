{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WL8r9O70RrQi"
      },
      "source": [
        "# NAME: <Last Name, First Name>\n",
        "\n",
        "## OPER 785 Homework 4\n",
        "\n",
        "In this assignment, you will be asked to construct an ANN to predict time-series data given past observed values."
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Instructions:** You have data from a time series, and you must construct a neural network to predict future values based on additional instructions below.\n",
        "\n",
        "**Data:**"
      ],
      "metadata": {
        "id": "c7cCsX4YjDI9"
      }
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jv2EIMfsRrQj"
      },
      "source": [
        "Mount your Colab drive to make data available for use."
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "id": "Tkg7MfWkJR7k"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dQt5ammORrQk"
      },
      "source": [
        "## Setup"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Gv0T_OYORrQk"
      },
      "source": [
        "Import a few common modules, ensure MatplotLib plots figures inline and prepare a function to save the figures. We also check that Python 3.5 or later is installed (although Python 2.x may work, it is deprecated so we strongly recommend you use Python 3 instead), as well as Scikit-Learn ≥0.20 and TensorFlow ≥2.0."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "pey0aa46RrQk"
      },
      "outputs": [],
      "source": [
        "# Python ≥3.5 is required\n",
        "import sys\n",
        "assert sys.version_info >= (3, 5)\n",
        "\n",
        "# Scikit-Learn ≥0.20 is required\n",
        "import sklearn\n",
        "assert sklearn.__version__ >= \"0.20\"\n",
        "\n",
        "try:\n",
        "    # %tensorflow_version only exists in Colab.\n",
        "    %tensorflow_version 2.x\n",
        "    IS_COLAB = True\n",
        "except Exception:\n",
        "    IS_COLAB = False\n",
        "\n",
        "# TensorFlow ≥2.0 is required\n",
        "import tensorflow as tf\n",
        "from tensorflow import keras\n",
        "#assert tf.__version__ >= \"2.0\"\n",
        "\n",
        "if not tf.config.list_physical_devices('GPU'):\n",
        "    print(\"No GPU was detected. CNNs can be very slow without a GPU.\")\n",
        "    if IS_COLAB:\n",
        "        print(\"Go to Runtime > Change runtime and select a GPU hardware accelerator.\")\n",
        "\n",
        "# Common imports\n",
        "import numpy as np\n",
        "import os\n",
        "import pandas as pd\n",
        "\n",
        "# to make this notebook's output stable across runs\n",
        "np.random.seed(42)\n",
        "tf.random.set_seed(42)\n",
        "\n",
        "# To plot pretty figures\n",
        "%matplotlib inline\n",
        "import matplotlib as mpl\n",
        "import matplotlib.pyplot as plt\n",
        "mpl.rc('axes', labelsize=14)\n",
        "mpl.rc('xtick', labelsize=12)\n",
        "mpl.rc('ytick', labelsize=12)\n",
        "\n",
        "# Where to save the figures\n",
        "PROJECT_ROOT_DIR = \".\"\n",
        "CHAPTER_ID = \"hw4\"\n",
        "IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, \"images\", CHAPTER_ID)\n",
        "os.makedirs(IMAGES_PATH, exist_ok=True)\n",
        "\n",
        "def save_fig(fig_id, tight_layout=True, fig_extension=\"png\", resolution=300):\n",
        "    path = os.path.join(IMAGES_PATH, fig_id + \".\" + fig_extension)\n",
        "    print(\"Saving figure\", fig_id)\n",
        "    if tight_layout:\n",
        "        plt.tight_layout()\n",
        "    plt.savefig(path, format=fig_extension, dpi=resolution)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*TO DO:* Load other packages you feel necessary to solve the problem at hand."
      ],
      "metadata": {
        "id": "_Sjgk9_dVMo5"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "6kNSgfHPVk_H"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Some plotting code that will be useful later**\n",
        "\n",
        "You can adapt use this code or adapt it as you require. Alternately, you may code your own plotting algorithms as you see fit to meet the requirements in the sections below."
      ],
      "metadata": {
        "id": "fdulqH_GaDa2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def plot_series(series, y=None, y_pred=None, x_label=\"$t$\", y_label=\"$x(t)$\"):\n",
        "    plt.plot(series, \".-\")\n",
        "    if y is not None:\n",
        "        plt.plot(time_steps, y, \"bx\", markersize=10) # You will have to change \"time_steps\" to comply with your variable naming\n",
        "    if y_pred is not None:\n",
        "        plt.plot(time_steps, y_pred, \"ro\") # You will have to change \"time_steps\" to comply with your variable naming\n",
        "    plt.grid(True)\n",
        "    if x_label:\n",
        "        plt.xlabel(x_label, fontsize=16)\n",
        "    if y_label:\n",
        "        plt.ylabel(y_label, fontsize=16, rotation=0)\n",
        "    plt.hlines(0, 0, 100, linewidth=1)\n",
        "    plt.axis([0, time_steps + 1, -1, 1]) # You will have to change \"time_steps\" to comply with your variable naming\n",
        "\n",
        "def plot_learning_curves(loss, val_loss):\n",
        "    plt.plot(np.arange(len(loss)) + 0.5, loss, \"b.-\", label=\"Training loss\")\n",
        "    plt.plot(np.arange(len(val_loss)) + 1, val_loss, \"r.-\", label=\"Validation loss\")\n",
        "    plt.gca().xaxis.set_major_locator(mpl.ticker.MaxNLocator(integer=True))\n",
        "    plt.axis([1, 20, 0, 0.05])\n",
        "    plt.legend(fontsize=14)\n",
        "    plt.xlabel(\"Epochs\")\n",
        "    plt.ylabel(\"Loss\")\n",
        "    plt.grid(True)\n",
        "\n",
        "def plot_ANN_history(df):\n",
        "    pd.DataFrame(history.history).plot(figsize=(8,5))\n",
        "    plt.grid(True)\n",
        "    plt.gca().set_ylim(0,1) # sets verticle range to [0,1]\n",
        "    plt.show\n",
        "\n"
      ],
      "metadata": {
        "id": "4Y_mzeHQaEWK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Load data\n",
        "\n",
        "Data is located in the file \"OPER 785 hw4 data.csv\"\n",
        "\n",
        "**Format:** The data is 10000 sections (samples) of the time series. Each section (line) consists of 51 observations.\n",
        "\n",
        "*To Do:* Load the data from the file. Keep the data in a variable you can refer to later (in other sections). Sectioning the data file will occur in each part of the assignment as needed for prediction requirements."
      ],
      "metadata": {
        "id": "QZZ_oZnzXrAm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Your code here\n"
      ],
      "metadata": {
        "id": "bbHrl8ScXsOe"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Optional\n",
        "To Do:*\n",
        "\n",
        "Look at your data in whatever way you may need or deem appropriate."
      ],
      "metadata": {
        "id": "RBbqnlKyMptY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Your code here\n"
      ],
      "metadata": {
        "id": "X-e7yy4IM-Ho"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Part 1\n",
        "\n",
        "For part 1, you will be predicting the next (single) value in the time series."
      ],
      "metadata": {
        "id": "JmsarVSHXw61"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "*To Do:*\n",
        "\n",
        "1) section the data into the input and target (x and y),\n",
        "\n",
        "2) section the data into training, testing, and validation sets (70%, 20%, 10%)"
      ],
      "metadata": {
        "id": "6iMYjKQOMcDo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Your code here\n",
        "\n"
      ],
      "metadata": {
        "id": "weDZX8j2Xw62"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Optional To Do:*\n",
        "\n",
        "Explore your time series"
      ],
      "metadata": {
        "id": "eyZu85n6XxKE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Your code here\n"
      ],
      "metadata": {
        "id": "l5rDX3P7XxKF"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "*To Do:* Compute the mean square error of the validation set using a naive forecast."
      ],
      "metadata": {
        "id": "onG23yW1XxWD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Your code here\n",
        "\n"
      ],
      "metadata": {
        "id": "w1y9TL-gXxWE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "*To Do:* Construct a MLP model to make a linear prediction. Then calculate the mean square error of the validation set using your MLP. Discuss hyperparameter choices to include early stopping conditions selected. Experimentation is not required. However, you should explain your reasoning for hyperparameter settings."
      ],
      "metadata": {
        "id": "sjgQUEfMXxn_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Your code here\n",
        "\n"
      ],
      "metadata": {
        "id": "iA4D23gTXxoA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "*To Do:* Plot your losses over the training epochs and discuss model fitness, overfit, and mitigation you may have used for the latter.\n",
        "\n",
        "You may use the predefined functions \"plot_learning_curves\" or \"plot_ANN_history\" or code you have developed for the purpose as you please."
      ],
      "metadata": {
        "id": "2LTnAsGVXxr2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Your code here\n",
        "\n"
      ],
      "metadata": {
        "id": "YE4xEbF-Xxr2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "*To Do:* Plot the first time series sample in your data set an include the truth value and the predicted value from your MLP model.\n",
        "\n",
        "The predefined methods \"plot_series\" may be used for your convenience, or you may use your own code."
      ],
      "metadata": {
        "id": "GaflUEbnXxyb"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Your code here\n",
        "\n"
      ],
      "metadata": {
        "id": "GIDwOtZ3Xxyc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "*To Do:* Construct a Deep Recurrent Network to make predictions for the time series."
      ],
      "metadata": {
        "id": "8s7ap2ipXyAn"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Your code here\n",
        "\n"
      ],
      "metadata": {
        "id": "fhaA1jb3XyAo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "*To Do:* Discuss your RNN. Points you must address: NN depth, width, hyperparameter settings, early stopping (if applicable). Your reasoning for each setting is important."
      ],
      "metadata": {
        "id": "9nlBI4nPfsT9"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Part 1 Analysis\n",
        "\n",
        "*To Do:* Compare and discuss the results from you Deep RNN with the naive and linear forecast models."
      ],
      "metadata": {
        "id": "OqR4_hn5raYq"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Part 2: Forecasting Multiple Steps Ahead\n",
        "\n",
        "Going back to the original data you loaded from the file \"OPER 785 hw4.csv,\" we are going to construct a recurrent neural network to predict 5 steps ahead."
      ],
      "metadata": {
        "id": "CZlheT-cr0un"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "*To Do:*\n",
        "\n",
        "1) section the data into the input and target (x and y). Your y will consist of the last 5 observations in each series.\n",
        "\n",
        "2) section the data into training, testing, and validation sets (70%, 20%, 10%)"
      ],
      "metadata": {
        "id": "s8B6AuMms947"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Your code here\n",
        "\n"
      ],
      "metadata": {
        "id": "fsybzpeifsT_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "*To Do:*\n",
        "\n",
        "Construct a Deep Recurrent Network capable of predicting multiple time steps ahead."
      ],
      "metadata": {
        "id": "LhTwDft4fsiW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Your code here\n",
        "\n"
      ],
      "metadata": {
        "id": "yJ67IesqfsiX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "*To Do:* Calculate the MSE for your Deep RNN. Discuss the difference between the MSE in predicting 10 values vs. the MSE in part 1, where only a single prediction was made. What makes them different?"
      ],
      "metadata": {
        "id": "-0VKhgOOfsnE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Your code here\n",
        "\n"
      ],
      "metadata": {
        "id": "uNdAG6BffsnE"
      },
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
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
      "version": "3.8.5"
    },
    "nav_menu": {},
    "toc": {
      "navigate_menu": true,
      "number_sections": true,
      "sideBar": true,
      "threshold": 6,
      "toc_cell": false,
      "toc_section_display": "block",
      "toc_window_display": false
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}