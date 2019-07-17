import numpy as np 
import matplotlib.pyplot as plt 

np.random.seed(2)
mu,sigma = 100,20
a = np.random.normal(mu,sigma,size=100)

plt.hist(a,20,normed=1,histtype='stepfilled',facecolor='y',alpha=0.75)
plt.title(r'直方图',fontproperties='SimHei')
plt.show()