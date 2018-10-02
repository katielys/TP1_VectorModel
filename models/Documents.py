class Documents(object):
	"""docstring for Documents"""
	def __init__(self, pn, rn, man,autor,title,src,majorSubjects,minorSubjects,ae,ref,citations):
		self.paperNumber = pn
		self.recordNumber = rn
		self.medlineAcessionNumber = man
		self.autor = autor
		self.source = src
		self.title = title
		self.majorSubjects = majorSubjects
		self.minorSubjects = minorSubjects
		self.abstractExtract = ae
		self.references = ref
		self.citations = citations

	def __getPaperNumber(self):
		return self.paperNumber	
	def	__getRecordNumber(self):
		return self.recordNumber
	def __getMedlineAcessionNumber(self):
		return self.medlineAcessionNumber
	def __getTitle(self):
		return self.title	
	def __getSource(self):
		return self.source
	def __getAbstract(self):	
		return self.abstractExtract	
	def __getCitations(self):
		return self.citations
	def __getReferences(self):
		return self.references	
	def __getAutors(self):
		return self.autor
	def __getMajorSubjects(self):
		return self.majorSubjects
	def __getMinorSubjects(self):
		return self.minorSubjects				

	def toString(self):
		strToReturn = ''
		strToReturn = strToReturn + "Paper Number: " + __getPaperNumber() + "\n"
		strToReturn = strToReturn + "Record Number: " + __getRecordNumber() + "\n"
		strToReturn = strToReturn + "Medline Acession Number: " + __getMedlineAcessionNumber()+ "\n"
		strToReturn = strToReturn + "Title: "+ __getTitle()+ "\n"
		strToReturn = strToReturn + "Source: "+ __getSource()+  "\n"
		strToReturn = strToReturn + "Abstract/Extract: "+ __getAbstract()+  "\n"
		strToReturn = strToReturn + "Citations: "+ __getCitations()+  "\n"
		strToReturn = strToReturn + "References: "+ __getReferences()+  "\n"
		strToReturn = strToReturn + "Autors: : "+ __getAutors()+  "\n"
		strToReturn = strToReturn + "Major Subjects: "+ __getMajorSubjects()+  "\n"
		strToReturn = strToReturn + "Minor Subjects: "+ __getMinorSubjects()+  "\n"


		return	strToReturn