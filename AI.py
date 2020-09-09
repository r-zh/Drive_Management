# -*- coding: utf-8 -*-

# All the AI trainning se

# AI works for take the right action in each moment
# -*- coding: utf-8 -*-

# All the AI trainning set

# AI for Self Driving Car

# Importing the libraries

import numpy as np
import random
import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.autograd as autograd
from torch.autograd import Variable

class Network(nn.Moudle): #inheritance the nn.Moudle -》 java extend

    def __init__(self, input_size, nb_action): #self is complusory first one; nb_action-> final result
        super(Network, self).__init__()
        self.input_siz = input_size
        self.nb_action = nb_action
        # connect input layer to full layer
        # neural network including input, hidden and output 3 layers
        # input_size -> actions, 30 -> hidden layers
        self.fc1 = nn.Linear(input_size,30) #full connection
        
        self.fc1 = nn.Linear(30, nb_action) #full connection hidden layers to output_layers
        
    