import matplotlib.pyplot as plt 
labels = 'frogs','hogs','dogs','logs'
sizes = [15,30,45,10]
explode = [0,0.1,0,0]

plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)

plt.show()