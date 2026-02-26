import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [1,2,3,4,5]
y = [50,40,70,80,20]
z = [10,20,30,40,50]

ax.plot(x,y,z)

plt.title('3D Plot Example')
plt.show()