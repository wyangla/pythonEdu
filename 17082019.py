'''
basic ideas of:
    1. object
    2. class
    3. instance
    4. property
    5. methods
'''

# OO object oriented

class cls(object):
    
    clsProperty = -2
    
    def __init__(self, inputProperty):
        self.insProperty = inputProperty
        
    def insMethod(self):
        print(self.insProperty)
        
    @classmethod
    def clsMethod(cls):
        print(cls.clsProperty)


def subFunc():
    cls.clsMethod()
    ins = cls(3)
    ins.insMethod()
    return cls(1).insMethod

def parentFunc(inputFunc):
    sf = inputFunc()
    sf()



if __name__ == "__main__":
    parentFunc(subFunc)