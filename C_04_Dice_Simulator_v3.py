import random


def roll_die():
    result = random.randint(1, 6)
    return result


# main routine stars here

# rolls two dice and returns total and whether we
# had a double roll
def two_rolls():
    double_score = "no"

    # Roll two diec
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    user_points = roll_1 + roll_2

    # Show the use the result
    print(f"Die 1 : {roll_1} \t Die 2: {roll_2}")

    return user_points, double_score



how_many = int(input("how many dice?"))

#tab = loob plus the for in range thingy
for item in range (0, 10):

    if how_many == 2:
        start_points = two_rolls()
        points = start_points[0]
        double_points = start_points[1]

        print(f"you have{points}Points and double score of {double_points}")





