# Author: Quentin Jensen
# http://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html

import sys

def compress(fin, fout):
	cLine = ""
	lastLine = "+"
	for line in fin:
		cLine = compressName(line)
		#cLine = compressNamesBySection(cLine, lastLine)
		lastLine = line

		if(cLine):
			fout.write(cLine)


def compressNamesBySection(cLine, lastLine):
	if cLine[0] == lastLine[0]:
		print(cLine[0])
		return  cLine[2:]
	else:
		return cLine


def compressName(line):
	""" maps the name of the line to its corresponding index into names.
    and writes that index to the line instead"""

	for name in names:
		if line[0:6] == name[0:6]:
			return names[name] + line[6:]







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
"MTRIXn": "MT",
"ORIGXn": "OR",
"SCALEn": "SC",
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
	foutName = finName + "c"
	
	with open(finName, 'r') as fin:
			with open(foutName, 'w') as fout:
				compress(fin, fout)
	




