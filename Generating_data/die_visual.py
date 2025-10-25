from die import Die
import plotly.express as px


#create a D6.
die = Die()

#Make some rolls and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#Analyse the results.
frequencies = []
poss_results = range(1,die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualise the results. 
title = "Results of Rolling one D6 1000 times"
labels={'x':'Result','y':'Frequency of Result'}
fig = px.bar(x=poss_results,y=frequencies, title=title, labels=labels)
fig.show()