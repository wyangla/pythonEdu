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
    def insMethod(self):
        print(1)

def subFunc():
    return cls().insMethod

def parentFun():
    sf = subFunc()
    sf()



if __name__ == "__main__":
    parentFun()