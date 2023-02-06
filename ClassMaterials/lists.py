# Create an empty list
numbers = []

# keep track of how many numbers entered
count = 1

# collect our numbers from the User
print("-" * 60)
print("Enter 5 numbers to multiply by 2 <press Enter after each number>")

# the loop will cntinuew until we get all of our numbers
while(count <= 5):
	print("Count is now:", count)
	currentNumber = input("Enter a number: ")
	numbers.append(int(currentNumber))
	count += 1

# iterate over our list, myultiply each value by 2, and print to the screen
print("\n\n")
print("your numbers multiplied by 2 are:")
for num in numbers:
	print(num * 2)
	
