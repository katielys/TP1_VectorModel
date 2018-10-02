
class VectorModel(object):

	def __init__(self):
		self.totalOfDocs = 0
		self.invIndex = []

	def tf(self, document, word):
		if document in self.invIndex[word]:
			return self.invIndex[word][document]
		else:
			return 0.0
