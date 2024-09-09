

while True:

    error = "Please enter an integer that is 13 or more"



    try:

        my_num = int(input("Enter an integer:"  ))
        print("Your number is" ,my_num)
            # Checks that the number is more than / equal to 13
        if my_num < 13:
            print(error)
        else:
            print("Your number is🎲🎲 " , my_num)


    except ValueError:
        print(error)
