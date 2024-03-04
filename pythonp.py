print("h")
print("pleaae run the program")
mstring = 'abcd'
print(mstring[-1]) #last string
print(mstring[:2]) # in this last one is excluded
print(mstring[:]) # this will print everything
print(mstring[::2]) # when i use :: then it will exclude the no. of times you used in that
# like if i have used ::2 then it will skip every element after 1
# if you have used :::3 it will print the third letter skipping 2 
# string is immutable you cannot change this
x=mstring.upper()
print(x)
mstring="Hello Pankaj Sharma"
x=mstring.split()
print(x)
# now this has splitted everything
x=mstring.split('l')
print(x)
# now this will split the string by the l character 
# In simple words whenever compiler see the l character it will break split the string 


# print formatting
x= "Item One: {x} Item Two:{y}".format(x="dog",y="cat")
print(x)
a="My name is: {x} my cell is: {y}".format(x="Pankaj", y=9509712287)
print(a)