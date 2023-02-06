class Employee:
	def __init__(self, name, start_year, team):
		self.name = name
		self.start_year = start_year
		self.team = team


	def member_intro(self):
		print("Meet ", self.name)
		print(f"{self.name} joined the Services Team in {self.start_year}")
		print(f"{self.name} is part of the {self.team} Team")

chan = Employee('Chan', 2021, 'Battery')
chan.member_intro()
print('\n')
obed = Employee('Obed', 2021, 'Battery')
obed.member_intro()
print('\n')
enersto = Employee('Ernesto', 2020, 'NDT')
enersto.member_intro()
print('\n')
paige = Employee('Paige', 2022, 'Battery')
paige.member_intro()
print('\n')
chris = Employee('Chris', 2019, 'ATS')
chris.member_intro()

teamMembers = ['bob','jim','jan']
teamMemberObjs = []

for member in teamMembers:
	newObj = Employee()
	newObj.name(member)
	teamMemberObjs.append(newObj)
	


