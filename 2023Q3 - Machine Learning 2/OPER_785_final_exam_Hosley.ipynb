{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "considerable-hamburg"
      },
      "source": [
        "# <center>OPER 785 Final Exam</center>\n",
        "## Summer 2022\n",
        "\n",
        "### Hosley, Brandon\n",
        "\n",
        "This file is designed to test your ability to apply concepts learned in OPER 785. The code provided is intended to reduce the overhead necessary to load data and prepare the environment for the AI tasks.\n",
        "\n",
        "Each of you were asked to establish or verify that you had a Google email account, which gives you access to the Google Colab environment. The code within this file is tailored for Google Colab.\n",
        "\n",
        "The data provided is found within two files available through the links within the code. These files are \"celeba_grayscale.zip\" and \"celeba_attr.csv\". The exam itself will define the contents of these files as they relate to your task(s).\n",
        "\n",
        "## Notes regarding the data\n",
        "Note 1: the CelebA data set is inherent in the tensorflow data sets, but is currently buggy and not generally directly available through tensorflow. In addition, it is too large to use directly without a significantly enhanced environment. The files were obtained from the internet by some researchers in China, and they note the files may not be commercially used since copyrights for the pictures may belong to others.\n",
        "\n",
        "Note 2: You may research the data set if you are so inclined. However, I have modified the actual data to make it more suitable for the RAM restricted environment of colab. In particular, I've made the images grayscale and reduced their size by 50%. The files are 109 x 89 pixels in a single channel.\n",
        "\n",
        "Note 3: Details about the original data set may be found in the readme.txt file linked here: https://drive.google.com/file/d/1S_p93j1oaw89wTXjaa04UrlpT2ay-Czp/view?usp=sharing. Our modified data set is taken from the \"cropped and centered\" data.\n",
        "\n",
        "Note 4: Details about the data partitioning may be found in the .xlsx file linked here: https://drive.google.com/file/d/1_smlpHK38PKsJpkKhO6ScnQOt5-AgZqf/view?usp=sharing. Legend: 0 = test set, 1 = validation set, 2 = test set.\n",
        "\n",
        "Note 5: Details about the data labels (i.e., \"truth\" data) may be found in the .xlsx file linked here: https://drive.google.com/file/d/1ntt5eDCAYgpN7yVznYaxBUVZYicgxK4s/view?usp=sharing.\n",
        "\n"
      ],
      "id": "considerable-hamburg"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Cwl8xLpvvjFD"
      },
      "source": [
        "## Exam Task\n",
        "\n",
        "You have been given access to the CelebA (cropped and centered) data set. The data set has been modified from color to grayscale and reduced in size to 109x89 pixels.\n",
        "\n",
        "You will build a convolutional neural network to correctly classify images from this data set. The characteristic used for classification will be gender (as determined by the original researchers).\n",
        "\n",
        "In performing this task, you will experiment with various parameters and hyperparameters to make your network as accurate and robust as possible in line with class lectures, discussions, and assignments.\n",
        "\n",
        "Deliverables: Completed jupyter notebook with complete code and documentation detailing your work. In addition, you may build a .pdf document that shows aspects of your experiments and results leading to your final model. Please include discussion of your thinking/reasoning in selecting parameter/hyperparameter values leading to the level selected for the final model. In addition to accuracy, you may consider such factors as RAM requirements and training/execution time. Clearly indicate your metrics."
      ],
      "id": "Cwl8xLpvvjFD"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8roKN84QrBTy"
      },
      "source": [
        "## Exam Instructions\n",
        "This exam is designed as a take home exam. It is to be an individual effort.\n",
        "\n",
        "The exam is due before 11:59 on Wednesday, 17 March. Though you have 6 days to complete the exam, you should be able to satisfactorily complete the exam with between 4-8 hours of dedicated work. The exam is open-book, open homework, and open notes. You may freely use examples from the class and book (including the book's github site) to guide your work. However, you may not copy code from other sources to complete the assigned tasks. Your work is to be your own.\n",
        "\n",
        "Required tasks (questions) are clearly indicated in the coding and markdown sections. Complete each task to the best of your ability. If you must make an assumption to continue at any point, please indicate the assumption you are making. For full credit, please document and discuss all work done in sufficient detail to let me know a) what you did and b) that you know what you are doing. SHOW ALL WORK. Good luck!"
      ],
      "id": "8roKN84QrBTy"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dKDG_NpNoz3o"
      },
      "source": [
        "## Load the normal packages and check we are set for GPU runs"
      ],
      "id": "dKDG_NpNoz3o"
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "looking-possible",
        "outputId": "cba48c23-8476-46ba-ef29-0e716e6f550b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Colab only includes TensorFlow 2.x; %tensorflow_version has no effect.\n"
          ]
        }
      ],
      "source": [
        "# Load our normal packages and run our normal checks for versioning\n",
        "\n",
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
        "assert tf.__version__ >= \"2.0\"\n",
        "\n",
        "if not tf.config.list_physical_devices('GPU'):\n",
        "    print(\"No GPU was detected. LSTMs and CNNs can be very slow without a GPU.\")\n",
        "    if IS_COLAB:\n",
        "        print(\"Go to Runtime > Change runtime and select a GPU hardware accelerator.\")"
      ],
      "id": "looking-possible"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "FQOIu-ppW2N4"
      },
      "source": [
        "## Import packages necessary for the exam tasks in the following section."
      ],
      "id": "FQOIu-ppW2N4"
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "Y050oj2uW0eN"
      },
      "outputs": [],
      "source": [
        "# Common imports\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "\n",
        "import skimage\n",
        "from skimage import color\n",
        "from skimage import io\n",
        "\n",
        "import os\n",
        "\n",
        "import random\n",
        "import time\n",
        "import gdown\n",
        "\n",
        "# load the necessary keras packages\n",
        "from tensorflow.keras import layers\n",
        "from tensorflow.keras import models\n",
        "from tensorflow.keras.utils import to_categorical\n",
        "from tensorflow.keras.callbacks import EarlyStopping\n",
        "\n",
        "\n",
        "# The following may represent additional packages you may find useful for\n",
        "# display or other tasks.\n",
        "\n",
        "import matplotlib as mpl\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns"
      ],
      "id": "Y050oj2uW0eN"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "mysDmSxj35wz"
      },
      "source": [
        "## Here you may choose to import other packages as you prefer/need.\n",
        "\n",
        "This section is optional and intended as a convenient place for your customization."
      ],
      "id": "mysDmSxj35wz"
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "FzIzKUMW4ZV9"
      },
      "outputs": [],
      "source": [
        "# <TO DO - OPTIONAL> Import other packages you find useful\n",
        "\n",
        "from skimage.io import imread\n",
        "from skimage.transform import resize\n",
        "from tensorflow.keras.callbacks import ModelCheckpoint"
      ],
      "id": "FzIzKUMW4ZV9"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "JGP3vNPV3b8Y"
      },
      "source": [
        "## Mount drive containing data\n",
        "\n",
        "Mounting a drive gives you access to a place to store data during your VM session. When you execute the following block, you will get a prompt requesting access to your Google Drive. Once you allow access, you will have a file structure within your VM session. You may look at the resulting directory structure by clicking the folder icon on the left bar in the colab file window."
      ],
      "id": "JGP3vNPV3b8Y"
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u5s4KEwg3dG1",
        "outputId": "1095ec34-8aa5-4822-fc6c-8ba746117d48"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ],
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive', force_remount=True)"
      ],
      "id": "u5s4KEwg3dG1"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MF5ztkRgqZqK"
      },
      "source": [
        "## Loading Data\n",
        "\n",
        "Now that you have a mounted drive (a place to put data), I've made the data you will need for the exam publicly available with the link (i.e., you may access this data from any computer with internet access). The data file as it exists today is 469MB (the original CelebA data files are in excess of 1.4GB).\n",
        "\n",
        "Following the hyperlink in the commented line will bring you to the data file from a web browser. The python coded is how your VM will load the data and make it accessible in your following code."
      ],
      "id": "MF5ztkRgqZqK"
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "id": "4_qQv72S8s5o",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 103
        },
        "outputId": "51d7057c-8de5-46da-8202-70796321cc35"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Downloading...\n",
            "From: https://drive.google.com/uc?id=115Jp99wupi-0Tu8i35wp0X9Hmy6R6S0o\n",
            "To: /content/celeba_greyscale.zip\n",
            "100%|██████████| 469M/469M [00:11<00:00, 41.5MB/s]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'celeba_greyscale.zip'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 8
        }
      ],
      "source": [
        "# https://drive.google.com/file/d/115Jp99wupi-0Tu8i35wp0X9Hmy6R6S0o/view?usp=sharing\n",
        "url = 'https://drive.google.com/uc?id=115Jp99wupi-0Tu8i35wp0X9Hmy6R6S0o'\n",
        "output = 'celeba_greyscale.zip'\n",
        "gdown.download(url, output, quiet=False)"
      ],
      "id": "4_qQv72S8s5o"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bdZ58kuCiEsi"
      },
      "source": [
        "### Unzipping data for use\n",
        "\n",
        "You are about to unzip 202599 files to your Colab Virtual Machine (VM). They will be available to you throughout your session but they will go away once the session is over/deleted.\n",
        "\n",
        "The \"-q\" flag means \"quiet,\" and if you use it, you won't have to watch 202,599 files be unzipped with feedback for each file. However, this command throws a warning and 2 errors, both inconsequential to your project and files. If this disturbs you, you may comment out the first command in favor of the currently commented second command. The second command produces no error warnings, but it does output a confirmation line for each file and takes longer to unpack the lot."
      ],
      "id": "bdZ58kuCiEsi"
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "id": "xdJN_21ABYPP",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "68d251b0-56b3-4483-e613-3db2300c0267"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "warning [./celeba_greyscale.zip]:  76 extra bytes at beginning or within zipfile\n",
            "  (attempting to process anyway)\n",
            "error [./celeba_greyscale.zip]:  reported length of central directory is\n",
            "  -76 bytes too long (Atari STZip zipfile?  J.H.Holm ZIPSPLIT 1.1\n",
            "  zipfile?).  Compensating...\n",
            "error:  expected central file header signature not found (file #202600).\n",
            "  (please check that you have transferred or created the zipfile in the\n",
            "  appropriate BINARY mode and that you have compiled UnZip properly)\n"
          ]
        }
      ],
      "source": [
        "!unzip -q './celeba_greyscale.zip'\n",
        "\n",
        "#!unzip './celeba_greyscale.zip'"
      ],
      "id": "xdJN_21ABYPP"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bacterial-bargain"
      },
      "source": [
        "### Just take a quick look at a file\n",
        "\n",
        "You may change the value of n_img to any number between 1 and 202599 to view a particular picture. Mathplotlib package may be used to show more than a single file, as we've done in classes prior, but I leave that to you to code if you so desire. Note: plt.imshow() will typically show the grayscale image as the green channel of a color image, so you will have to adjust how the image is treated using the mathplotlib image package."
      ],
      "id": "bacterial-bargain"
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "id": "round-implementation",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 537
        },
        "outputId": "9249b953-5798-4f9b-c58f-33beb15d3d1f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "./celeba_greyscale/\n",
            "./celeba_greyscale/000053.jpg\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.image.AxesImage at 0x7f2c90f8ad10>"
            ]
          },
          "metadata": {},
          "execution_count": 10
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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9mmUNmvYl8iZZ55ZmzdvXlHeu3dvraWlpbZo0aJerNWRy9atW2tmVnvggQdqtVqttmPHjtqAAQNqd999d7HPs88+WzOz2tKlS3urmkcEr7zySm3KlCm1++67r/aXf/mXxUtEbdY9X/jCF2rvfve797t93759tXHjxtX+5V/+pfi3HTt21AYNGlT74Q9/eDiqeMRxwQUX1D72sY8l/3bxxRfX5syZU6vVGqvNGlLOeuutt2zZsmU2e/bs4t/69u1rs2fPtqVLl/ZizY5cdu7caWZmI0eONDOzZcuW2e7du5M2nDp1qrW1tf3Zt+G8efPsggsuSNrGTG22P372s5/ZjBkz7MMf/rCNHTvWTjvtNPvud79bbF+zZo11dHQk7dbU1GQzZ878s223s88+25YsWWIrV640M7Mnn3zSHnzwQTv//PPNrLHarCGj+G7bts327t1rzc3Nyb83Nzfbc88910u1OnLZt2+fLViwwM455xw7+eSTzcyso6PDBg4cmOTgNvtTG3Z0dPRCLY8M7rrrLnvsscfskUceqdumNuue1atX2y233GILFy60L37xi/bII4/Y5z73ORs4cKDNnTu3aJvuntc/13a7+uqrraury6ZOnWr9+vWzvXv32g033GBz5swxM2uoNmvIl4gox7x58+zpp5+2Bx98sLerckSzYcMGu+KKK+y+++6zo446qrer0zDs27fPZsyYYV/96lfNzOy0006zp59+2m699VabO3duL9fuyORHP/qR3XHHHXbnnXfatGnT7IknnrAFCxZYS0tLw7VZQ8pZo0ePtn79+tXNiuns7LRx48b1Uq2OTObPn28///nP7de//nWSoWzcuHH21ltv2Y4dO5L9/5zbcNmyZbZ161Z717veZf3797f+/fvbAw88YDfddJP179/fmpub1WbdMH78eDvppJOSfzvxxBNt/fr1ZmZF2+h5/V8+//nP29VXX22XXnqpTZ8+3f7+7//errzySlu0aJGZNVabNeRLZODAgXb66afbkiVLin/bt2+fLVmyxGbNmtWLNTtyqNVqNn/+fPvJT35i999/v7W3tyfbTz/9dBswYEDShitWrLD169f/2bbhueeea0899ZQ98cQTxX8zZsywOXPmFH+rzeo555xz6qaPr1y50iZNmmRmZu3t7TZu3Lik3bq6uuyhhx76s223119/vS5jYL9+/Yrc5g3VZr3t7Fflrrvuqg0aNKj2/e9/v7Z8+fLa5ZdfXhs+fHito6Ojt6t2RPDpT3+61tTUVPvNb35T27JlS/Hf66+/XuzzqU99qtbW1la7//77a48++mht1qxZtVmzZvVirY88/OysWk1t1h0PP/xwrX///rUbbrihtmrVqtodd9xRO/roo2v/+Z//Wexz44031oYPH1776U9/WvvjH/9Yu/DCC4/I6aqHi7lz59YmTJhQTPH98Y9/XBs9enTtqquuKvZplDZr2JdIrVarfetb36q1tbXVBg4cWDvzzDNrf/jDH3q7SkcMZtbtf7fddluxzxtvvFH7zGc+UxsxYkTt6KOPrv3N3/xNbcuWLb1X6SMQvkTUZt3z3//937WTTz65NmjQoNrUqVNr3/nOd5Lt+/btq1177bW15ubm2qBBg2rnnntubcWKFb1U296nq6urdsUVV9Ta2tpqRx11VO2YY46p/eM//mNt165dxT6N0mbKJyKEEKIyDemJCCGEODLQS0QIIURl9BIRQghRGb1EhBBCVEYvESGEEJXRS0QIIURl9BIRQghRGb1EhBBCVEYvESGEEJXRS0QIIURl9BIRQghRmf8HqBhVL+N53g8AAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "# dir_data contains the extracted image files (note)\n",
        "dir_data = \"./celeba_greyscale/\"\n",
        "\n",
        "print(dir_data)\n",
        "\n",
        "n_img = 53\n",
        "fnum = str(n_img).zfill(6)\n",
        "filen = dir_data + fnum + \".jpg\"\n",
        "pic = io.imread(filen)\n",
        "print(filen)\n",
        "io.imshow(pic)"
      ],
      "id": "round-implementation"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XSgN3iqz5YNv"
      },
      "source": [
        "## Load in the \"truth\" data (i.e., the y data set)\n",
        "\n",
        "Truth data is stored in a comma delimited file. Rows represent the image file in order from 1 to 202599. Columns represent an image attribute, where -1 is \"does not possess the attribute\" and 1 is \"does possess the attribute.\" In all cases, the potential classification is binary. The file, as currently posted, has neither row nor column labels. However, they are currently unaltered from order and value as established by the original researchers. The file size is approximately 22.7MB.\n",
        "\n",
        "The labeled data (and indeed several additional worksheets I developed as I worked with the data) may be accessed at https://drive.google.com/file/d/1ntt5eDCAYgpN7yVznYaxBUVZYicgxK4s/view?usp=sharing.\n",
        "\n",
        "Note: The attributes were established by the original researchers and represent only their notion or interpretation of the attribute label. By using this data set, I am ascribing no inherent value or judgment (positive or negative) in whether the picture is said to have an attribute or not. The original researchers classified the images in 40 attributes, many of which may now be considered controversial (e.g., \"attractive\" or \"male\"). Indeed, some are the subject of current social discussion.\n",
        "\n",
        "However, this assignment is in no way intended as a commentary on current social discourse or intended to suggest such discourse is settled or should not procede. Regardless of the attributes ultimately chosen for the assignment, the goal is ANN classification, not social commentary."
      ],
      "id": "XSgN3iqz5YNv"
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "id": "G_kcn3Sa5XEg",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8ea27345-341f-4117-94d0-a9f7fdabb471"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Downloading...\n",
            "From: https://drive.google.com/uc?id=12hZjys_pyl1XG52uYx9LyvZYB0V7-_UC\n",
            "To: /content/celeba_attr.csv\n",
            "100%|██████████| 22.7M/22.7M [00:00<00:00, 61.0MB/s]\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(202599, 40) (40,)\n",
            "[[-1.  1.  1. ... -1. -1.  1.]\n",
            " [-1. -1. -1. ... -1. -1.  1.]\n",
            " [-1. -1. -1. ... -1. -1.  1.]\n",
            " ...\n",
            " [-1. -1. -1. ... -1. -1.  1.]\n",
            " [-1.  1.  1. ... -1. -1.  1.]\n",
            " [-1.  1.  1. ... -1. -1.  1.]]\n"
          ]
        }
      ],
      "source": [
        "# https://drive.google.com/file/d/12hZjys_pyl1XG52uYx9LyvZYB0V7-_UC/view?usp=sharing\n",
        "url = 'https://drive.google.com/uc?id=12hZjys_pyl1XG52uYx9LyvZYB0V7-_UC'\n",
        "output = 'celeba_attr.csv'\n",
        "gdown.download(url, output, quiet=False)\n",
        "\n",
        "Y_full = np.genfromtxt('./celeba_attr.csv',delimiter=',')\n",
        "\n",
        "print(Y_full.shape, Y_full[0,:].shape)\n",
        "print(Y_full)"
      ],
      "id": "G_kcn3Sa5XEg"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5Fn4qjk6uXcG"
      },
      "source": [
        "At this point, you have the entire data set available to you. It still needs to be prepped and partitioned appropriately. The data is already divided into test, validation, and test sets. However, the set is too large to run in the Colab environment due to RAM restrictions. Therefore, part of your task will be to decide on the appropriate sizes for each of the test, validation, and test sets used to train your neural network."
      ],
      "id": "5Fn4qjk6uXcG"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SRrgsptLqk6i"
      },
      "source": [
        "### Prep Y (\"truth\") Data\n",
        "\n",
        "You may decide you need to prep the truth data in a way to make it compatible with our CNN architectures we have been working with. If required, do so in the following code section, clearly documenting your data wrangling/preparation.\n",
        "\n",
        "You do not have to separately segregate the y data into training, validation, and test sets. This will be done simultaneously with the image data segregation. In addition, code provided later picks the correct column for \"gender\" categorization."
      ],
      "id": "SRrgsptLqk6i"
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "id": "gIyowljFuN53",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 52
        },
        "outputId": "2b822617-9de0-48ee-a95b-1a4f1f2eb543"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'\\nAfter examining the supplied documents it does not appear that I will make any changes\\nin this cell. I will have to change the -1 to 0 but will do so in the cell in which the\\ny data is loaded. This operation will reference the dataset sizes.\\n'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 12
        }
      ],
      "source": [
        "# <TO DO> Build data wrangling code here to prepare the truth data for use in your CNN.\n",
        "# Use sufficient comments to let me know what you are doing and why.\n",
        "\n",
        "'''\n",
        "After examining the supplied documents it does not appear that I will make any changes\n",
        "in this cell. I will have to change the -1 to 0 but will do so in the cell in which the\n",
        "y data is loaded. This operation will reference the dataset sizes.\n",
        "'''"
      ],
      "id": "gIyowljFuN53"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "configured-wound"
      },
      "source": [
        "## Establish the size of your test, validation, and test sets.\n",
        "\n",
        "Colab limits the RAM available, so it is doubtful that you will be able to load the entire data set in the colab VM environment. Colab shows you your RAM (and Disk) usage in the upper right corner of the jupyter window.\n",
        "\n",
        "You must establish a balance between the amount of data necessary to get good results vs. the time and memory requirements available. Ultimately, your RAM requirements will consist of training, validation, and test images and their equivalent y-vectors PLUS the CNN model.\n",
        "\n",
        "The next section provides a centralized area for defining the size of your data sets. Make sure your exam submission sufficiently documents your decision process leading to the establishment of your data set sizes."
      ],
      "id": "configured-wound"
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "id": "De45LjPzzmnR"
      },
      "outputs": [],
      "source": [
        "# These variables define the scope of the FULL data set and its partitioning\n",
        "# Your data sets will be subsets of the larger partitions.\n",
        "n_train_full = 162770 # full training set (DON'T CHANGE THIS NUMBER)\n",
        "n_validate_full = 19867 # full validation set (DON'T CHANGE THIS NUMBER)\n",
        "n_test_full = 19962 # full test set (DON'T CHANGE THIS NUMBER)\n",
        "\n",
        "# <TO DO> Select your training, validation, and test set sizes. Effectively doing\n",
        "# so may require some experimentation. Detail your efforts, decisions, reasoning,\n",
        "# and final values in your exam submission.\n",
        "\n",
        "# This section defines your data set sizes. These numbers are yours to change.\n",
        "# Clearly document your data set size selection and process.\n",
        "n_train = 162770    # This represents the number of images you are using in your\n",
        "                    # training set. Change this value.\n",
        "n_validate = 19867  # This represents the number of images you are using in your\n",
        "                    # validation set. Change this value.\n",
        "n_test = 19962      # This represents the number of images you are using in your\n",
        "                    # test set. Change this value.\n"
      ],
      "id": "De45LjPzzmnR"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qyktOZxV1Gzm"
      },
      "source": [
        "### Loading the data\n",
        "\n",
        "You should not need to change anything in this section. You define the data set sizes in the section of code above. At the end of this code block, your data is stored in:\n",
        "\n",
        "x_train, (numpy array of size [n_train, 109, 89])\n",
        "\n",
        "x_validation, (numpy array of size [n_validate, 109, 89])\n",
        "\n",
        "x_test, (numpy array of size [n_test, 109, 89])\n",
        "\n",
        "y_train, (numpy array of size [n_train,])\n",
        "\n",
        "y_validation, (numpy array of size [n_validate,])\n",
        "\n",
        "y_test, (numpy array of size [n_test,])"
      ],
      "id": "qyktOZxV1Gzm"
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "id": "disabled-income",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 137
        },
        "outputId": "6bd1bd33-b69f-43fe-dd84-5e3d67809be0"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'\\n\\n# Load training data\\nx_train = []\\nt0 = time.time()\\nprint(\"Begin loading training data...\")\\nfor i in range(0,n_train):\\n    fnum = str(i+1).zfill(6)\\n    filen = dir_data + fnum + \".jpg\"\\n    x_train.append(io.imread(filen)/255)\\nprint(\"Read in training data (seconds): \", time.time()-t0)\\n\\n# y data\\n# You will have to build code to get the appropriate column data from Y_full\\ny_train = Y_full[:n_train,20]\\n\\nx_train = np.asarray(x_train)\\ny_train = np.asarray(y_train)\\n\\nprint(x_train.shape)\\nprint(y_train.shape)\\n# print(y_train)\\n\\nx_validate = []\\nprint(\"Begin loading validation data...\")\\nt0 = time.time()\\nfor i in range(0, n_validate):\\n    fnum = str(i+n_train_full+1).zfill(6)\\n    filen = dir_data + fnum + \".jpg\"\\n    x_validate.append(io.imread(filen)/255)\\nprint(\"Read in validation data (seconds): \", time.time()-t0)\\n\\n# y data\\n# You will have to build code to get the appropriate column data from Y_full\\ny_validate = Y_full[n_train_full:n_train_full+n_validate,20]\\n\\nx_validate = np.asarray(x_validate)\\ny_validate = np.asarray(y_validate)\\n\\nprint(x_validate.shape)\\nprint(y_validate.shape)\\n\\nx_test = []\\nprint(\"Begin loading test data...\")\\nt0 = time.time()\\nfor i in range(0, n_test):\\n    fnum = str(i+n_train_full+n_validate_full+1).zfill(6)\\n    filen = dir_data + fnum + \".jpg\"\\n    x_test.append(io.imread(filen)/255)\\nprint(\"Read in test data (seconds): \", time.time()-t0)\\n\\n# y data\\n# You will have to build code to get the appropriate column data from Y_full\\ny_test = Y_full[n_train_full+n_validate_full:n_train_full+n_validate_full+n_test,20]\\n\\nx_test = np.asarray(x_test)\\ny_test = np.asarray(y_test)\\n\\nprint(x_test.shape)\\nprint(y_test.shape)\\n\\n'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 14
        }
      ],
      "source": [
        "'''\n",
        "\n",
        "# Load training data\n",
        "x_train = []\n",
        "t0 = time.time()\n",
        "print(\"Begin loading training data...\")\n",
        "for i in range(0,n_train):\n",
        "    fnum = str(i+1).zfill(6)\n",
        "    filen = dir_data + fnum + \".jpg\"\n",
        "    x_train.append(io.imread(filen)/255)\n",
        "print(\"Read in training data (seconds): \", time.time()-t0)\n",
        "\n",
        "# y data\n",
        "# You will have to build code to get the appropriate column data from Y_full\n",
        "y_train = Y_full[:n_train,20]\n",
        "\n",
        "x_train = np.asarray(x_train)\n",
        "y_train = np.asarray(y_train)\n",
        "\n",
        "print(x_train.shape)\n",
        "print(y_train.shape)\n",
        "# print(y_train)\n",
        "\n",
        "x_validate = []\n",
        "print(\"Begin loading validation data...\")\n",
        "t0 = time.time()\n",
        "for i in range(0, n_validate):\n",
        "    fnum = str(i+n_train_full+1).zfill(6)\n",
        "    filen = dir_data + fnum + \".jpg\"\n",
        "    x_validate.append(io.imread(filen)/255)\n",
        "print(\"Read in validation data (seconds): \", time.time()-t0)\n",
        "\n",
        "# y data\n",
        "# You will have to build code to get the appropriate column data from Y_full\n",
        "y_validate = Y_full[n_train_full:n_train_full+n_validate,20]\n",
        "\n",
        "x_validate = np.asarray(x_validate)\n",
        "y_validate = np.asarray(y_validate)\n",
        "\n",
        "print(x_validate.shape)\n",
        "print(y_validate.shape)\n",
        "\n",
        "x_test = []\n",
        "print(\"Begin loading test data...\")\n",
        "t0 = time.time()\n",
        "for i in range(0, n_test):\n",
        "    fnum = str(i+n_train_full+n_validate_full+1).zfill(6)\n",
        "    filen = dir_data + fnum + \".jpg\"\n",
        "    x_test.append(io.imread(filen)/255)\n",
        "print(\"Read in test data (seconds): \", time.time()-t0)\n",
        "\n",
        "# y data\n",
        "# You will have to build code to get the appropriate column data from Y_full\n",
        "y_test = Y_full[n_train_full+n_validate_full:n_train_full+n_validate_full+n_test,20]\n",
        "\n",
        "x_test = np.asarray(x_test)\n",
        "y_test = np.asarray(y_test)\n",
        "\n",
        "print(x_test.shape)\n",
        "print(y_test.shape)\n",
        "\n",
        "'''"
      ],
      "id": "disabled-income"
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "id": "HhhibHoBZ6ni"
      },
      "outputs": [],
      "source": [
        "'''\n",
        "Because I am unwilling to throw away perfectly good data, I have opted to forego\n",
        "specifying a particular size of subsample and to fetch data as I go instead.\n",
        "'''\n",
        "\n",
        "# Collect the Training Data Filenames\n",
        "train_names = []\n",
        "for i in range(0,n_train_full):\n",
        "    fnum = str(i+1).zfill(6)\n",
        "    train_names.append(dir_data + fnum + \".jpg\")\n",
        "\n",
        "# Collect the Validation Data Filenames\n",
        "val_names = []\n",
        "for i in range(0,n_validate_full):\n",
        "    fnum = str(i+1).zfill(6)\n",
        "    val_names.append(dir_data + fnum + \".jpg\")\n",
        "\n",
        "# Collect the Test Data Filenames\n",
        "test_names = []\n",
        "for i in range(0,n_test_full):\n",
        "    fnum = str(i+1).zfill(6)\n",
        "    test_names.append(dir_data + fnum + \".jpg\")\n",
        "\n",
        "# Load the Y labels\n",
        "y_train     = np.asarray( Y_full[:n_train,20] )\n",
        "y_val       = np.asarray( Y_full[n_train_full:n_train_full+n_validate,20] )\n",
        "y_test      = np.asarray( Y_full[n_train_full+n_validate_full:n_train_full+n_validate_full+n_test,20] )\n",
        "\n",
        "# Convert labels -1 to 0\n",
        "y_train[y_train == -1]  = 0,\n",
        "y_val[y_val == -1]      = 0,\n",
        "y_test[y_test == -1]    = 0"
      ],
      "id": "HhhibHoBZ6ni"
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "id": "pek_FSKPOUgi"
      },
      "outputs": [],
      "source": [
        "# Define variables for this section\n",
        "dir_data = \"./celeba_greyscale/\"\n",
        "img_size = [109, 89, 1]\n",
        "batch_size = 32\n",
        "\n",
        "class Data_Generator(keras.utils.Sequence) :\n",
        "    '''\n",
        "    This is the data generator that will be used to pipeline data to the model\n",
        "    '''\n",
        "\n",
        "    def __init__(self, image_filenames, labels, batch_size) :\n",
        "        self.image_filenames = image_filenames\n",
        "        self.labels = labels\n",
        "        self.batch_size = batch_size\n",
        "\n",
        "    # Return length of the iterator\n",
        "    def __len__(self) :\n",
        "        return (np.ceil(len(self.image_filenames) / float(self.batch_size))).astype(np.int)\n",
        "\n",
        "    # Return a single, specific item\n",
        "    def __getitem__(self, idx) :\n",
        "        batch_x = self.image_filenames[idx * self.batch_size : (idx+1) * self.batch_size]\n",
        "        batch_y = self.labels[idx * self.batch_size : (idx+1) * self.batch_size]\n",
        "\n",
        "        return np.array([\n",
        "                resize(imread(str(file_name)), (img_size))\n",
        "                for file_name in batch_x])/255.0, np.array(batch_y)\n",
        "\n",
        "# Define train, val, and test instances of the generators\n",
        "training_batch_generator = Data_Generator(train_names, y_train, batch_size)\n",
        "validation_batch_generator = Data_Generator(val_names, y_val, batch_size)\n",
        "test_generator = Data_Generator(test_names, y_test, 1)"
      ],
      "id": "pek_FSKPOUgi"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dtl2ddrX1_B2"
      },
      "source": [
        "The code below does not require you to change anything. Its intent is to display the dimensions of the images in the training, validation, and test sets, respectively."
      ],
      "id": "dtl2ddrX1_B2"
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "id": "bridal-currency"
      },
      "outputs": [],
      "source": [
        "# print(x_train[0].shape, x_validate[0].shape, x_test[0].shape)"
      ],
      "id": "bridal-currency"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ctRrnSIjRUDQ"
      },
      "source": [
        "## Data wrangling\n",
        "\n",
        "Reshape and retype the data sets, if necessary, to prepare them as inputs for the CNN."
      ],
      "id": "ctRrnSIjRUDQ"
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "id": "6Dfv5kpmRUez"
      },
      "outputs": [],
      "source": [
        "# <TO DO> Include your documented code here for any data wrangling/reshaping you need\n",
        "# for your CNN (both x and y data). Use sufficient comments in your submission to\n",
        "# let me know what you are doing.\n",
        "\n"
      ],
      "id": "6Dfv5kpmRUez"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "VAKsB3J6RUqa"
      },
      "source": [
        "## Build the CNN Model"
      ],
      "id": "VAKsB3J6RUqa"
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "id": "Ol_V1Ss2RUyn",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "10f1dfb8-b9f4-42e8-836a-10d9382d88c3"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Model: \"sequential\"\n",
            "_________________________________________________________________\n",
            " Layer (type)                Output Shape              Param #   \n",
            "=================================================================\n",
            " conv2d (Conv2D)             (None, 105, 85, 64)       1664      \n",
            "                                                                 \n",
            " batch_normalization (BatchN  (None, 105, 85, 64)      256       \n",
            " ormalization)                                                   \n",
            "                                                                 \n",
            " conv2d_1 (Conv2D)           (None, 101, 81, 64)       102464    \n",
            "                                                                 \n",
            " max_pooling2d (MaxPooling2D  (None, 50, 40, 64)       0         \n",
            " )                                                               \n",
            "                                                                 \n",
            " batch_normalization_1 (Batc  (None, 50, 40, 64)       256       \n",
            " hNormalization)                                                 \n",
            "                                                                 \n",
            " dropout (Dropout)           (None, 50, 40, 64)        0         \n",
            "                                                                 \n",
            " conv2d_2 (Conv2D)           (None, 46, 36, 128)       204928    \n",
            "                                                                 \n",
            " batch_normalization_2 (Batc  (None, 46, 36, 128)      512       \n",
            " hNormalization)                                                 \n",
            "                                                                 \n",
            " conv2d_3 (Conv2D)           (None, 42, 32, 128)       409728    \n",
            "                                                                 \n",
            " max_pooling2d_1 (MaxPooling  (None, 21, 16, 128)      0         \n",
            " 2D)                                                             \n",
            "                                                                 \n",
            " batch_normalization_3 (Batc  (None, 21, 16, 128)      512       \n",
            " hNormalization)                                                 \n",
            "                                                                 \n",
            " dropout_1 (Dropout)         (None, 21, 16, 128)       0         \n",
            "                                                                 \n",
            " conv2d_4 (Conv2D)           (None, 17, 12, 256)       819456    \n",
            "                                                                 \n",
            " batch_normalization_4 (Batc  (None, 17, 12, 256)      1024      \n",
            " hNormalization)                                                 \n",
            "                                                                 \n",
            " conv2d_5 (Conv2D)           (None, 13, 8, 256)        1638656   \n",
            "                                                                 \n",
            " max_pooling2d_2 (MaxPooling  (None, 6, 4, 256)        0         \n",
            " 2D)                                                             \n",
            "                                                                 \n",
            " batch_normalization_5 (Batc  (None, 6, 4, 256)        1024      \n",
            " hNormalization)                                                 \n",
            "                                                                 \n",
            " dropout_2 (Dropout)         (None, 6, 4, 256)         0         \n",
            "                                                                 \n",
            " flatten (Flatten)           (None, 6144)              0         \n",
            "                                                                 \n",
            " dense (Dense)               (None, 256)               1573120   \n",
            "                                                                 \n",
            " batch_normalization_6 (Batc  (None, 256)              1024      \n",
            " hNormalization)                                                 \n",
            "                                                                 \n",
            " dropout_3 (Dropout)         (None, 256)               0         \n",
            "                                                                 \n",
            " dense_1 (Dense)             (None, 60)                15420     \n",
            "                                                                 \n",
            " batch_normalization_7 (Batc  (None, 60)               240       \n",
            " hNormalization)                                                 \n",
            "                                                                 \n",
            " dropout_4 (Dropout)         (None, 60)                0         \n",
            "                                                                 \n",
            " dense_2 (Dense)             (None, 1)                 61        \n",
            "                                                                 \n",
            "=================================================================\n",
            "Total params: 4,770,345\n",
            "Trainable params: 4,767,921\n",
            "Non-trainable params: 2,424\n",
            "_________________________________________________________________\n"
          ]
        }
      ],
      "source": [
        "# <TO DO>\n",
        "# Define and document your CNN model (you will compile and train it in the next\n",
        "#    block)\n",
        "#\n",
        "# Considerations: number of layers\n",
        "#                 number and size of filters and padding in each layer\n",
        "#                 step size\n",
        "#                 pooling how often, algorithm used, and size\n",
        "#                 activation function at each level (which and why)\n",
        "#                 overfit considerations and other mitigation steps and where\n",
        "#                    implemented\n",
        "model = models.Sequential()\n",
        "\n",
        "# Insert (and document) model building code here\n",
        "\n",
        "'''\n",
        "Pairs of convolutional layers that are pooled.\n",
        "Dropout to help prevent overfitting.\n",
        "3x3 kernels werre chosen as the base images are fairly small.\n",
        "Small details are important, and shouldn't be lost.\n",
        "However, 5x5 had superior performance.\n",
        "'''\n",
        "\n",
        "model.add(layers.Conv2D(filters = 64, kernel_size = (5,5), activation ='relu',input_shape=(img_size)))\n",
        "model.add(layers.BatchNormalization(axis=3))\n",
        "model.add(layers.Conv2D(filters = 64, kernel_size = (5,5), activation ='relu'))\n",
        "model.add(layers.MaxPooling2D(pool_size=(2,2)))\n",
        "model.add(layers.BatchNormalization(axis=3))\n",
        "model.add(layers.Dropout(0.25))\n",
        "\n",
        "model.add(layers.Conv2D(filters = 128, kernel_size = (5,5), activation ='relu'))\n",
        "model.add(layers.BatchNormalization(axis=3))\n",
        "model.add(layers.Conv2D(filters = 128, kernel_size = (5,5), activation ='relu'))\n",
        "model.add(layers.MaxPooling2D(pool_size=(2,2)))\n",
        "model.add(layers.BatchNormalization(axis=3))\n",
        "model.add(layers.Dropout(0.25))\n",
        "\n",
        "model.add(layers.Conv2D(filters = 256, kernel_size = (5,5), activation ='relu'))\n",
        "model.add(layers.BatchNormalization(axis=3))\n",
        "model.add(layers.Conv2D(filters = 256, kernel_size = (5,5), activation ='relu'))\n",
        "model.add(layers.MaxPooling2D(pool_size=(2,2)))\n",
        "model.add(layers.BatchNormalization(axis=3))\n",
        "model.add(layers.Dropout(0.25))\n",
        "\n",
        "model.add(layers.Flatten())\n",
        "\n",
        "model.add(layers.Dense(256, activation = \"relu\")) #Fully connected layer\n",
        "model.add(layers.BatchNormalization())\n",
        "model.add(layers.Dropout(0.5))\n",
        "\n",
        "model.add(layers.Dense(60, activation = \"relu\")) #Fully connected layer\n",
        "model.add(layers.BatchNormalization())\n",
        "model.add(layers.Dropout(0.5))\n",
        "\n",
        "model.add(layers.Dense(1, activation = \"softmax\")) #Classification layer or output layer\n",
        "\n",
        "model.summary()"
      ],
      "id": "Ol_V1Ss2RUyn"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "pID74A_TTaBN"
      },
      "source": [
        "## Compile and Train the CNN"
      ],
      "id": "pID74A_TTaBN"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zM3vjGXzTaKH",
        "outputId": "eede2420-f7b2-4b35-866c-99cba0d68cde"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/300\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-16-91b4875ee322>:18: DeprecationWarning: `np.int` is a deprecated alias for the builtin `int`. To silence this warning, use `int` by itself. Doing this will not modify any behavior and is safe. When replacing `np.int`, you may wish to use e.g. `np.int64` or `np.int32` to specify the precision. If you wish to review your current use, check the release note link for additional information.\n",
            "Deprecated in NumPy 1.20; for more details and guidance: https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations\n",
            "  return (np.ceil(len(self.image_filenames) / float(self.batch_size))).astype(np.int)\n",
            "/usr/local/lib/python3.10/dist-packages/tensorflow/python/util/dispatch.py:1176: SyntaxWarning: In loss categorical_crossentropy, expected y_pred.shape to be (batch_size, num_classes) with num_classes > 1. Received: y_pred.shape=(None, 1). Consider using 'binary_crossentropy' if you only have 2 classes.\n",
            "  return dispatch_target(*args, **kwargs)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5086/5086 [==============================] - 353s 66ms/step - loss: 0.0000e+00 - accuracy: 0.4194 - val_loss: 0.0000e+00 - val_accuracy: 0.4258\n",
            "Epoch 2/300\n",
            "5086/5086 [==============================] - 333s 65ms/step - loss: 0.0000e+00 - accuracy: 0.4194 - val_loss: 0.0000e+00 - val_accuracy: 0.4258\n",
            "Epoch 3/300\n",
            "2890/5086 [================>.............] - ETA: 2:09 - loss: 0.0000e+00 - accuracy: 0.4191"
          ]
        }
      ],
      "source": [
        "# <TO DO>\n",
        "# Compile the model (and document parameters chosen) using model.compile()\n",
        "\n",
        "model.compile(\n",
        "    # Categorical cross entropy seems to be a generally good choice.\n",
        "    loss=\"categorical_crossentropy\",\n",
        "    # While SGD seems to produce good results and has a greater flexibility for tuning\n",
        "    # ADAM is a robust choice that produces generally good results without too much tuning.\n",
        "    optimizer=\"adam\",\n",
        "    metrics=[\"accuracy\"])\n",
        "\n",
        "# Early stopping is used\n",
        "es = EarlyStopping(\n",
        "    # Validation is used to measure performance against overfitting\n",
        "    monitor='val_loss',\n",
        "    # The goal is to minimize validation loss\n",
        "    mode='min',\n",
        "    # Patients resists settling into a local min\n",
        "    patience = 5,\n",
        "    # Small increases shouldn't reset patience\n",
        "    min_delta=0.01)\n",
        "\n",
        "# Checkpointing to save the best model at any given time\n",
        "mc = ModelCheckpoint('./best_model.h5',\n",
        "    # Best model will be determined by minmum validation loss\n",
        "    monitor='val_loss', mode='min', save_best_only=True)\n",
        "\n",
        "# Initiate the training\n",
        "history = model.fit(training_batch_generator,\n",
        "                    # Number of steps is the how many of the batches make up the total\n",
        "                    steps_per_epoch = int(n_train // batch_size),\n",
        "                    epochs = 300,\n",
        "                    validation_data = validation_batch_generator,\n",
        "                    validation_steps = int(n_validate // batch_size),\n",
        "                    callbacks=[es, mc])\n",
        "\n",
        "# Test the model's accuracy with the test data\n",
        "test_loss, test_acc = model.evaluate(test_generator)\n",
        "\n",
        "print('Test accuracy:', test_acc)"
      ],
      "id": "zM3vjGXzTaKH"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zDy1EgoO0vwL"
      },
      "source": [
        "### Plot the (typical) metrics\n",
        "\n",
        "The graph is a basic representation of the training results. You may devise more sophisticated representations as you determine appropriate. At a minimum, discuss the graph and its implications to your model's presumed accuracy and robustness."
      ],
      "id": "zDy1EgoO0vwL"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "PXZp1bqt0wCJ"
      },
      "outputs": [],
      "source": [
        "# <TO DO> Develop your displays used to evaluate your model. The included code provides\n",
        "# a minimum graphic display for possible metrics.\n",
        "pd.DataFrame(history.history).plot(figsize=(8,5))\n",
        "plt.grid(True)\n",
        "plt.gca().set_ylim(0,1)\n",
        "plt.show()"
      ],
      "id": "PXZp1bqt0wCJ"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "iGPnOBMdBMPf"
      },
      "source": [
        "We are going to use your model to evaluate the image in file 200000.jpg\n",
        "\n",
        "You do not have to change the code in the next block. It will just display the image your model will evaluate."
      ],
      "id": "iGPnOBMdBMPf"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Rh1yrSFEWcnp"
      },
      "outputs": [],
      "source": [
        "io.imshow(io.imread('./celeba_greyscale/200000.jpg'))"
      ],
      "id": "Rh1yrSFEWcnp"
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2axqdj3KBmuH"
      },
      "source": [
        "### Evaluate a Novel Data Point\n",
        "\n",
        "Modify the code in the following block to evaluate the indicated image with your compiled model and interpret the results."
      ],
      "id": "2axqdj3KBmuH"
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "TkTUVV7xm_6d"
      },
      "outputs": [],
      "source": [
        "# <TO DO> Modify the code below to evaluate image 200000.jpg\n",
        "x_new = io.imread('./celeba_greyscale/200000.jpg',as_gray=True)\n",
        "\n",
        "# Reshape the array if necessary\n",
        "# x_new = x_new.reshape()\n",
        "# print(x_new.shape)\n",
        "\n",
        "model.predict(x_new)\n",
        "\n",
        "# What does the output from model.predict(x_new) indicate. Discuss the values\n",
        "# output and what they represent."
      ],
      "id": "TkTUVV7xm_6d"
    }
  ],
  "metadata": {
    "accelerator": "GPU",
    "colab": {
      "machine_shape": "hm",
      "provenance": [],
      "gpuType": "A100"
    },
    "kernelspec": {
      "display_name": "Python 3",
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
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}