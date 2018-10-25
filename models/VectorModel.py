import os
import glob
import numpy as np
from pprint import pprint
from collections import Counter

class VectorModel(object):

	def __init__(self,pathDocs = "/home/katiely/Documents/RiI/TP1_VectorModel/cfc/separate/*.txt"):
		self.totalOfDocs = 0
		self.invIndex = []
		self.pathDocs = pathDocs
		self.vocabulary = []
		self.documents = {} #dict = (documento,palavras)
		self.invIndex = {} # Dict de Dict -> 

	def removerRuido(self,txt):
		txt = txt.strip()
		txt = txt.strip('\n')
		return txt

	def parseDocs(self):
		PATH = self.pathDocs
		print("->Lendo Arquivos.............")
		texts, words = {}, set()
		#print(glob.glob(PATH))
		for txtfile in glob.glob(PATH):
			with open(txtfile, 'r') as f:
				self.totalOfDocs += 1.0
				txt = f.readlines()
				txt_doc = []

				for i in range(0,len(txt)):
					txt[i] = self.removerRuido(txt[i])

					for sub_word in txt[i].split():
						txt_doc.append(sub_word)
						words.add(sub_word)

				docs = txtfile.split('/')[-1]
				docs = int(docs[1:-4])
				texts[docs] = txt_doc

		self.documents = texts
		self.vocabulary = sorted(list(words)) 
		print("->Tamanho total do vocabulario: "+ str(len(self.vocabulary)))
		print("->total docs: "+ str(len(self.documents)))


	def buildInvList(self):
		print("->criando indice....")
		dictWords = {}
		for x in self.vocabulary:
			# print(self.vocabulary)
			dictWords[x] = dict()

		for txt, wrds in self.documents.items():
			freq = Counter(wrds)
			for aWord, aFreq in freq.most_common():
				dictWords[aWord][txt] = aFreq


		self.invIndex = dictWords
		# pprint(dict(self.invIndex))
		# input("\nClique <ENTER> para prosseguir")

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
		v_Q = np.zeros(len(self.vocabulary))

		freq_q = Counter()

		for x in range(0,len(query)):
			freq_q[query[x]] += 1
			
		for w in range(0,len(query)):
			if(query[w] in self.vocabulary):
				w_d = self.idf(query[w]) * freq_q[query[w]]
				position = self.vocabulary.index(query[w])
				v_Q[position] = w_d
		return v_Q



			