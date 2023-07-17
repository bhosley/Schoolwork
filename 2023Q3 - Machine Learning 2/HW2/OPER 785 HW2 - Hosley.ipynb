{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Homework 2\n",
    "## Hosley, Brandon\n",
    "## OPER 785\n",
    "\n",
    "### Task:\n",
    "Expand the example such that the network is capable of solving the XOR operator (remember: the XOR operator evaluates two binary inputs and returns a 0 when the inputs are equal and a 1 when the inputs are different). It should be sufficient to add an additional layer of TLUs to solve this problem, but there is the problem of 2 sets of weights to account for in your back propagation.\n",
    "\n",
    "Deliverables: Well documented code and output (Jupyter Notebook is sufficient for both, but you may use any language, interpreter, or compiler). Important notations include beginning weights, final weights, and dimensionality of arrays."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Example Artificial Neural Network (from Class)\n",
    "Follows example from Polycode channel on YouTube."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import the appropriate packages\n",
    "import numpy as np"
   ]
  },
  {
   "attachments": {},
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
   "execution_count": 2,
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
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Once the class is defined, we can instantiate it through defining new variables. Let's consider a case of three\n",
    "binary input variables with a single binary output. The data can be seen to represent (x1 \"AND\" x3)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(4, 3) (4, 1)\n"
     ]
    }
   ],
   "source": [
    "x = np.array([[0, 0, 1],[1, 1, 1],[1, 0, 1],[0, 1, 1]])\n",
    "y = np.array([[0],[1],[1],[0]])\n",
    "print(x.shape, y.shape)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Once we have the inputs and outputs, we can instantiate an instance of the NeuralNetwork object."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "ann = NeuralNetwork(x,y)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We train the neural network for a specified number of epochs and show the outputs after training. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.10993431]\n",
      " [0.91093839]\n",
      " [0.92696043]\n",
      " [0.09053048]]\n"
     ]
    }
   ],
   "source": [
    "ann.train(100)\n",
    "    \n",
    "print(ann.output)"
   ]
  },
  {
   "attachments": {},
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
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.02568097]\n",
      " [0.97910164]\n",
      " [0.9830782 ]\n",
      " [0.02081371]]\n",
      "[[ 7.6987835 ]\n",
      " [-0.21511781]\n",
      " [-3.63634624]]\n"
     ]
    }
   ],
   "source": [
    "ann.train(1400) #This will give us 1500 replications\n",
    "print(ann.output)\n",
    "print(ann.weights)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's define a new data set representing the logical \"XOR\" function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "x1 = np.array([[0,0],[0,1],[1,0],[1,1]])\n",
    "y1 = np.array([[0],[1],[1],[0]])"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can define a new ANN based on the new data, train it, and look at the output."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.5       ]\n",
      " [0.50011473]\n",
      " [0.49988522]\n",
      " [0.49999995]]\n"
     ]
    }
   ],
   "source": [
    "ann1 = NeuralNetwork(x1,y1)\n",
    "ann1.train(100)\n",
    "print(ann1.output)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Additional training will not help us out. The single layer ANN cannot describe the nonlinear XOR function "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.5]\n",
      " [0.5]\n",
      " [0.5]\n",
      " [0.5]]\n"
     ]
    }
   ],
   "source": [
    "ann1.train(1400)\n",
    "print(ann1.output)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Begin Homework Portion"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "class DeepNeuralNetwork(NeuralNetwork):\n",
    "    def __init__(self, x, y):\n",
    "        super().__init__(x, y)\n",
    "\n",
    "        # Set weights\n",
    "        self.weights_hidden     = np.random.uniform(size=(x.shape[1], 2))\n",
    "        self.bias_hidden        = np.random.uniform(size=(1, 2))\n",
    "        self.weights_output     = np.random.uniform(size=(2, y.shape[1]))\n",
    "        self.bias_output        = np.random.uniform(size=(1, 1))\n",
    "        self.output             = np.zeros(self.y.shape)\n",
    "\n",
    "    def train(self, i, lr):\n",
    "        for _ in range (i):\n",
    "            # Forward Propagation\n",
    "            self.hidden_layer_input     = np.dot(self.x, self.weights_hidden) + self.bias_hidden\n",
    "            self.hidden_layer_output    = self.sigmoid(self.hidden_layer_input)\n",
    "            self.output_layer_input     = np.dot(self.hidden_layer_output, self.weights_output) + self.bias_output\n",
    "            self.output                 = self.sigmoid(self.output_layer_input)\n",
    "            \n",
    "            # Backpropagation\n",
    "            self.error                  = self.y - self.output\n",
    "            self.d_output               = self.error * self.sigmoid_derivative(self.output)\n",
    "            \n",
    "            self.error_hidden_layer     = self.d_output.dot(self.weights_output.T)\n",
    "            self.d_hidden_layer         = self.error_hidden_layer * self.sigmoid_derivative(self.hidden_layer_output)\n",
    "            \n",
    "            # Updating Weights and Biases\n",
    "            self.weights_output         += self.hidden_layer_output.T.dot(self.d_output) * lr\n",
    "            self.bias_output            += np.sum(self.d_output, axis=0, keepdims=True) * lr\n",
    "            self.weights_hidden         += self.x.T.dot(self.d_hidden_layer) * lr\n",
    "            self.bias_hidden            += np.sum(self.d_hidden_layer, axis=0, keepdims=True) * lr\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Final predictions:\n",
      "[[0.01925543]\n",
      " [0.98336582]\n",
      " [0.9833735 ]\n",
      " [0.01722527]]\n",
      "\n",
      "Final hidden weights and bias:\n",
      "[[4.58811077 6.46772612]\n",
      " [4.58638776 6.46067251]] \n",
      " [[-7.03972497 -2.87152512]]\n",
      "\n",
      "Final output weights and bias:\n",
      "[[-10.28268276]\n",
      " [  9.58673232]] \n",
      " [[-4.43517739]]\n"
     ]
    }
   ],
   "source": [
    "ann2 = DeepNeuralNetwork(x1,y1)\n",
    "ann2.train(50000, 0.1)\n",
    "print('Final predictions:')\n",
    "print(ann2.output)\n",
    "print('\\nFinal hidden weights and bias:')\n",
    "print(ann2.weights_hidden, '\\n', ann2.bias_hidden)\n",
    "print('\\nFinal output weights and bias:')\n",
    "print(ann2.weights_output, '\\n', ann2.bias_output)"
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
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
