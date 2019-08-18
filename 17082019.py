'''
basic ideas of:
    1. object
    2. class
    3. instance
    4. property
    5. methods
'''

# OO object oriented
# Q: in python3 can only use class method access class property?

class cls(object):
    
    # 4.5. cls property, cls method; ins property, ins method
    clsProperty = -2
    
    def __init__(self, inputProperty):
        self.insProperty = inputProperty
        
    def insMethod(self):
        print(self.insProperty)
        
    # 3. relationship between instances
    @classmethod
    def clsMethod(cls):
        print(cls.clsProperty)
        
    @classmethod
    def clsMethod_2(cls, inputProperty):
        cls.clsProperty = inputProperty


def subFunc():
    cls.clsMethod()
    
    # 2. relationship between cls and instance
    ins = cls(-3)
    ins.__init__(3)
    ins.insMethod()
    ins.clsMethod_2(2)    # modify the shared cls property

    ins_2 = cls(1)
    ins_2.clsMethod()
    return ins_2.insMethod


# 1. method is object in python
def parentFunc(inputFunc):    
    sf = inputFunc()
    sf()



if __name__ == "__main__":
    parentFunc(subFunc)

print ("hello world")

