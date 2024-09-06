# Checks users enter yes (y) or (n)

def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("you did not chose a valid response")

# Main routine
while True:
    want_instruction = yes_no("Do you want to read the instructions? ")
    print(f"You chose {want_instruction}")





#roll_again = yes_no("Do you want to roll again? ")
 #print(f"you said {roll_again} to rolling again.")



# print(f" You answered {want_instructions} to the question ")


# got to video (03 yes no part 2), timestamp 0:45