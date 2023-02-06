# CrappyCalculator.py: If you actually need this, you're doomed
print("\n\n")		# print out 2 new lines
print("*" * 60)		# note the multiplication operator when used on a string duplicates it
print("Enter a Selection\n")
print("1: Add 2 Values")
print("2: Multiply 2 Values")
print("3: Divide 2 Values")
print("*" * 60)

choice = input("Type [1,2,3])")

if (choice == "1"):
	firstNum = input("Enter First Number: ")
	secondNum = input("Enter Second Number: ")
	print("Result =", int(firstNum) + int(secondNum))
elif (choice == "2"):
	firstNum = input("Enter First Number: ")
	secondNum = input("Enter Second Number: ")
	print("Result = ", int(firstNum) * int(secondNum))
elif (choice == "3"):
	firstNum = input("Enter First Number: ")
	secondNum = input("Enter Second Number: ")
	print("Result = ", int(firstNum) / int(secondNum))
else:
	print("Not a valid selection!!")