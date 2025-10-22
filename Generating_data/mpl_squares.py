import matplotlib.pyplot as plt


input_values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,
                24,25]
squares = [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361, 
           400,441,484,529,576,625]

plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()
ax.plot(input_values,squares,linewidth=3)

#Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()
