# Author: Quentin Jensen
#
# tricks:
#	- shorten each name (columns 1-6)
#	- only mention the name once, for each section
#		(ie: if lines 1-2 are named "A", then lines 3-6 are named "B", only lines 1 and 3 are labeled)
#	- in the ATOM section, many numbers are consecutive. shorten it to only the beginning and end
#			
# for reference: http://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html
#

import sys


def compress(fin, fout):
	"""iterate through each line, calling functions to compress a line further"""

	lastLine = "++"
	currentName = ""
	cLine = ""
	for line in fin:

		cLine = compressName(line)

		#only keep the names that begin a new section
		if cLine[0:4] == currentName:
			cLine = cLine[4:]
		else:
			currentName = cLine[0:4]

		#remove leading and trailing whitespace
		cLine = cLine.strip() + "\n"

		if(cLine):
			fout.write(cLine)
		
		lastLine = cLine




def compressName(line):
	""" maps the name of the line to its corresponding index into names.
    and writes that index to the line instead"""

	for name in names:
		if line[0:6] == name[0:6]:
			#print(names[name] + line[6:])
			return "<" + names[name] + ">" + line[6:]







# all names available to a pdb file. these names are contained in characters
# 1-6 of each line.
names = {
"HEADER": "HD",
"OBSLTE": "OB",
"TITLE ": "TI",
"SPLT  ": "ST",
"CAVEAT": "CA",
"COMPND": "CO",
"SOURCE": "SO",
"KEYWDS": "KE",
"EXPDTA": "EX",
"NUMMDL": "NU",
"MDLTYP": "MD",
"AUTHOR": "AU",
"REVDAT": "RV",
"SPRSDE": "SP",
"JRNL  ": "JR",
"REMARKS": "RE",
"DBREF ": "DB",
"DBREF1": "D1",
"DBREF2": "D2",
"SEQADV": "SV",
"SEQRES": "SR",
"MODRES": "MO",
"HET   ": "HT",
"FORMUL": "FO",
"HETNAM": "HM",
"HETSYN": "HN",
"HELIX ": "HE",
"SHEET ": "SH",
"SSBOND": "SS",
"LINK  ": "LI",
"CISPEP": "CI",
"SITE  ": "SI",
"CRYST1": "CR",
"MTRIX1": "M1",
"MTRIX2": "M2",
"MTRIX3": "M3",
"ORIGX1": "O1",
"ORIGX2": "O2",
"ORIGX3": "O3",
"SCALE1": "S1",
"SCALE2": "S2",
"SCALE3": "S3",
"MODEL ": "ML",
"ATOM  ": "AT",
"ANISOU": "AN",
"TER   ": "TE",
"HETATM": "HA",
"ENDMDL": "EM",
"CONECT": "CT",
"MASTER": "MA",
"END   ": "EN"}


if __name__ == "__main__":

	#1HHP.pdb -> 1HHP.cpdb
	#finName = sys.argv[0]
	finName = "./pdbs/1HHP.pdb"
	#prefix = finName.split('.')[0]
	#foutName = prefix + ".cpdb"
	#foutName = finName + "c"
	foutName = "tmp.cpdb"
	
	with open(finName, 'r') as fin:
			with open(foutName, 'w') as fout:
				compress(fin, fout)
	




