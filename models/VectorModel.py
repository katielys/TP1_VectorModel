
class VectorModel(object):

	def __init__(self):
		self.totalOfDocs = 0

	def __preprocessing(self, sentence):

		sentence = sentence.lower()
		modifiedSentence = sentence.strip().split()

		return modifiedSentence