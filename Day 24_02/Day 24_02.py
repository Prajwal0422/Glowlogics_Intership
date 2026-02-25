import numpy as np
import matplotlib.pyplot as plt

x= np.array([80,85,90,85])
y= np.array([80,85,50])

plt.title("Sport")
plt.xlabel("Average pulse")
plt.ylabel("Caolorie burnage")

plt.plot(x,y)
plt.show()