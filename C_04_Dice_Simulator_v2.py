import random


def roll_die():
    result = random.randint(1, 6)
    return result


# main routine stars here
#tab = loob plus the for in range thingy
for item in range (0, 10):
    user_score = 0
    double_score = "no"

    # Roll two diec
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    user_points = roll_1 + roll_2

    # Show the use the result
    print(f"Die 1 : {roll_1} \t Die 2: {roll_2} \t points: {user_points}")
    print(f"Double score opportunity: {double_score}")
