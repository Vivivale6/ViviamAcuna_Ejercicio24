import numpy as np
import  matplotlib.pyplot as plt

medicion= [1.2, 2.5,2.8,5.0]
x= np.lispace(0.0001,100, 100)
y= np.ones(100)


def fun(x, lamda):
    
    a = np.exp(-1.0/lamda)
    b= np.exp(-20/lamda)
    
    return np.exp(-x/lamda)/(lamda*(a-b))
c= len(medicion)

def cuenta(y,c,x):
    contador=0.0
    for i in range(1000):
        for j in range(c):
            y[i]= y[i]*(fun([j], x[i]))
            
        contador+=y[i]
    return contador

d= cuenta(y,c,x)
y=y/d

plt.plot(x,y)
