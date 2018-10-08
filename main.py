
import os
import sys
from models.VectorModel import VectorModel
from models.PreProcessing import PreProcessing
if __name__ == '__main__':
	print("\n\n--------------------")
	print("     Model Vector ")
	print("--------------------\n\n")
	aux = PreProcessing()
	aux.readDocuments()
	#allwords = aux.readAndSaveDocsSeparate()
	#print(allwords)
   