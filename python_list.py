# list
#mylist = ['a','b','c','d','e']
#print(mylist[:3])

#mylist2 = ['string',95097122,95098748,20.50]
#print(mylist2)
#print("after change")
#mylist2[0] = 'kya kare'
#print(mylist2)

# append will add in the last
#mylist.append(34)
#print(mylist)
# to add multiple
#mylist.append(["x","y","z"])
#print(mylist)
# in using this way this will simply add the whole as a new element 
# and will look bad
 
# instead of this we can use extend
#listtwo=['x','y','z']
#mylist.extend(listtwo)
#print(mylist)

# to remove we can use pop method
#mylist.pop(0)
#print(mylist)
#mylist.pop(3)
# basically this will reverse our list
#mylist.reverse()
#print(mylist)
# these changes occur in place means we donot have to save them in other list
# my list.sort
#mylist.sort()
#print(mylist)

# indexing a nested list
#mylist = [1,2,['x','y','z']]
#print(mylist[2][1])
# In this way i can access single elements of list inside another list

# list comphressions
matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)


sec_col = [row[1] for row in matrix]
print(sec_col)

thi_col = [p[2] for p in matrix]
print(thi_col)