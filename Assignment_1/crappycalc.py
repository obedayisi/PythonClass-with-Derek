exitFlat = 0		# <-- Added a new variable and assigned it a value of 0

while (exitFlat == 0):
	print("\n\n")
	print("*" * 60)
	print("Enter a Selection\n")
	print("1: Add 2 Values")
	print("2: Multiply 2 Values")
	print("3: Divide 2 Values")
	print("*" * 60)
	print("4: Exit Program")

	choice = input("Type [1,2,3,4]")
	if (choice == "1"):
		firstNum = input("Enter First Number: ")
		secondNum = input("Enter Second Number: ")
		print("Result = ", int(firstNum) + int(secondNum))
	elif (choice == "2"):
		firstNum = input("Enter First Number: ")
		secondNum = input("Enter Second Number: ")
		print("Result = ", int(firstNum) * int(secondNum))
	elif (choice == "3"):
		firstNum = input("Enter First Number: ")
		secondNum = input("Enter Second Number: ")
		print("Result = ", int(firstNum) / int(secondNum))
	elif (choice == "4"):
		exitFlat = 1
		print("bye")
	else:
		print("Not a valid selection!!")