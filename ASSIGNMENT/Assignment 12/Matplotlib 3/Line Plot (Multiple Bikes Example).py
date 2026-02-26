import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [50,40,70,80,20]
y2 = [80,20,20,50,60]
y3 = [70,20,60,40,60]
y4 = [80,20,20,50,60]

plt.plot(x,y,'g',label='Enfield',linewidth=5)
plt.plot(x,y2,'c',label='Honda',linewidth=5)
plt.plot(x,y3,'k',label='Yamaha',linewidth=5)
plt.plot(x,y4,'y',label='KTM',linewidth=5)

plt.title('Bike Details in Line Plot')
plt.ylabel('Distance in kms')
plt.xlabel('Days')
plt.legend()
plt.show()