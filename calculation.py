# program loop
while True:

    question = input("Please enter the calculation method in numbers. |1. +, 2. -, 3.×, 4.÷\n> ")

    one = int(input("Please enter the first number.\n> "))
    two = int(input("Please enter the second number.\n> "))

    # Answer display after calculation for each calculation method
    if question == '1':
        print( "answer is " + str(one + two) + ".")
    elif question == '2':
        print("anser is " + str(one - two) + ".")
    elif question == '3':
        print("anser is " + str(one * two) + ".")
    elif question == '4':
        print("anser is " + str(one / two) + ".")
    else:
        print("Error.")  