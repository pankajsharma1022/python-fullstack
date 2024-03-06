#try:
#    f = open('file.txt', 'r')
#    f.write("Test write to sample text")
#except IOError:
#    print("ERROR: COULD  NOT FIND FILE OR READ DATA")
#else:
#    print("SUCCESS!")
#    f.close()
#print("hello world!")            

#############
try:
    f=open('file.txt','r')
    f.write('Test write to simple text')
except:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
finally:
    print("I always work no matter what!")
            