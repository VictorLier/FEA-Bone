import numpy as np


def ImportData(Directory):
    array = np.empty([2,1])
    i=1
    while True:
        try:
            Filename = Directory + "\\" "i" + ".txt"
            Load = np.loadtxt(Filename)
            print(Load)
            array = np.append(array, Load)
            i = i+1
        except:
            break
    
    return array


array = ImportData(r"C:\Users\Victor\Documents\DTU\41812 FEA\Project 2\ANSYS")

Directory = r"C:\Users\Victor\Documents\DTU\41812 FEA\Project 2\ANSYS"

Filename = Directory + "\\" "1" + ".txt"

Load = np.loadtxt(Filename)
print(Load)

#print(array)

