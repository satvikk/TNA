import numpy as np
D = np.loadtxt('dist.txt')
Gd=np.zeros([100,100])
for i in range(1,101):
	Gd[i-1]=np.argsort(D[i-1], kind='quicksort', order=None) +1 
np.savetxt('Gd.txt', Gd, fmt='%-3.0f') 