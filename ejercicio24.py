import numpy as np
import  matplotlib.pyplot as plt
medicion= [1.2, 2.5,2.8,5.0]


def fun(x):
    lamda=1
    return 1/lamda*np.exp(-x/lamda)
