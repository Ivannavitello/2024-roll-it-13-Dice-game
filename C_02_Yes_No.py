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


# got to video (07), timestamp 0:45\




#elif want_instructions == "no" or want_instructions == "n":
    #print("you chose no")
#elif want_instructions == "ya":
    #print("you chose yes")
#elif want_instructions == "non":
    #print("you chose no")
#elif want_instructions == "stop":
    #print("you chose us to stop ok :(")
#elif want_instructions == "why":
    #print("we were just trying to help what do you mean why >:( 😠")
#elif want_instructions == "ok":
    #print("ok ok ok ok ok ok ok")
#elif want_instructions == "maybe":
    #print("what if you just answer the question right YES OR NO")