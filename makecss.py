import sys
from xml.dom import minidom

class makeCSS():
	
	########################### CONFIG #############################
	"""
		MINIFIED:
		if False the output css formatted by tabs by parent-child relation
		if True the output css is minified
	"""
	MINIFIED = False 
	
	"""	
		RETURNORIGINAL:
		if False only the css selectors are returned
		if True the input html code returned as well
	"""
	RETURNORIGINAL = True
	
	TABCHAR = '\t'
	"""
		TABCHAR:
		Tab characther for indenting when MINFIED = False
	"""
	########################### /CONFIG #############################
	

	retpar = ''
	parentCounter = ''
	elemArray = []
	
	def getParents(self, element):
		
		def par(element):
			
			self.parentCounter += self.TABCHAR
			
			pid = ''
			pc = ''
			
			if element.parentNode.nodeType == element.parentNode.ELEMENT_NODE:
				par(element.parentNode)
				# TODO elso elemet ismetli
			
			# get element id
			pid = element.getAttribute('id')
			if pid == '':
				pid = ''
			else:
				pid = '#' + pid
			
			# get element class
			pc = element.getAttribute('class').replace(' ','.')
			if pc == '':
				pc = ''
			else:
				pc = '.' + pc
			
			if element.nodeName != 'makeCSSContainer':
				self.retpar += element.nodeName + pid + pc + ' ' 
			#print retpar
			
		
		par(element)
		r = self.retpar
		self.retpar = ''
		return r
		
			

	def parseCSS(self, dom, orig):
		
		if self.RETURNORIGINAL:
			print orig
		
		ndom = minidom.parseString(dom)
		ret = ''
		
		for elements in range(len(ndom.getElementsByTagName('*'))):
			element = ndom.getElementsByTagName('*')[elements]
			if element.nodeName != 'makeCSSContainer':
				parent = self.getParents(element)
			
				if parent not in self.elemArray:
					self.elemArray.append(parent)
					
					if self.MINIFIED:
						ret += parent + '{}\n'
					else:
						ret += self.parentCounter + parent + '{\n\t\n' + self.parentCounter + '}\n\n'
					self.parentCounter = ''
		return ret


c = makeCSS()
r = sys.stdin.read().strip()
print c.parseCSS('<?xml version="1.0" encoding="utf-8" ?><makeCSSContainer>'+r+'</makeCSSContainer>', r)

