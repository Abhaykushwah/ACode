'''Python for Beginners #13
List Functions'''

#Heterogenous list
a=[1,'bitten',3,4.0,'tech']

print("Length of list:",len(a))

a[0]=2
print("list:",a)

a.append('subscribe')
print("list:",a)

a.insert(1,'tech')
print("list:",a)

b=a.pop(0)
print("element deleted:",b)
print("list:",a)

a.remove(4.0)
print("list:",a)

del a[1:3]
print("list:",a)

a=['tech','bitten']
a.reverse()
print("List in reverse",a)

a.sort()
print("List after sorting",a)
