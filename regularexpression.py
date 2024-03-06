import re
#patterns = ['term1','term2']
#text = 'This is a string with term1,not the other!'
#for pattern in patterns:
#    print("I'm searching for: "+pattern)
# here regular exprssions helps you to find paaterns in strings
#    if re.search(pattern,text):
#        print("Match")
#    else:
#        print("NO MATCH")


#match = re.search('term1',text)
#print(type(match))
#print(match.start())
# it will give the value where they start to match


#####@@@@@@@@@@@@@##########
#split_term = '@'
#email = 'userEgmail.com'.split()
#print(re.split(split_term))
# we use split method when we want to split the string
# for example split method will split the string from the @ sign in two different strings 


# print(re.findall('match','test phrase match in middle'))

# if oi use findall then in this it doesn't matter how many words i have used of same name 
# it will print me all of them


#def multi_re_find(patterns,phrase):
#   for pat in patterns:
#        print("searching for pattern {}".format(pat))
#        print(re.findall(pat,phrase))
#        print('\n')
#test_phrase = 'sdsd..sssddd..sdddsddd...dsds.dssssss...sddddd'
#test_patterns = ['sd*'] 
#multi_re_find(test_patterns,test_phrase) 


# if i used the 'sd+' then it will search for the patterns staring with s and followed by 1 or more D
# if i want0 and ! time then i can use ? like sd?
#def multi_re_find(patterns,phrase):
#    for pat in patterns:
#        print("searching for pattern {}".format(pat))
#        print(re.findall(pat,phrase))
#        print('\n')
#test_phrase = 'sdsd..sssddd..sdddsddd...dsds.dssssss...sddddd'
#test_patterns = ['sd?']  
#multi_re_find(test_patterns,test_phrase) 

# If i write like '[sd{3}] then it means search for the every s followed by 3ds in a row'
# If i write like '[sd{1,3}]' then it means it will find for the s followed by 1 and 3 ds in a row
# and the result for that will be ['sd','sd','sddd','sddd','sd','sddd']


# if I want to find if is followed by either one or more s and one or more d
# then use ['s[sd]+'] here it will give the result for the s followed by either one or more s or d


######@@@@@@@@@@@@@@@@@$$$$$$$$$$#######
# to exlude terms we use this
def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
test_patterns = ['[^!.?]+']
multi_re_find(test_patterns,test_phrase)
 # ^  ---> this symbol is used to remove 
 
 # if i want to resturn the sequence of lower case character then i will use
# ['[a-z]+'] now i will get in return sequence of lower case character
# ['[A-Z]+']  for uppercase pattern

# for the sequence of digits use [r'\d+']
# for the sequence of non-digits use [r'\D+']
# for the sequence of white spaces use [r'\s+']
# for non spaces use [r'\s+']
# ---------> for example
def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
test_patterns = [r'\s+']
multi_re_find(test_patterns,test_phrase)

# for the alpha numeric use [r'\w']
# for non alpha numeric use [r'\W']
# spaces comes into the section of non-aplha numeric along with special symbols
def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
test_patterns = [r'\w+']
multi_re_find(test_patterns,test_phrase)