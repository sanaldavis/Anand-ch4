class Bank:
	def __init__(self):
		self.bal=0

	def dep(self,amount):
		self.bal+=amount
		return self.bal

	def wit(self,amount):
		self.bal-=amount
		return self.bal

a=Bank()
print a.dep(100)
print a.dep(300)
print a.wit(100)
b=Bank()
print b.dep(4000)
print b.dep(1000)
print b.wit(345)
