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
    
    clsProperty = -2
    
    def __init__(self):
        self.insProperty = -1
        
    def insMethod(self):
        self.insProperty = 1
        print(self.insProperty)
        
    @classmethod
    def clsMethod(cls):
        print(cls.clsProperty)


def subFunc():
    cls.clsMethod()
    return cls().insMethod

def parentFunc(inputFunc):
    sf = inputFunc()
    sf()



if __name__ == "__main__":
    parentFunc(subFunc)