from objects import FamousRockBand


band1 = FamousRockBand('Led Zeppelin')
band1.add_member('Robert Plant')
band1.add_member('Jimmy Page')
band1.add_member('John Paul Jones')
band1.add_member('John Bonham')
band1.add_record_label('Swan Song')
band1.add_manager('Pere Grant')

print(band1.bandname)
print(band1.manager)
print(band1.members)