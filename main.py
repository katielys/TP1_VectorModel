
import os
import sys
from models.VectorModel import VectorModel
from models.PreProcessing import PreProcessing
if __name__ == '__main__':
	##vectorModel = VectorModel('C:\\Users\\Katiely\\Documents\\UFAM\\6periodo\\RI\\TP1\\TP1_VectorModel\\cfc')
	##print(vectorModel.totalOfDocs)
	# with open('C:\\Users\\Katiely\\Documents\\UFAM\\6periodo\\RI\\TP1\\TP1_VectorModel\\cfc\\cf74', 'r') as file:
	# 	print(file)
	aux = PreProcessing()
	aux.readDocument('C:\\Users\\Katiely\\Documents\\UFAM\\6periodo\\RI\\TP1\\TP1_VectorModel\\cfc\\docs\\cf74')
   