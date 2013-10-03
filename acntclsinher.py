class Bank:
        def __init__(self):
                self.bal=0

        def dep(self,amount):
                self.bal+=amount
                return self.bal

        def wit(self,amount):
                self.bal-=amount
                return self.bal





class Mini(Bank):
	def __init__(self,minibal):
 		Bank.__init__(self)	
		self.minibal=minibal

	def withdrw(self,amount):
		if self.balance-amount < self.minibal:
			print "cant"
		else:
			Bank.withdrw(self,amount)
	def dep(self,amount):
		Bank.dep(self,amount)


a=Mini(100)
print a.dep(100)
print a.dep(300)
print a.withdrw(100)
b=Mini(100)
print b.dep(4000)
print b.dep(1000)
print b.withdrw(345)

