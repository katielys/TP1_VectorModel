# -*- coding: utf-8 -*-
import numpy as np

class Metrics(object):
	"""docstring for Metics"""
	def __init__(self,N,R):

		self.N = N # Solução
		self.R = R # Resposta
		self.axisX = []
		self.axisY = []

		self.precisao_value = 0.0
		self.revocacao_value = 0.0
		self.f1_value = 0.0
		self.MAP_value = 0.0

	def precisao(self):
		N = set(self.N)
		R = set(self.R)
		
		self.precisao_value = float(len(N.intersection(R))) / len(R)
		return self.precisao_value

	def revocacao(self):
		N = set(self.N)
		R = set(self.R)
		
		self.revocacao_value = float(len(N.intersection(R))) / len(N)
		return self.revocacao_value

	def f1(self):
		try:
			self.f1_value = 2*((self.precisao_value * self.revocacao_value)/(self.precisao_value + self.revocacao_value))
			return self.f1_value
		except Exception as e:
			return 0.0

	def calculateXY(self):
		
		indiceRelevantes = []
		for i, r in enumerate(self.R):
			if r in self.N:
				indiceRelevantes += [i + 1]

		self.axisX = [0] * len(indiceRelevantes)
		self.axisY = [0] * len(indiceRelevantes)

		for i, value in enumerate(indiceRelevantes):
			Ri = self.R[:value]
			Ni = self.N

			self.axisX[i] = self.revocacao(Ni, Ri)
			self.axisY[i] = self.precisao(Ni, Ri)

	def MAP(self):
		counter = 0.0
		for y in self.axisY:
			counter += y

		try:
			self.MAP_value = counter / len(self.axisY)
			return self.MAP_value
		except Exception as e:
			return 0.0

	def dcgk(self , k=10, method=0):
		r= self.R
		r = np.asfarray(r)[:k]
		if r.size:
			if method == 0:
				return r[0] + np.sum(r[1:] / np.log2(np.arange(2, r.size + 1)))
			elif method == 1:
				return np.sum(r / np.log2(np.arange(2, r.size + 2)))
			else:
				raise ValueError('method must be 0 or 1.')
		return 0.0


	def ndcgk(self, k=10, method=0):
		r= self.R
		dcg_max = self.dcgk( k, method)
		if not dcg_max:
			return 0.
		return self.dcgk( k, method) / dcg_max

	def parroba(self, k=10):
		r= self.R
		assert k >= 1
		r = np.asarray(r)[:k] != 0
		if r.size != k:
			raise ValueError('Relevance score length < k')
		return np.mean(r)

