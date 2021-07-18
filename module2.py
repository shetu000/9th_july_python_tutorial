

def foo():
    return "welcome in foo()"

def bar():
    return "welcome in bar()"



class Animal:
    def __init__(self,bread):
        self.bread=bread
    def speak(self):
        return "woof!"

if __name__=='__main__':   #this will run individually , it will not works for imported module
    print(foo())
    print(bar())
    d=Animal("dog")
    print(d.speak())
