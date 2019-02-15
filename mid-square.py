import random

def gethash(dictkey):
    square=dictkey**2
    i1=square%100
    print('i1:',i1)
    hash1=i1%20
    print('hash=',hash1)
    return hash1
def addentry(hash1,dictkey):
    if [dictkey,hash1] not in lists:
        lists[hash1].append([dictkey,hash1])
        print('final list',lists[hash1])
lists = [[] for _ in range(20)]       
for i in range(20):
    key=random.randint(0,100)
    print(key)
    hash2=gethash(key)
    addentry(hash2,key)
