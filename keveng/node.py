class Node():

    childNodes = {}
    parentNode = None

    def __init__(self, name):
        self.name = name
    
    def adoptChild(self, child):
        self.childNodes.append(child)
        child.parentNode = self
    
    def killChild(self, child):
        self.childNodes.remove(child)
        child.parentNode = None