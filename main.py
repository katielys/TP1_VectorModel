# -*- coding: utf-8 -*-
import os
import sys
import re
from models.VectorModel import VectorModel
from models.VectorModelPlus import VectorModelPlus
from models.PreProcessing import PreProcessing
from models.Metrics import Metrics
from pprint import pprint

def readQueries(PATH_DOCS = "/home/katiely/Documents/RiI/TP1_VectorModel/cfc/cfquery"):

	print("lendo arquivo de consultas.....")
	queries = []
	_QN = r"^(QN)\ ([0-9]*)"
	_QU = r"^(QU)\ ([\w \n]*)"
	_NR = r"^(NR)\ ([0-9]*)"
	_RD = r"^(RD)\ ([\d \n]*)"
	
	with open(PATH_DOCS,'r' ) as arquivo:
		text = arquivo.read()
		QN = re.findall(_QN,text,re.MULTILINE)
		QU = re.findall(_QU,text,re.MULTILINE)
		NR = re.findall(_NR,text,re.MULTILINE)
		RD = re.findall(_RD,text,re.MULTILINE)
		
		for x in range(100):

			docRelavants = RD[x][1].strip().split()
			docToScore = zip(docRelavants[0::2], docRelavants[1::2]) #Tupla -> x = n doc relevante, y=relevancia

			q = (QN[x][1],QU[x][1],NR[x][1],docToScore)
			queries.append(q)
			# pprint(list(q[3]))
			# input("Clique <ENTER> para prosseguir")
	return queries

if __name__ == '__main__':

	try:
		PATH_DOCS = sys.argv[1]
	except Exception as e:
		pass

	
	
	# aux = VectorModel("cfc/separate/*.txt")
	aux = VectorModel("cfc/separate/*.txt")
	
	queries = readQueries(PATH_DOCS)

	acc_precisao = 0.0
	acc_revocacao = 0.0
	acc_f1 = 0.0
	acc_MAP = 0.0

	for i in range(0,len(queries)):

		r_querie = [int(x) for x, y in queries[i][3]]
		# print("Querie Number: " + queries[i][0])
		# print("Number Relevants: " + queries[i][2])
		print(queries[i][2])
		rank_vetorial = vmp.ranking_k(queries[i][1],1) #Vai calcular o top k similares -> passa título querie como parametro int(queries[i][2])

		
		metrics = Metrics(r_querie,rank_vetorial)

		acc_precisao += metrics.precisao()
		print("Precisão: " + str(metrics.precisao()))
		acc_revocacao += metrics.revocacao()
		print("Revocação: " + str(metrics.revocacao()))
		acc_f1 += metrics.f1()
		print("F-Measure: " + str(metrics.f1()))
		print("NDCG@10 "+ str(metrics.ndcgk(metrics.R)))
		#print("P@10: "+ str( metrics.parroba(metrics.R)))
		#print("MAP: " + str(metrics.MAP()))



		# print("Vetorial: ")
		# pprint(rank_vetorial)
		# print("\n\n")
		# print("Relevantes: ")
		# pprint(r_querie)
		# print("\n\n")
		# input("Clique <ENTER> para prosseguir")
	print("Media precisao: " + str(acc_precisao/len(queries)))
	print("Media revocacao: " + str(acc_revocacao/len(queries)))
	print("Media f-measure: " + str(acc_f1/len(queries)))
	print("Media MAP: " + str(acc_MAP/len(queries)))
