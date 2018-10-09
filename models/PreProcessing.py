import re
import os
import sys

from models.Documents import Documents

#numberOfDocs = 0
PATH = "/home/katiely/Documents/RiI/TP1_VectorModel/cfc/docs/"
class PreProcessing():
	def __init__(self):
		listaDocs = []
		
	

	def readAndSaveDocsSeparate(self,docsPath = PATH):
		numberOfDocs = 0
		listaDocs = []

		print("->Reading documents...")
		files = os.listdir(docsPath)
		
		for eachfile in files:
			
			pathFile = PATH+eachfile
			with open(pathFile,'r') as doc:
				content =  doc.read().split("\n\n")
				numberOfDocs = numberOfDocs+ len(content)
				for aux in range(0,len(content)):
					#print(content[aux])
					listaDocs.append(content[aux])
					content[aux] = content[aux].lower()
					auxx = content[aux].split(" ")
					for x in auxx:
						if(x in ["\n"]):
							x = x[0:len(x) -1]
						
					
			doc.close()	
		 	
		for x in range(0,len(listaDocs)):
			
			try:
				path = "d"+str(x)+".txt"
				f = open("/home/katiely/Documents/RiI/TP1_VectorModel/cfc/separate/"+path,'w+')
				f.write(listaDocs[x])
			except Exception as e:
				raise e 
			

		print("->Creating all documents ....")
		#print("->Amount of Words: "+ str(len(allWords)))
		#print("->Amount of docs: " + str(numberOfDocs-5))
		
	#return allWords		
	def readDocuments(self, docsPath = PATH):
		numberOfDocs = 0
		allWords = set()

		print("->Reading documents...")
		files = os.listdir(docsPath)
		
		for eachfile in files:
			
			pathFile = PATH+eachfile
			with open(pathFile,'r') as doc:
				content =  doc.read().split("\n\n")
				numberOfDocs = numberOfDocs+ len(content)
				for aux in range(0,len(content)):
					#print(content[aux])

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
