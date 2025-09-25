import time 

# get duration from user
minutes = int(input("How many minutes do you want to study for? "))

# convert minutes to seconds 
total_seconds = minutes * 60
seconds_studied = 0

while seconds_studied < total_seconds:
    #convert seconds_studied to minutes and seconds for diplay
    minutes_display = seconds_studied // 60 #integer division
    seconds_display = seconds_studied % 60 # remainder (modulo)

    print(f"\rTime studied: {minutes_display}:{seconds_display:02d}", end="",flush=True) #:02d makes seconds show as 2 digits, \r returns cursor to start of line, end="" prevents print from adding newline, flush = True ensures output shows immediately 
    time.sleep(1) #wait for 1 second
    seconds_studied +=1 # Add 1 to our counter

print("\nTime's up!")

