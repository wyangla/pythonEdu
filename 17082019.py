'''
basic ideas of:
    1. object
    2. class
    3. instance
    4. property
    5. methods
'''

# OO object oriented

class cls():
    def __init__(self):
        self.clsProperty = -1
        
    def insMethod(self):
        self.clsProperty = 1
        print(self.clsProperty)
        
    @classmethod
    def clsMethod(cls):
        print(2)

def subFunc():
    cls.clsMethod()
    return cls().insMethod

def parentFunc(inputFunc):
    sf = inputFunc()
    sf()



if __name__ == "__main__":
    parentFunc(subFunc)