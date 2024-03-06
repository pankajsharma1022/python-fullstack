#python scope follows the LEGB rule
x=25
#def my_func():
#    x=50
#    return x
#print(x)
# here this print is calling global variable x
#print(my_func())
# here my_func() is calling local variable x which is inside of function my_fun
# LOCAL
#lambda x:x**2
# ENCLOSING function local
#name='This is a global name!'
#def greet():
#    name="sammy"
#    def hello():
#        print("hello "+name)
#    hello()    
#greet()       
# it will first look for the local variable and if it is 
# not there then it will call the global variable or function if available
#x=50
#def func(x):
#    print('x is ',x)
#    x=100
#    print('local x is changed to:',x)
#func(x)
#print(x)
def func():
    global x
    x=1000
print("before function call, x is:",x)
func()
print("after function call, x is:",x)
# by using global keyword i can change the values globally 
# or i change the them entirely

     