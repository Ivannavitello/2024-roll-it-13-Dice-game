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
    print('''
    
***** instructions *****

do something and do the game 
    Just play if you want
why are you here '🎲🎲🎲🎲😁☆*: .｡. o(≧▽≦)o .｡.:*☆

actual instructions Nuber Checker

  
    ''')


print()
print("🎲🎲 Roll it 13 🎲🎲")
print("hello world")
print()
print()


# loop for testing purposes
# Test this Test

want_instructions = input(" Do you want to see the instructions? ").lower()

# checks users enter yes (y) or (n) testing the test
if want_instructions == "yes":
    instruction()

print("program continues")




# print(f" You answered {want_instructions} to the question ")


# got to video (07), timestamp ???
