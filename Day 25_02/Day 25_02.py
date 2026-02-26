# import matplotlib.pyplot as plt
# import numpy as np
#
# x1 = np.array([2,3,4,5])
# x2 = np.array([2,3,4,5])
# y1 = np.array([33,4,5,3])
# y2 = np.array([2,3,4,5])
# plt.subplot(1,2,3)
# plt.plot(x1,y1)
# plt.show()

from matplotlib import pyplot as plt

plt.bar([8,22,3,12,3,4],height=2,width=5)
plt.bar([3,4,2,33,12,3],height=6,width=5)
plt.legend()
plt.ylabel("Distanbce")
plt.xlabel("New")
plt.show()

#Pie chart

