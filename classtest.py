class person:
	def __init__(self, name):
		self.name = name
	def printname(self):
		print self.name

a = person("aa")
b = a
print a, id(a), a.printname()
print b, id(b), b.printname()