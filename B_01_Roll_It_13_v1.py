# Checks users enter yes (y) or (n)

def yes_no(question):
    while True:
        response = input(question).lower()
        # YEs or no checker if user doesn't answer properly it repeats
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please type yes / no")

def instruction():
    # Checks that users enter an integer
    # that is more than 13

    print('''
    
***** instructions *****

do something and do the game 
    Just play if you want
why are you here '🎲🎲🎲🎲😁☆*: .｡. o(≧▽≦)o .｡.:*☆
(❁´◡`❁) ^_____^
actual instructions Nuber Checker
 Actually Instructions: To begin, decide on a winning score (eg: The first one to get a score of 50 points wins).

For each round of the game, you win points by rolling dice.
The winner of the round is the one who gets closest to 13 without going over.

If you win the round, then your score will increase by the number of points that you earned.
If your first roll of two dice is a double (eg: both dice show a three),
then your final score will be double the number of points.

If you lose the round, then you dont get any points.

If you and the computer tie ( eg: you both get a score of 11),
then you will both have 11 points added to your score.

Your goal is to reach the target goal before the computer.

Good Luck!
  
    ''')


print()
print("🎲🎲 Roll it 13 🎲🎲")
print("hello world")
print()
print()

# Checks that users enter an integer
# that is more than 13

def int_check():

    while True:

        error = "Please enter an integer that is 13 or more"

        try:

            response = int(input("Enter an integer:"))
            print("Your number is", response)
                # Checks that the number is more than / equal to 13


            if response < 13:
                print(error)
            else:
                return response


        except ValueError:
                print(error)



# loop for testing purposes
# Test this Test

want_instructions = input(" Do you want to see the instructions? ").lower()

# checks users enter yes (y) or (n) testing the test
if want_instructions == "yes":
    instruction()

print()
target_score = int_check()
print(target_score)



# print(f" You answered {want_instructions} to the question ")


# got to video (09), timestamp ???
