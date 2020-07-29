original = [["Cat", 'Dog'],['Rat','Kittern']]

copied = original[:]

print(original == copied)
print(original is copied)

copied[0].append("Cammel")
print(copied)
print(original)
