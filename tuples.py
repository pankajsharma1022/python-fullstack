
#Booleans
True
False
# tupples : these are immutable
t = (1,2,3)
print(t[0])
t=('a',True,123)
print(t)

#sets
x=set()

x.add(1)
x.add(2)
x.add(3)
print(x)

# reassign hello to goodbye
l=[3,7,[1,4,'hello']]
l[2][2]="goodbye"
print(l)

# call hello from dictionary
d1={'simple_key':'hello'}
d2={'k1':{'k2':'hello'}}
d3={'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])
# here k1 dictionay then list oth index item then dictionary again and then again 1th index item of list