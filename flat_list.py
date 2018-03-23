'''#!/usr/bin/python'''

import random

def recoursive_flat(alist, newlist):
	i=0
	
	while i < len(alist):
		if type(alist[i]) == type([]):
			
			recoursive_flat(alist[i], newlist)
			
		elif type(alist[i]) == type(1):
			newlist.append(alist[i])
			
		i+=1
	
	return 

'''
def rappend(lisa):

	rando=random.randint(0,1)
	if rando == 1:
		lis=[]
		rappend(lis)
		lisa.append(lis)
		lisa.append([])
		lisa.append(1)
	else:
		for i in range(random.randint(1,5)):
			lisa.append(random.randint(1,99))
	return


lista=[1,2,3,[4,5,[]],[{3:5}],8,9]
listc=[3,4,5,6,6]
lista.append("a")
lista.append(listc)

for k in range(50):
		rappend(lista)


#lista=[]
newlis=[]
print (lista)
recoursive_flat(lista, newlis)


print (newlis)'''
