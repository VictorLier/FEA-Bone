import numpy as np
import matplotlib.pyplot as plt


FileName = 'testFile.txt'

Directory = 'C:\\Users\\Victor\\Documents\\DTU\\41812 FEA\\Project 2\\ANSYS\\'

FilSti = Directory + FileName

print (FilSti)

data = np.loadtxt(FilSti)

plt.plot(data[:,0],data[:,1])
plt.show()
