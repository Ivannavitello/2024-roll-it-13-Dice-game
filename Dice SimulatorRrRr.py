import random


#generates an integer between 0 and 6
#to simulate a roll of a dice
def roll_die():
    result = random.radint(1, 6)
    return result

#main routine starts here
die_roll = roll_die()
print(die_roll)



# random mumbers

#for item in range(0, 10):
    #dice_roll = random.randint(1, 24)
   # print(dice_roll, end="\t")
