import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.plasma, s=10)

#Set chart title and label axes
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Cube of value", fontsize=14)

#Set size of tick labels
ax.tick_params(labelsize=14)

#set range for each axis
ax.axis([1,5100,0,150_000_000_000])
#ax.ticklabel_format(style='plain')

plt.savefig('cube_plot.png', bbox_inches='tight')
plt.show()

