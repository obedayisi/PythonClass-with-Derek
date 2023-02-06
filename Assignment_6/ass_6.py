def addition(firstNum, secondNum):
	if choice == '1':
		print("Result =", int(firstNum) + int(secondNum))
def multiplication(firstNum, secondNum):
	if choice == "2":
		print("Result =", int(firstNum) * int(secondNum))
def division(firstNum, secondNum):
	if choice == "3":
		print("Result =", int(firstNum) / int(secondNum))
def subtraction(firstNum, secondNum):
	if choice == "4":
		print("Result =", int(firstNum) - int(secondNum))


def calculate(choice):
	firstNum = input("Enter First Number:")
	secondNum = input("Enter Second Number:")
	addition(firstNum, secondNum)
	multiplication(firstNum, secondNum)
	division(firstNum, secondNum)
	subtraction(firstNum, secondNum)
	
	#else:
		#print("Not a valid selection!!")


def header1():
	print("\n\n")
	print("*" * 60)
	print("Enter a Selection\n")
	print("1: Add 2 Values")
	print("2: Multiply 2 Values")
	print("3: Divide 2 Values")
	print("4: Subtract 2 Values")
	print("5: Exit program")
	print("*" * 60)

while True:
	header1()
	valid_selection = [1, 2, 3, 4, 5]
	choice = input("Type [1,2,3,4,5]")
	if int(choice) not in valid_selection:
		print("\nNot a valid selection")
		continue
	if choice == "5":
		print("Bye")
		break
	calculate(choice)