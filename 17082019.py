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

def subFunc():
    return cls().insMethod

def parentFun(inputFun):
    sf = inputFun()
    sf()



if __name__ == "__main__":
    parentFun(subFunc)