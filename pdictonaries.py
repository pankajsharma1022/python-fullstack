# dictonaries
my_stuff = {"key1":123,'key2':'value2','key3':{'123':[1,2,'grabMe']}}
# here in key3 there is a key inside the key
print(my_stuff)
#here in we can access only grabme also for that we need to
print(my_stuff['key3']['123'][2])
# in this we provided the index no. of 'grabme' and then put then putted the key's attached to it like '123'&'key3'
print(my_stuff['key3']['123'][2].upper())
my_stuff = {'lunch':'pizza','bfast':'eggs'}
my_stuff['lunch'] = 'burger'
print(my_stuff['lunch'])