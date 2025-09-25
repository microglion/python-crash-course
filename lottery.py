from random import sample
pool = [1,2,3,5,7,11,13,17,19,23,29, 'a', 'b', 'c', 'd', 'e']
pick = sample(pool, 4)
print(f"Any ticket matching these 4  numbers or letters wins a prize: {pick}")
my_ticket = [3,11,17,'b']
counter = 0
while set(my_ticket) != set(pick):
    pick = sample(pool,4)
    counter +=1

print(f"it took {counter} tries to get a winning ticket")
print(f"your ticket: {my_ticket}")
print(f"winning numbers: {pick}")

