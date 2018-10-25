# -*- coding: utf-8 -*-
import os
import glob
import numpy as np
import nltk

from pprint import pprint
from collections import Counter
from operator import itemgetter
from nltk.tokenize import word_tokenize

stemmer = nltk.stem.SnowballStemmer('english')

class VectorModelPlus(object):

	def __init__(self,pathDocs = "/home/katiely/Documents/RiI/TP1_VectorModel/cfc/separate/*.txt"):
		self.totalOfDocs = 0
		self.invIndex = []
		self.pathDocs = pathDocs
		self.vocabulary = []
		self.documents = {} #dict = (documento,palavras)
		self.invIndex = {} # Dict de Dict -> 
		self.norms = {}
		self.vetorsDocument = {} #Vetores de cada doc

		with open('stopwords.txt', 'r') as file:
			self.stopWords = set(file.read().split())

		self.parseDocs()
		self.buildInvList()
		self.calculateDocumentsVectors()
		self.calculateNormEachDoc() 

	def removerRuido(self,txt):
		txt = txt.strip()
		txt = txt.strip('\n')
		return txt

	def hasNumbers(self,word):
		return any(char.isdigit() for char in word)

	def preProcessamento(self,word):

		if (self.hasNumbers(word) == False):return None
		
		word = word.lower()                          
		word = stemmer.stem(word)

		if (word in self.stopWords == True):return None                      
		
		return word

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
						sub_word = self.preProcessamento(sub_word)
						if (sub_word != None):
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

	def calculateQueryVector(self,query):
		v_Q = {}
		v_Q = np.zeros(len(self.vocabulary))

		freq_q = Counter()
		query_words = query.split()

		for x in range(0,len(query_words)):
			freq_q[query_words[x]] += 1
			
		for w in range(0,len(query_words)):
			if(query_words[w] in self.vocabulary):

				w_d = self.idf(query_words[w]) * freq_q[query_words[w]]
				position = self.vocabulary.index(query_words[w])
				v_Q[position] = w_d

		return v_Q

	def calculateSimilarity(self,doc,query,vector_query,norm_query):

		sum_q = 0.0
		sum_norms = self.norms[doc] * norm_query

		for i in range(0,len(self.vocabulary)):
			sum_q += self.vetorsDocument[doc][i] * vector_query[i]

		similarity = sum_q/sum_norms

		return similarity

	def reformularQuery(self,query):

		nova_consulta = ""
		for sub_word in query.split():
			sub_word = self.preProcessamento(sub_word)
			if (sub_word != None):
				nova_consulta += sub_word + ""
		return nova_consulta

	def ranking_k(self,query,k=10):
		print("->Calculando Rank de cada documento..............")
		if (k > len(self.documents)):
			k = 10
		documents_rank = {} # Key = doc number | Value = similarity
		tuple_documents = []
		top_k = []

		query = self.reformularQuery(query)
		vector_query = self.calculateQueryVector(query)
		norm_query = np.linalg.norm(vector_query)

		for doc in self.documents.keys():
			documents_rank[doc] = self.calculateSimilarity(doc,query,vector_query,norm_query)

		for doc, sim in documents_rank.items():
			tuple_documents.append((doc,sim))

		tuple_documents.sort(key=lambda x: x[1],reverse = True)

		for i in range(0,k):
			top_k.append(tuple_documents[i][0])

		print("->finalizando calculo..................")
		return top_k







			