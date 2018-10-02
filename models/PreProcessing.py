import re
import os
import sys

from models.Documents import Documents

#numberOfDocs = 0
PATH = "C:\\Users\\Katiely\\Documents\\UFAM\\6periodo\\RI\\TP1\\TP1_VectorModel\\cfc\\docs"
class PreProcessing():
	def __init__(self):
		pass 

	def readDocuments(self, docsPath = PATH):
		numberOfDocs = 0
		allWords = set()
		print("->Reading documents...")
		files = os.listdir(docsPath)
		
		for eachfile in files:
			
			with open(PATH+"\\"+eachfile,'r') as doc:
				content =  doc.read().split("\n\n")
				numberOfDocs = numberOfDocs+ len(content)
				for aux in range(0,len(content)):
					content[aux] = content[aux].lower()
					auxx = content[aux].split(" ")
					for x in auxx:
						if(x in ["\n"]):
							x = x[0:len(x) -1]
						allWords.add(x)
					
			doc.close()	
		print("->Read all documents ....")
		print("->Amount of Words: "+ str(len(allWords)))
		print("->Amount of docs: " + str(numberOfDocs-5))
		
		return allWords		