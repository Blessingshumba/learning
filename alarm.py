# This script activate the ISC alarm when leaving the premises
# You will need to enter the code that you were given
# Only three chances are given that and if you fails the program will lock you out
name = input("Please enter your name ")
print("Good Evening " + name + "Please note you are the last person to leave the office please set the alarm \n"
                               " by following procedures below PLEASE NOTE YOU ONLY HAVE THREE CHANCES ")
num = int(input("Please enter the 4 digit pin to activate the alarm "))
pin = 1979
count = 0
while num != pin:
    count = count + 1
    print("incorrect code")
    # print("You have " + str(3-count) + " trials left ")
    # TODO tidy up the formatting
    print("You have {} trials left ".format(str(3 - count)))
    num = int(input(" Please enter the 4 digit pin to activate the alarm "))
    if num == pin:
        print("Congratulations you have set the alarm now lock the door and go home")
    elif count == 2:
        print("ooops " + name + " You cant go home today")
        break
        # TODO remove todo
