import os
import glob
import numpy as np
from collections import Counter

class VectorModel(object):

	def __init__(self,pathDocs = "/home/katiely/Documents/RiI/TP1_VectorModel/cfc/separate/*.txt"):
		self.totalOfDocs = 0
		self.invIndex = []
		self.pathDocs = pathDocs

	def parseDocs(self):
		PATH = self.pathDocs
		print("->Lendo Arquivos.............")
		texts, words = {}, set()
		#print(glob.glob(PATH))
		for txtfile in glob.glob(PATH):
			with open(txtfile, 'r') as f:
				self.totalOfDocs += 1.0
				txt = f.readlines()
				words |= set(txt)
				docs = txtfile.split('/')[-1]
				docs = int(docs[1:-4])
				texts[docs] = txt

		self.documents = texts
		self.vocabulary = sorted(list(words)) 
		print("->Tamanho total do vocabulario: "+ str(len(self.vocabulary)))
		print("->total docs: "+ str(len(self.documents)))


	def buildInvList(self):
		print("->criando indice....")
		dictWords = {}
		for x in self.vocabulary:
			dictWords[x] = dict()

		for txt, wrds in self.documents.items():
			freq = Counter(wrds)
			for aWord, aFreq in freq.most_common():
				dictWords[aWord][txt] = aFreq

		self.invIndex = dictWords
		print("->Finalizacao da criacao do indice.....")

	def tf(self, document, word):
		if (document in self.invIndex[word]):
			return self.invIndex[word][document]
		else:
			return 0.0
	def idf(self, word):
		N = self.totalOfDocs
		if (word in self.invIndex):
			Nt = len(self.invIndex[word])
		else:
			Nt = 0.0
		if Nt != 0:
			return np.log(N / Nt)
		else:
			return 0.0		
	def calculateDocumentsVectors(self):
		print("->calculando norma documentos")
		vetors = {}
		total = len(self.documents)
		atual = 0.0
		for doc in self.documents.keys():
			vetors[doc] = np.zeros(len(self.vocabulary))
			for i, w in enumerate(self.vocabulary):

				w_d = self.idf(w) * self.tf(doc, w)
				if (w_d > 0.0):
					vetors[doc][i] = w_d
		self.vetorsDocument = vetors	
		print("->acabou calculo da norma docs")		
	def calculateNormEachDoc(self):
		print("->Calculando norma de cada documento..............")
		norms = {}
		for doc in self.documents:
			norms[doc] = np.linalg.norm(self.vetorsDocument[doc])
		self.norms = norms
		print("->finalizando calculo..................")
	def calculateQueryVectors(self,query):
		v_Q = {}
		v_Q['Q'] = np.zeros(len(self.vocabulary))
		freq = {}
		for x in range(0,len(query)):
			if x in freq:
				freq[x] += 1
			else:
				freq[x] = 1

		for w in range(0,len(query)):
			w_d = self.idf(w) * freq.get(w, 0)
			position = self.vocabulary.index(w)
			v_Q['Q'][position] = w_d
		return v_Q



			