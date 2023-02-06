# Question: Write a program that converts Celsius to Fahrenheit

# Take user input in Celsius 
print("This program converts temperature from Celsius to Fahrenheit")
celsius = input("\nPlease enter a temperature in Celsius: ")
celsius = int(celsius)

# Convert Celsius to Fahrenheit (F = C x 9/5 + 32)
fahrenheit = celsius*(9/5) + 32

# Display Results
print("\n----------------------------------------------------------------")
print(f"\nTemperature you entered in Celsius is: {celsius}C")
print(f"Temperature in Fahrenheit is: {fahrenheit}F")
