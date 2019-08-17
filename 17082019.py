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
        
    @classmethod
    def clsMethod_2(cls, inputProperty):
        cls.clsProperty = inputProperty


def subFunc():
    cls.clsMethod()
    
    ins = cls(-3)    # could be anything
    ins.__init__(3)
    ins.insMethod()
    ins.clsMethod_2(2)    # modify the shared cls property

    
    ins_2 = cls(1)
    ins_2.clsMethod()
    return ins_2.insMethod


def parentFunc(inputFunc):
    sf = inputFunc()
    sf()



if __name__ == "__main__":
    parentFunc(subFunc)