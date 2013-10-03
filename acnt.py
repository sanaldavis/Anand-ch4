def makacnt():
  return {'balance':0}

def dep(account, rs):
  account['balance']+=rs
  return account['balance']

def withdrw(account,rs):
  account['balance']-=rs
  return account['balance']

a=makacnt()
b=makacnt()
print dep(a,100)
print withdrw(a,10)
print dep(b,800)
print withdrw(b,100)

