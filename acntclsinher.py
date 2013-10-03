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
		if self.bal-amount < self.minibal:
			print "cant"
		else:
			print Bank.wit(self,amount)
	def dep(self,amount):
		print Bank.dep(self,amount)


a=Mini(100)
a.dep(100)
a.dep(300)
a.withdrw(350)
b=Mini(100)
b.dep(4000)
b.dep(1000)
b.withdrw(345)

