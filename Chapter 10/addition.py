            
active = True
while active:
    value1 = input("Enter a number\nor press 'q' to quit: ")
    if value1 == 'q':
        break
    value2 = input("Enter another number\nor press 'q' to quit: ")
    if value2 == 'q':
        break
    try:
        answer = float(value1) + float(value2)
    except ValueError:
        print("You must enter two numbers to add them!") 
    else:
        print(f"the answer is {answer}.") 