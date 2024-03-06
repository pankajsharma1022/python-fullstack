class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self):
        return "Title: {}, Auhtor: {}, Pages: {}".format(self.title,self.author,self.pages) 
    def __len__(self):
        return self.pages
    def __del__(self):
        print("not a book")   
b=Book("zindagi","pankaj",4000)
print(b)    
print(len(b))    
del b
# this is the the syntax to directly call the del function
