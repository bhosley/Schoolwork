{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Example Artificial Neural Network (from scratch)\n",
    "Follows example from Polycode channel on YouTube.\n",
    "\n",
    "Video links:\n",
    "https://www.youtube.com/watch?v=kft1AJ9WVDk and \n",
    "https://www.youtube.com/watch?v=Py4xvZx-A1E\n",
    "\n",
    "The code may be downloaded from Canvas, and you may have to move the files or adjust the path "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import the appropriate packages\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Define a neural network class. The class will have a sigmoid activation function, its derivative, \n",
    "feedforward and backpropogation steps, and a single output.\n",
    " \n",
    "As a single layer network, the network is incapable of calculating complex logical operators. Multiple\n",
    "layers would be required for something as simple as a logical \"XOR\" function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class NeuralNetwork:\n",
    "    def __init__(self, x, y):\n",
    "        self.x              = np.array(x)\n",
    "        self.y              = np.array(y)\n",
    "        \n",
    "        # Set weights\n",
    "        self.weights        = 2 * np.random.random((x.shape[1],y.shape[1])) - 1\n",
    "\n",
    "        self.error          = np.zeros(self.y.shape)\n",
    "        self.output         = np.zeros(self.y.shape)\n",
    "        self.adjustments    = np.zeros(self.y.shape)\n",
    "\n",
    "    def sigmoid(self,x):\n",
    "        return 1 / (1 + np.exp(-x))\n",
    "\n",
    "    def sigmoid_derivative(self,x):\n",
    "        return x* (1-x)\n",
    "\n",
    "    def train(self, i):\n",
    "        for iteration in range (i):\n",
    "            # Feedforward\n",
    "            self.output = self.sigmoid(np.dot(self.x, self.weights))\n",
    "    \n",
    "            # Back propogation\n",
    "            self.error = self.y - self.output\n",
    "            self.adjustments = self.error * self.sigmoid_derivative(self.output)\n",
    "            self.weights += np.dot(self.x.T, self.adjustments)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Once the class is defined, we can instantiate it through defining new variables. Let's consider a case of three\n",
    "binary input variables with a single binary output. The data can be seen to represent (x1 \"AND\" x3)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = np.array([[0, 0, 1],[1, 1, 1],[1, 0, 1],[0, 1, 1]])\n",
    "y = np.array([[0],[1],[1],[0]])\n",
    "print(x.shape, y.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Once we have the inputs and outputs, we can instantiate an instance of the NeuralNetwork object."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ann = NeuralNetwork(x,y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We train the neural network for a specified number of epochs and show the outputs after training. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ann.train(100)\n",
    "    \n",
    "print(ann.output)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note, the outputs from the trained network are \"close to\" the desired output (training values). More training epochs\n",
    "would get us closer to the desired values [0, 1, 1, 0]. So let's try some additional training epochs (Note: since the\n",
    "weights are not reset, we can just call the training function again)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ann.train(1400) #This will give us 1500 replications\n",
    "print(ann.output)\n",
    "print(ann.weights)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's define a new data set representing the logical \"XOR\" function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "x1 = np.array([[0,0],[0,1],[1,0],[1,1]])\n",
    "y1 = np.array([[0],[1],[1],[0]])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can define a new ANN based on the new data, train it, and look at the output."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ann1 = NeuralNetwork(x1,y1)\n",
    "ann1.train(100)\n",
    "print(ann1.output)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Additional training will not help us out. The single layer ANN cannot describe the nonlinear XOR function "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ann1.train(1400)\n",
    "print(ann1.output)"
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
