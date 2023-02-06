# Question: Write a program to find the Area of a Circle

# Take user input. This is the radius of the circle
print("This program calculates the area of a circle")
radius = input("\nPlease enter the radius of the circle: ")
radius = int(radius)

# Calculate Area of the circle based on the radius (Area = pi*r^2)
area = 3.14*radius**2

# Display results
print("\n-------------------------------------------------------------")
print(f"\nThe radius you entered is: {radius}")
print(f"The Area of the circle is: {area}")