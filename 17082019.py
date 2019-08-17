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
    def clsMethod(self):
        print(1)

def subFunc():
    return cls().clsMethod

def parentFun():
    sf = subFunc()
    sf()



if __name__ == "__main__":
    parentFun()