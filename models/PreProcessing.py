import re
from models.Documents import Documents
class PreProcessing():
	def __init__(self):
		pass
	def readDocument(self, docPath):
		with open(docPath,'r') as doc:
			aux  = 0
			l = []
			for line in doc:
				print (line)
				l.append(line)
				aux= aux+1
			print(aux)	
			print(l[12])
