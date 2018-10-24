
import os
import sys
import re
from models.VectorModel import VectorModel
from models.PreProcessing import PreProcessing

def readQueries(PATH_DOCS = "/home/katiely/Documents/RiI/TP1_VectorModel/cfc/cfquery"):
	print("lendo arquivo de consultas.....")
	queries = []
	_QN = r"^(QN)\ ([0-9]*)"
	_NR = r"^(NR)\ ([0-9]*)"
	_RD = r"^(RD)\ ([\d \n]*)"
	_QU = r"^(QU)\ ([\w \n])"
	with open(PATH_DOCS,'r' ) as arquivo:
		text = arquivo.read()
		QN = re.findall(_QN,text,re.MULTILINE)
		QU = re.findall(_QU,text,re.MULTILINE)
		RD = re.findall(_RD,text,re.MULTILINE)
		NR = re.findall(_NR,text,re.MULTILINE)

		for x in range(100):
			q = (QN[x][1],QU[x][1],NR[x][1],RD[x][1])
			queries.append(q)

	return queries
if __name__ == '__main__':
	print("\n\n--------------------")
	print("     Model Vector ")
	print("--------------------\n\n")
<<<<<<< HEAD

	print("Testando salvar as paradas")
=======
>>>>>>> master
	
	aux = VectorModel()
	aux.parseDocs()
	aux.buildInvList()
	aux.calculateDocumentsVectors()
	aux.calculateNormEachDoc() 
	readQueries = readQueries()  
	aux.calculateQueryVectors(readQueries)