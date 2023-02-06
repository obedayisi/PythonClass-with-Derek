class RockBand:
	""" Anyone can be in a band """
	def __init__(self, bandname):
		self.bandname = bandname
		self.members = []

	def add_member(self, name):
		self.members.append(name)

class FamousRockBand(RockBand):
	""" Famous bands have extra properties """
	def add_manager(self, manager):
		self.manager = manager 

	def add_record_label(self, record_label):
		self.record_label = record_label

band1 = FamousRockBand('Led Zeppelin')
band1.add_member('Robert Plant')
band1.add_member('Jimmy Page')
band1.add_member('John Paul Jones')
band1.add_member('John Bonham')
band1.add_record_label('Swan Song')
band1.add_manager('Pere Grant')