message = "This is an alien invasion game. Shoot an alien and find out how many points " \
"it's worth. The more you shoot, the more you earn"
print(message)

game_on = True
while game_on == True:
	print("\n")
	print("=" * 90)
	print("1 = Green Alien")
	print("2 = Yellow Alien")
	print("3 = Red Alien")
	print("4 = Blue Alien")
	print("Enter 'exit' to exit the game")
	print("\nNow make your selection to shoot an alien")
	print("=" * 90)

	Green_Alien = 5
	Yellow_Alien = 10
	Red_Alien = 20
	Blue_Alien = 30

	shoot_alien = input("Type 1, 2, 4, or 'exit': ")
	if shoot_alien == "1":
		print(f"Well done! You won {Green_Alien} points for shooting a Green Alien")
	elif shoot_alien == "2":
		print(f"Great! You won {Yellow_Alien} points for shooting a Yellow Alien")
	elif shoot_alien == "3":
		print(f"Awesome! You won {Red_Alien} points for shooting a Red Alien")
	elif shoot_alien == "4":
		print(f"Woo-hoo! You won {Blue_Alien} for shooting a Blue Alien")
	elif shoot_alien.lower() == "exit":
		game_on = False
		print("Game Over! Bye")
	else:
		print("Invalid selection. Please select a valid option")