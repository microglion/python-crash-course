from random import randint
class Die:
    def __init__(self, sides=6):
        self.sides=sides

    def roll_die(self):
        outcome = randint(1,self.sides)
        print(outcome)

    def multi_roll(self, num_rolls):
        for i in range(num_rolls):
            self.roll_die()


K_die = Die(8)
K_die.multi_roll(5)

K_die = Die(8)
K_die.multi_roll(5)









