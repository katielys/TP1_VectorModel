from VectorModel import VectorModel
from operator import itemgetter

class WAND(VectorModel):
	def __init__(self, pathDocs = "/home/katiely/Documents/RiI/TP1_VectorModel/cfc/separate/*.txt"):
		super(WAND, self).__init__(pathDocs)
		self.UB = None
		self.listaInv = None
		self.InvertedIndex = None
		self.termosOrd = None
		self.top_k = None
		self.curDoc = None

		self.threshold = -1;
		self.result_num = None;

	def ordTermos(self):
		if(len(self.termosOrd) == 0):
			for elem in self.listaInv: 
				self.termosOrd.append([listaInv[elem][0], listaInv[elem][1]])  
		sorted(self.termosOrd, key=itemgetter(0))

	def nextID(self, change_index, docID):
		change_term = termosOrd[change_index][1]
		while (listaInv[change_term][0] < docID): 
			listaInv[change_term] += 1
		self.termosOrd[change_index][0] = self.listaInv[change_term][0];

	def findPivotTerm(self):
		UBscore = 0;
		for i in range(0, len(self.termosOrd)):
			UBscore += self.UB[self.termosOrd[i][1]];
			if (UBscore >= threshold):
				return i
		return -1

	def run(self):
		self.listaInv = self.invIndex
		while (true):
			ordTermos();
			pivot_index = findPivotTerm()

			if (pivot_index == -1):
				return -1

			lastID = 2000000

			pivot_term = self.termosOrd[pivot_index][1]
			pivot_DID = self.listaInv[pivot_term][0]
			
			if (pivot_DID == lastID):
				return -1
			
			if (pivot_DID <= self.curDoc):
				change_index = 0
				self.nextID(change_index, self.curDoc + 1)
			else:
				first_DID = termosOrd[0][1]
				if (first_DID == pivot_DID):
					self.curDoc = pivot_DID
					return self.curDoc
				else:
					for i in range(0, pivot_index):
						self.nextID(i, pivot_DID)
