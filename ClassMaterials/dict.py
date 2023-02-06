shows = {
	'seinfeld': ['Jerry', 'George', 'Elaine', 'Kramer'],
	'office': ['Michael', 'Dwight', 'Pam', 'Jim', 'Creed'],
	'sledgehammer': ['Sledge', 'Dori', 'Captain Trunk', 'Officer Majoy']
}

for key in shows.keys():
	print("\n")
	print("**",key,"**")
	for character in shows[key]:
		print(character)
print(shows['sledgehammer'][0])
shows['office'].append('Angela')