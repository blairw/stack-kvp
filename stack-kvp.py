import csv, array, sys

# all arrays start at 0
TRANPOSE_BEGINS_AT = 1

with sys.stdin as csvfile:
	nextlinereader = csv.reader(csvfile, delimiter=',', quotechar='|')

	headings = []
	linecounter = 0
	totalcolumns = 0
	for row in nextlinereader:

		# handle headings
		if linecounter == 0:
			preparedLineToPrint = ''
			colcounter = 0
			
			for cell in row:
				if colcounter < TRANPOSE_BEGINS_AT: 
					preparedLineToPrint = preparedLineToPrint + cell + ","
				headings.append(cell)
				colcounter = colcounter + 1

			# completed
			print preparedLineToPrint + "key,value"
			totalcolumns = colcounter

		# handle rows
		else:
			colcounter = 0

			commonstart = ''
			while colcounter < totalcolumns:
				if colcounter < TRANPOSE_BEGINS_AT:
					commonstart = commonstart + row[colcounter] + ","
				else:
					print commonstart + headings[colcounter] + "," + row[colcounter]
				colcounter = colcounter + 1

		# regardless, for all lines
		linecounter = linecounter + 1
