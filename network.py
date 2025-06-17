import typing
import random
import numpy as np
from activation_functions import *


class network():
    def __init__(self,nodes:list[int],activations:list[activation_function]) -> None:


        self.weights = [np.asmatrix([[random.random() for k in range(nodes[i])] for j in range(nodes[i+1])])
                    for i in range(len(nodes)-1)]
        
        self.biases = [np.asmatrix([random.random() for j in range(nodes[i])]) for i in range(len(nodes))]

        self.activations=activations


    def forward_pass(self,x):

        for i in range(len(self.weights)):

            x = self.activations.calculate((x*self.weights[i]) + self.bias[i])
        
        return x
    
    
            
