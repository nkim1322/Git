nucleotides = { 'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
	

print ''.join([nucleotides[letter] for letter in raw_input("Enter sequence ")])

