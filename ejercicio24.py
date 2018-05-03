import numpy as np
import  matplotlib.pyplot as plt

medicion= [1.2, 2.5,2.8,5.0]
x= np.linspace(0.0001,100, 100)
y= np.ones(100)


def fun(x, lamda):
      
    ca = 1.0/(np.exp(-1) - np.exp(-20))
    return (ca/lamda)*np.exp(-x/lamda)
c= len(medicion)


contador=0.0
for i in range(100):
    for j in range(c):
        y[i]= y[i]*(fun(medicion[j], x[i]))
            
    contador+=y[i]
y=y/contador

plt.plot(x,y)
plt.show()
