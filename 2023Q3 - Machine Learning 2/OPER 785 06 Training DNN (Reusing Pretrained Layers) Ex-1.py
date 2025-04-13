{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Reusing_Pretrained_Layers_Example1.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "import tensorflow as tf\n",
        "from tensorflow import keras\n",
        "import numpy as np"
      ],
      "metadata": {
        "id": "YCra9DxbVOub"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "zEQWYXTLVOwy"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Load the MNIST dataset from Keras\n",
        "## Split into training and validation sets"
      ],
      "metadata": {
        "id": "y4xMqH3gVukv"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "kynT1NNjVN63",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a4d5d751-998e-4ea5-d34c-7e7f65de6417"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/train-labels-idx1-ubyte.gz\n",
            "32768/29515 [=================================] - 0s 0us/step\n",
            "40960/29515 [=========================================] - 0s 0us/step\n",
            "Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/train-images-idx3-ubyte.gz\n",
            "26427392/26421880 [==============================] - 0s 0us/step\n",
            "26435584/26421880 [==============================] - 0s 0us/step\n",
            "Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/t10k-labels-idx1-ubyte.gz\n",
            "16384/5148 [===============================================================================================] - 0s 0us/step\n",
            "Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/t10k-images-idx3-ubyte.gz\n",
            "4423680/4422102 [==============================] - 0s 0us/step\n",
            "4431872/4422102 [==============================] - 0s 0us/step\n"
          ]
        }
      ],
      "source": [
        "(X_train_full, y_train_full), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()\n",
        "X_train_full = X_train_full / 255.0\n",
        "X_test = X_test / 255.0\n",
        "X_valid, X_train = X_train_full[:5000], X_train_full[5000:]\n",
        "y_valid, y_train = y_train_full[:5000], y_train_full[5000:]"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Let's split the fashion MNIST training set in two:\n",
        "* `X_train_A`: all images of all items except for sandals and shirts (classes 5 and 6).\n",
        "* `X_train_B`: a much smaller training set of just the first 200 images of sandals or shirts.\n",
        "\n",
        "The validation set and the test set are also split this way, but without restricting the number of images.\n",
        "\n",
        "We will train a model on set A (classification task with 8 classes), and try to reuse it to tackle set B (binary classification). We hope to transfer a little bit of knowledge from task A to task B, since classes in set A (sneakers, ankle boots, coats, t-shirts, etc.) are somewhat similar to classes in set B (sandals and shirts). However, since we are using `Dense` layers, only patterns that occur at the same location can be reused (in contrast, convolutional layers will transfer much better, since learned patterns can be detected anywhere on the image, as we will see in the CNN chapter)."
      ],
      "metadata": {
        "id": "7u86rgzAWJG8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def split_dataset(X, y):\n",
        "    y_5_or_6 = (y == 5) | (y == 6) # sandals or shirts\n",
        "    y_A = y[~y_5_or_6]\n",
        "    y_A[y_A > 6] -= 2 # class indices 7, 8, 9 should be moved to 5, 6, 7\n",
        "    y_B = (y[y_5_or_6] == 6).astype(np.float32) # binary classification task: is it a shirt (class 6)?\n",
        "    return ((X[~y_5_or_6], y_A),\n",
        "            (X[y_5_or_6], y_B))\n",
        "\n",
        "(X_train_A, y_train_A), (X_train_B, y_train_B) = split_dataset(X_train, y_train)\n",
        "(X_valid_A, y_valid_A), (X_valid_B, y_valid_B) = split_dataset(X_valid, y_valid)\n",
        "(X_test_A, y_test_A), (X_test_B, y_test_B) = split_dataset(X_test, y_test)\n",
        "X_train_B = X_train_B[:200]\n",
        "y_train_B = y_train_B[:200]"
      ],
      "metadata": {
        "id": "1FfqcMN3Vb7u"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "tf.random.set_seed(42)\n",
        "np.random.seed(42)"
      ],
      "metadata": {
        "id": "Sr0UQfvyWIRH"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model_A = keras.models.Sequential()\n",
        "# first flatten input data\n",
        "model_A.add(keras.layers.Flatten(input_shape=[28, 28]))\n",
        "# add five dense layers of various neuron amounts\n",
        "for n_hidden in (300, 100, 50, 50, 50):\n",
        "    model_A.add(keras.layers.Dense(n_hidden, activation=\"selu\"))\n",
        "model_A.add(keras.layers.Dense(8, activation=\"softmax\"))"
      ],
      "metadata": {
        "id": "lp3mqAvpWbmg"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model_A.compile(loss=\"sparse_categorical_crossentropy\",\n",
        "                optimizer=keras.optimizers.SGD(learning_rate=1e-3),\n",
        "                metrics=[\"accuracy\"])"
      ],
      "metadata": {
        "id": "Y3B0Ej_aWcXE"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "history = model_A.fit(X_train_A, y_train_A, epochs=20,\n",
        "                    validation_data=(X_valid_A, y_valid_A))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7qThpVn9WcZM",
        "outputId": "ad6710bf-0757-448e-9c7a-14b32727651a"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/20\n",
            "1375/1375 [==============================] - 6s 4ms/step - loss: 0.5803 - accuracy: 0.8143 - val_loss: 0.3851 - val_accuracy: 0.8677\n",
            "Epoch 2/20\n",
            "1375/1375 [==============================] - 5s 4ms/step - loss: 0.3580 - accuracy: 0.8774 - val_loss: 0.3227 - val_accuracy: 0.8916\n",
            "Epoch 3/20\n",
            "1375/1375 [==============================] - 5s 3ms/step - loss: 0.3210 - accuracy: 0.8899 - val_loss: 0.2995 - val_accuracy: 0.8994\n",
            "Epoch 4/20\n",
            "1375/1375 [==============================] - 5s 4ms/step - loss: 0.3016 - accuracy: 0.8969 - val_loss: 0.2868 - val_accuracy: 0.9036\n",
            "Epoch 5/20\n",
            "1375/1375 [==============================] - 5s 3ms/step - loss: 0.2882 - accuracy: 0.9017 - val_loss: 0.2767 - val_accuracy: 0.9071\n",
            "Epoch 6/20\n",
            "1375/1375 [==============================] - 5s 4ms/step - loss: 0.2780 - accuracy: 0.9039 - val_loss: 0.2716 - val_accuracy: 0.9108\n",
            "Epoch 7/20\n",
            "1375/1375 [==============================] - 5s 3ms/step - loss: 0.2697 - accuracy: 0.9077 - val_loss: 0.2708 - val_accuracy: 0.9108\n",
            "Epoch 8/20\n",
            "1375/1375 [==============================] - 5s 3ms/step - loss: 0.2627 - accuracy: 0.9104 - val_loss: 0.2678 - val_accuracy: 0.9131\n",
            "Epoch 9/20\n",
            "1375/1375 [==============================] - 5s 3ms/step - loss: 0.2574 - accuracy: 0.9109 - val_loss: 0.2576 - val_accuracy: 0.9145\n",
            "Epoch 10/20\n",
            "1375/1375 [==============================] - 5s 3ms/step - loss: 0.2524 - accuracy: 0.9136 - val_loss: 0.2558 - val_accuracy: 0.9158\n",
            "Epoch 11/20\n",
            "1375/1375 [==============================] - 5s 3ms/step - loss: 0.2478 - accuracy: 0.9147 - val_loss: 0.2515 - val_accuracy: 0.9163\n",
            "Epoch 12/20\n",
            "1375/1375 [==============================] - 5s 3ms/step - loss: 0.2435 - accuracy: 0.9162 - val_loss: 0.2532 - val_accuracy: 0.9148\n",
            "Epoch 13/20\n",
            "1375/1375 [==============================] - 5s 4ms/step - loss: 0.2401 - accuracy: 0.9181 - val_loss: 0.2496 - val_accuracy: 0.9148\n",
            "Epoch 14/20\n",
            "1375/1375 [==============================] - 5s 4ms/step - loss: 0.2368 - accuracy: 0.9190 - val_loss: 0.2446 - val_accuracy: 0.9180\n",
            "Epoch 15/20\n",
            "1375/1375 [==============================] - 5s 4ms/step - loss: 0.2338 - accuracy: 0.9205 - val_loss: 0.2549 - val_accuracy: 0.9136\n",
            "Epoch 16/20\n",
            "1375/1375 [==============================] - 5s 4ms/step - loss: 0.2307 - accuracy: 0.9211 - val_loss: 0.2448 - val_accuracy: 0.9175\n",
            "Epoch 17/20\n",
            "1375/1375 [==============================] - 5s 3ms/step - loss: 0.2278 - accuracy: 0.9222 - val_loss: 0.2549 - val_accuracy: 0.9153\n",
            "Epoch 18/20\n",
            "1375/1375 [==============================] - 5s 4ms/step - loss: 0.2251 - accuracy: 0.9231 - val_loss: 0.2486 - val_accuracy: 0.9113\n",
            "Epoch 19/20\n",
            "1375/1375 [==============================] - 5s 4ms/step - loss: 0.2225 - accuracy: 0.9234 - val_loss: 0.2400 - val_accuracy: 0.9180\n",
            "Epoch 20/20\n",
            "1375/1375 [==============================] - 5s 3ms/step - loss: 0.2202 - accuracy: 0.9247 - val_loss: 0.2435 - val_accuracy: 0.9150\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model_A.save(\"my_model_A.h5\")"
      ],
      "metadata": {
        "id": "XV1AxrS_Wcbf"
      },
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model_B = keras.models.Sequential()\n",
        "model_B.add(keras.layers.Flatten(input_shape=[28, 28]))\n",
        "for n_hidden in (300, 100, 50, 50, 50):\n",
        "    model_B.add(keras.layers.Dense(n_hidden, activation=\"selu\"))\n",
        "model_B.add(keras.layers.Dense(1, activation=\"sigmoid\"))"
      ],
      "metadata": {
        "id": "HKcZXVekWosK"
      },
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model_B.compile(loss=\"binary_crossentropy\",\n",
        "                optimizer=keras.optimizers.SGD(learning_rate=1e-3),\n",
        "                metrics=[\"accuracy\"])"
      ],
      "metadata": {
        "id": "Qyu9KIbWWou2"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "history = model_B.fit(X_train_B, y_train_B, epochs=20,\n",
        "                      validation_data=(X_valid_B, y_valid_B))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8oAzEYuOWoxO",
        "outputId": "b9c279ae-5491-49a9-df37-583ba6f5be46"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/20\n",
            "7/7 [==============================] - 1s 40ms/step - loss: 0.5486 - accuracy: 0.7300 - val_loss: 0.4821 - val_accuracy: 0.8012\n",
            "Epoch 2/20\n",
            "7/7 [==============================] - 0s 17ms/step - loss: 0.3941 - accuracy: 0.8550 - val_loss: 0.3780 - val_accuracy: 0.8682\n",
            "Epoch 3/20\n",
            "7/7 [==============================] - 0s 16ms/step - loss: 0.3016 - accuracy: 0.9150 - val_loss: 0.3135 - val_accuracy: 0.9087\n",
            "Epoch 4/20\n",
            "7/7 [==============================] - 0s 15ms/step - loss: 0.2448 - accuracy: 0.9600 - val_loss: 0.2684 - val_accuracy: 0.9260\n",
            "Epoch 5/20\n",
            "7/7 [==============================] - 0s 16ms/step - loss: 0.2043 - accuracy: 0.9750 - val_loss: 0.2376 - val_accuracy: 0.9391\n",
            "Epoch 6/20\n",
            "7/7 [==============================] - 0s 17ms/step - loss: 0.1761 - accuracy: 0.9800 - val_loss: 0.2146 - val_accuracy: 0.9483\n",
            "Epoch 7/20\n",
            "7/7 [==============================] - 0s 15ms/step - loss: 0.1553 - accuracy: 0.9800 - val_loss: 0.1972 - val_accuracy: 0.9533\n",
            "Epoch 8/20\n",
            "7/7 [==============================] - 0s 19ms/step - loss: 0.1390 - accuracy: 0.9900 - val_loss: 0.1827 - val_accuracy: 0.9564\n",
            "Epoch 9/20\n",
            "7/7 [==============================] - 0s 15ms/step - loss: 0.1256 - accuracy: 0.9900 - val_loss: 0.1685 - val_accuracy: 0.9635\n",
            "Epoch 10/20\n",
            "7/7 [==============================] - 0s 14ms/step - loss: 0.1136 - accuracy: 0.9900 - val_loss: 0.1578 - val_accuracy: 0.9655\n",
            "Epoch 11/20\n",
            "7/7 [==============================] - 0s 15ms/step - loss: 0.1040 - accuracy: 0.9950 - val_loss: 0.1490 - val_accuracy: 0.9686\n",
            "Epoch 12/20\n",
            "7/7 [==============================] - 0s 16ms/step - loss: 0.0960 - accuracy: 0.9950 - val_loss: 0.1416 - val_accuracy: 0.9686\n",
            "Epoch 13/20\n",
            "7/7 [==============================] - 0s 15ms/step - loss: 0.0892 - accuracy: 1.0000 - val_loss: 0.1351 - val_accuracy: 0.9686\n",
            "Epoch 14/20\n",
            "7/7 [==============================] - 0s 18ms/step - loss: 0.0834 - accuracy: 1.0000 - val_loss: 0.1289 - val_accuracy: 0.9696\n",
            "Epoch 15/20\n",
            "7/7 [==============================] - 0s 15ms/step - loss: 0.0778 - accuracy: 1.0000 - val_loss: 0.1236 - val_accuracy: 0.9716\n",
            "Epoch 16/20\n",
            "7/7 [==============================] - 0s 17ms/step - loss: 0.0733 - accuracy: 1.0000 - val_loss: 0.1191 - val_accuracy: 0.9726\n",
            "Epoch 17/20\n",
            "7/7 [==============================] - 0s 16ms/step - loss: 0.0692 - accuracy: 1.0000 - val_loss: 0.1151 - val_accuracy: 0.9736\n",
            "Epoch 18/20\n",
            "7/7 [==============================] - 0s 16ms/step - loss: 0.0656 - accuracy: 1.0000 - val_loss: 0.1112 - val_accuracy: 0.9757\n",
            "Epoch 19/20\n",
            "7/7 [==============================] - 0s 15ms/step - loss: 0.0622 - accuracy: 1.0000 - val_loss: 0.1075 - val_accuracy: 0.9777\n",
            "Epoch 20/20\n",
            "7/7 [==============================] - 0s 16ms/step - loss: 0.0590 - accuracy: 1.0000 - val_loss: 0.1046 - val_accuracy: 0.9767\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model_B.summary()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bA0y2besWoz1",
        "outputId": "3144c7d7-fa8e-4269-87e8-e026b74b9151"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Model: \"sequential_2\"\n",
            "_________________________________________________________________\n",
            " Layer (type)                Output Shape              Param #   \n",
            "=================================================================\n",
            " flatten_2 (Flatten)         (None, 784)               0         \n",
            "                                                                 \n",
            " dense_12 (Dense)            (None, 300)               235500    \n",
            "                                                                 \n",
            " dense_13 (Dense)            (None, 100)               30100     \n",
            "                                                                 \n",
            " dense_14 (Dense)            (None, 50)                5050      \n",
            "                                                                 \n",
            " dense_15 (Dense)            (None, 50)                2550      \n",
            "                                                                 \n",
            " dense_16 (Dense)            (None, 50)                2550      \n",
            "                                                                 \n",
            " dense_17 (Dense)            (None, 1)                 51        \n",
            "                                                                 \n",
            "=================================================================\n",
            "Total params: 275,801\n",
            "Trainable params: 275,801\n",
            "Non-trainable params: 0\n",
            "_________________________________________________________________\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model_A = keras.models.load_model(\"my_model_A.h5\")\n",
        "\n",
        "# removing last layer of model A\n",
        "model_B_on_A = keras.models.Sequential(model_A.layers[:-1])\n",
        "# adding new layer\n",
        "model_B_on_A.add(keras.layers.Dense(1, activation=\"sigmoid\"))"
      ],
      "metadata": {
        "id": "XA-_BxyrWwyt"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Because of how Python functions work, we actually need to \"clone\" Model A before we reuse its layers. "
      ],
      "metadata": {
        "id": "TA-JAz8RNZIO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "model_A_clone = keras.models.clone_model(model_A)\n",
        "model_A_clone.set_weights(model_A.get_weights())\n",
        "model_B_on_A = keras.models.Sequential(model_A_clone.layers[:-1])\n",
        "model_B_on_A.add(keras.layers.Dense(1, activation=\"sigmoid\"))"
      ],
      "metadata": {
        "id": "TyKFmI-mWw1X"
      },
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Now, we need to \"freeze\" the layers we are reusing, by setting their \"trainable\" attribute to False and compiling the model:"
      ],
      "metadata": {
        "id": "ZOkX_GT1ORlj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for layer in model_B_on_A.layers[:-1]:\n",
        "    layer.trainable = False\n",
        "\n",
        "model_B_on_A.compile(loss=\"binary_crossentropy\",\n",
        "                     optimizer=keras.optimizers.SGD(learning_rate=1e-3),\n",
        "                     metrics=[\"accuracy\"])"
      ],
      "metadata": {
        "id": "osKLthZQWw3w"
      },
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "id": "lBjptLCsWOjU",
        "outputId": "ef5da095-f24a-44cb-c69e-410f0e2c83b3",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/4\n",
            "7/7 [==============================] - 1s 40ms/step - loss: 1.1684 - accuracy: 0.3350 - val_loss: 1.0884 - val_accuracy: 0.3813\n",
            "Epoch 2/4\n",
            "7/7 [==============================] - 0s 14ms/step - loss: 1.0449 - accuracy: 0.3700 - val_loss: 0.9753 - val_accuracy: 0.4219\n",
            "Epoch 3/4\n",
            "7/7 [==============================] - 0s 14ms/step - loss: 0.9320 - accuracy: 0.4400 - val_loss: 0.8765 - val_accuracy: 0.4746\n",
            "Epoch 4/4\n",
            "7/7 [==============================] - 0s 16ms/step - loss: 0.8338 - accuracy: 0.5000 - val_loss: 0.7953 - val_accuracy: 0.5304\n",
            "Epoch 1/16\n",
            "7/7 [==============================] - 1s 40ms/step - loss: 0.6108 - accuracy: 0.6450 - val_loss: 0.4404 - val_accuracy: 0.8032\n",
            "Epoch 2/16\n",
            "7/7 [==============================] - 0s 17ms/step - loss: 0.3438 - accuracy: 0.8850 - val_loss: 0.2912 - val_accuracy: 0.9209\n",
            "Epoch 3/16\n",
            "7/7 [==============================] - 0s 17ms/step - loss: 0.2290 - accuracy: 0.9650 - val_loss: 0.2203 - val_accuracy: 0.9523\n",
            "Epoch 4/16\n",
            "7/7 [==============================] - 0s 16ms/step - loss: 0.1724 - accuracy: 0.9800 - val_loss: 0.1817 - val_accuracy: 0.9625\n",
            "Epoch 5/16\n",
            "7/7 [==============================] - 0s 14ms/step - loss: 0.1405 - accuracy: 0.9900 - val_loss: 0.1562 - val_accuracy: 0.9716\n",
            "Epoch 6/16\n",
            "7/7 [==============================] - 0s 17ms/step - loss: 0.1191 - accuracy: 1.0000 - val_loss: 0.1380 - val_accuracy: 0.9767\n",
            "Epoch 7/16\n",
            "7/7 [==============================] - 0s 15ms/step - loss: 0.1039 - accuracy: 1.0000 - val_loss: 0.1258 - val_accuracy: 0.9787\n",
            "Epoch 8/16\n",
            "7/7 [==============================] - 0s 14ms/step - loss: 0.0929 - accuracy: 1.0000 - val_loss: 0.1151 - val_accuracy: 0.9828\n",
            "Epoch 9/16\n",
            "7/7 [==============================] - 0s 18ms/step - loss: 0.0839 - accuracy: 1.0000 - val_loss: 0.1061 - val_accuracy: 0.9868\n",
            "Epoch 10/16\n",
            "7/7 [==============================] - 0s 17ms/step - loss: 0.0764 - accuracy: 1.0000 - val_loss: 0.0986 - val_accuracy: 0.9868\n",
            "Epoch 11/16\n",
            "7/7 [==============================] - 0s 15ms/step - loss: 0.0701 - accuracy: 1.0000 - val_loss: 0.0926 - val_accuracy: 0.9868\n",
            "Epoch 12/16\n",
            "7/7 [==============================] - 0s 14ms/step - loss: 0.0647 - accuracy: 1.0000 - val_loss: 0.0870 - val_accuracy: 0.9868\n",
            "Epoch 13/16\n",
            "7/7 [==============================] - 0s 19ms/step - loss: 0.0599 - accuracy: 1.0000 - val_loss: 0.0826 - val_accuracy: 0.9868\n",
            "Epoch 14/16\n",
            "7/7 [==============================] - 0s 15ms/step - loss: 0.0561 - accuracy: 1.0000 - val_loss: 0.0790 - val_accuracy: 0.9868\n",
            "Epoch 15/16\n",
            "7/7 [==============================] - 0s 14ms/step - loss: 0.0528 - accuracy: 1.0000 - val_loss: 0.0753 - val_accuracy: 0.9868\n",
            "Epoch 16/16\n",
            "7/7 [==============================] - 0s 16ms/step - loss: 0.0499 - accuracy: 1.0000 - val_loss: 0.0724 - val_accuracy: 0.9868\n"
          ]
        }
      ],
      "source": [
        "history = model_B_on_A.fit(X_train_B, y_train_B, epochs=4,\n",
        "                           validation_data=(X_valid_B, y_valid_B))\n",
        "\n",
        "for layer in model_B_on_A.layers[:-1]:\n",
        "    layer.trainable = True\n",
        "\n",
        "model_B_on_A.compile(loss=\"binary_crossentropy\",\n",
        "                     optimizer=keras.optimizers.SGD(learning_rate=1e-3),\n",
        "                     metrics=[\"accuracy\"])\n",
        "history = model_B_on_A.fit(X_train_B, y_train_B, epochs=16,\n",
        "                           validation_data=(X_valid_B, y_valid_B))"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model_B.evaluate(X_test_B, y_test_B)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eS6qLqArW6pS",
        "outputId": "d4c345ac-20c5-4e02-e5e9-5a37f7e50ccd"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "63/63 [==============================] - 0s 3ms/step - loss: 0.0931 - accuracy: 0.9835\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[0.09306484460830688, 0.9835000038146973]"
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model_B_on_A.evaluate(X_test_B, y_test_B)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jrS4dXbvXB3B",
        "outputId": "3874b2af-d29c-4d0b-8836-8a69facf0b2c"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "63/63 [==============================] - 0s 2ms/step - loss: 0.0666 - accuracy: 0.9910\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[0.06663096696138382, 0.9909999966621399]"
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Great! We got quite a bit of transfer: the error rate dropped by a factor of 4.9"
      ],
      "metadata": {
        "id": "S5O59nYMXJz6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "(100 - 97.05) / (100 - 99.40)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1TYPwB6vW6rQ",
        "outputId": "685c38f9-8d4a-44b0-8dac-5688897e9cc0"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "4.916666666666718"
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Conclusions\n",
        "Wow! It looks like transfer learning is great! Well it is, but unfortunately, some cheating has gone one here. The author already knows which form of tranfer learning will work best. Therefore, we don't know without some trial-and-error which layers we ought to keep."
      ],
      "metadata": {
        "id": "QrNHha2FOhVR"
      }
    }
  ]
}