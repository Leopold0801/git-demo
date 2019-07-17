import matplotlib.pyplot as plt
import numpy as np

'''
plt.plot([0,2,4,6,8],[3,1,4,5,2])
plt.ylabel('grade')
plt.axis([-1,10,0,6]) #x从-1到10，y从0到6
plt.show()
'''
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

a = np.arange(0.0,5.0,0.02)

plt.subplot(2,1,1)
plt.plot(a,f(a))

plt.subplot(2,1,2)
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.show()
