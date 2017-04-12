#Converts from decimal to binary system
def convert_to_binary(x):
    converted = ""
    while x > 0:
        if x % 2 == 0:
            x = int(x / 2)
            converted += "0"
        if x % 2 == 1:
            x = int(x / 2)
            converted += "1"
    print("Your number converted to binary system: " + converted[::-1])

#Converts from binary to decimal
def convert_to_decimal(x):
    converted = 0
    square = len(x) - 1
    for i in x:
        converted = converted + int(i)*(2**square)
        square -= 1
    print("Your number converted to decimal system: " + str(converted))

#Checks if exactly 2 numbers have been entered
def lenght_checking():
    global separated
    global number
    while not len(separated) == 2:
        print("Error! Example of correct input: 10101101 2 \n")
        number = input("Give me a number and (after space) a number system (2/10): ")
        separated = number.split(" ", 2)

#Checks if binary number has only "1" and "0"
def binary_checking():
    if separated[0] == "":
        print("\nIn binary system, you can only use 1 and 0.")
        separated[0] = input("Please enter ONLY your binary number once again: ")
        binary_checking()
    for element in separated[0]:
        if (element == "1" or element == "0"):
            continue
        else:
            print("\nIn binary system, you can only use 1 and 0.")
            separated[0] = input("Please enter ONLY your binary number once again: ")
            binary_checking()
            break


try_again = "yes"

#Main loop
while try_again == "yes":
    number = input("Give me a number and (after space) a number system (2/10): ")
    separated = number.split(" ", 2)

    lenght_checking()

    #Checks if input is digits only
    while not (separated[0].isdigit() and separated[1].isdigit()):
        print("You can enter only numbers! \n")
        number = input("Give me a number and (after space) a number system (2/10): ")
        separated = number.split(" ", 2)
        lenght_checking()

    #Makes sure the second number is "2" or "10"
    while not (separated[1] == "10" or separated[1] == "2"):
        print("Error! After space, you can enter only 2 o 10! \n")
        number = input("Give me a number and (after space) a number system (2/10): ")
        separated = number.split(" ", 2)
        lenght_checking()
        while not (separated[0].isdigit() and separated[1].isdigit()):
            print("You can enter only numbers! \n")
            number = input("Give me a number and (after space) a number system (2/10): ")
            separated = number.split(" ", 2)
            lenght_checking()



    #If decimal input
    if separated[1] == "10":
        if separated[0] == "0":
            print("Your number converted to binary system: 0")
        else:
            number_to_convert = int(separated[0])
            convert_to_binary(number_to_convert)

    #If binary input
    if separated[1] == "2":
        binary_checking()
        convert_to_decimal(separated[0])

    #Asks for starting again
    try_again = input("\n Would you like to try again? (yes/no) ")
    while not (try_again == "yes" or try_again == "no"):
        print("\n You can enter only yes or no!")
        try_again = input("Would you like to try again? (yes/no) ")
