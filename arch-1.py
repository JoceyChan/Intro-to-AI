#
# arch.py
#
# This script implements three Python classes for three different artificial
# neural network architectures: no hidden layer, one hidden layer, and two
# hidden layers. Note that this script requires the installation of the
# PyTorch (torch) Python package.
#
# This content is protected and may not be shared, uploaded, or distributed.
#
# PLACE ANY COMMENTS, INCLUDING ACKNOWLEDGMENTS, HERE.
# ALSO, PROVIDE ANSWERS TO THE FOLLOWING TWO QUESTIONS.
#
# Which network architecture achieves the lowest training set error?
# 2 Hidden layers is the lowest training set error.
# Which network architecture tends to exhibit the best testing set accuracy?
# Hidden Layer 1 is the best testing set accuracy.
# PLACE YOUR NAME AND THE DATE HERE
# Jocelyn Chan December 5, 2021

# PyTorch - Deep Learning Models

# Number of input features ...
input_size = 4
# Number of output classes ...
output_size = 3


class AnnLinear(nn.Module):
    """Class describing a linear artificial neural network, with no hidden
    layers, with inputs directly projecting to outputs."""

    def __init__(self):
        super().__init__()
        # PLACE NETWORK ARCHITECTURE CODE HERE
        self.my_layer = nn.Linear(input_size, output_size)

    def forward(self, x):
        # PLACE YOUR FORWARD PASS CODE HERE
        y_hat = self.my_layer(x)
        return y_hat


class AnnOneHid(nn.Module):
    """Class describing an artificial neural network with one hidden layer,
    using the rectified linear (ReLU) activation function."""

    def __init__(self):
        super().__init__()
        # PLACE NETWORK ARCHITECTURE CODE HERE
        self.hidLa = nn.Linear(input_size, 20)
        self.outLa = nn.Linear(20, output_size)

    def forward(self, x):
        # PLACE YOUR FORWARD PASS CODE HERE
        hidLaA = F.relu(self.hidLa(x))
        y_hat = self.outLa(hidLaA)
        return y_hat


class AnnTwoHid(nn.Module):
    """Class describing an artificial neural network with two hidden layers,
    using the rectified linear (ReLU) activation function."""

    def __init__(self):
        super().__init__()
        # PLACE NETWORK ARCHITECTURE CODE HERE
        self.hidL1 = nn.Linear(input_size, 16)
        self.hidL2 = nn.Linear(16, 12)
        self.outLa = nn.Linear(12, output_size)

    def forward(self, x):
        # PLACE YOUR FORWARD PASS CODE HERE
        hidLaA1 = F.relu(self.hidL1(x))
        hidLaA2 = F.relu(self.hidL2(hidLaA1))
        y_hat = self.outLa(hidLaA2)
        return y_hat
