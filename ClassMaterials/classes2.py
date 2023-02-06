class Driver:
	def __init__(self, name, sponsor, pay):
		self.name = name
		self.sponsor = sponsor
		self.pay = pay
		self.winCount = 0
	def add_a_win(self):
		self.winCount += 1
	def get_wins(self):
		return self.winCount

driver1 = Driver('Ricky Bobby', 'Laughing Clown Malt Liquor', 1000000)
driver2 = Driver('Jean Girard', 'Perrier', 900000)
driver1.add_a_win()
driver2.add_a_win()
driver2.add_a_win()

print(driver1.name, " has ", driver1.get_wins())
print(driver2.name, " has ", driver2.get_wins())