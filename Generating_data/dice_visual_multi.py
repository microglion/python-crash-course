from die import Die
import plotly.express as px


#create two D6 Dice.
die_1 = Die()
die_2 = Die()

#Make some rolls and store results in a list.
results = [die_1.roll() * die_2.roll() for roll_num in range(5_000_000)]

max_result = die_1.num_sides * die_2.num_sides
poss_results = range(1,max_result+1)
frequencies = [results.count(value) for value in poss_results]

#Visualise the results. 
title = "Results of Rolling two D6 Dice and multiplying values 5,000,000 times"
labels={'x':'Result','y':'Frequency of Result'}
fig = px.bar(x=poss_results,y=frequencies, title=title, labels=labels)
#Further customise chart
fig.update_layout(xaxis_dtick=1)
fig.write_html('dice_visual_multi.html')