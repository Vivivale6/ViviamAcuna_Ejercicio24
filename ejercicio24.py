import numpy as np
import  matplotlib.pyplot as plt

medicion= [1.2, 2.5,2.8,5.0]
x= np.linspace(0.0001,100, 100)
y= np.ones(100)


def fun(x, lamda):
    
    a = np.exp(-1.0/lamda)
    b= np.exp(-20/lamda)
    
    return np.exp(-x/lamda)/(lamda*(a-b))

contador=0.0
for i in range(100):
    for j in range(len(medicion)):
        y[i]= y[i]*(fun(medicion[j], x[i]))
            
        contador+=y[i]
        
    return contador


y=y/contador

plt.plot(x,y)
