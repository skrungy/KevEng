from .node import *

class Scene():                              # not inheriting Node since Scenes don't have a parent
                                            # also has active childs (for rendering and active scripts idk)
    activeChilds = {}
    childNodes = {}

    def __init__(self, name):
        self.name = name

    def make_active(self, object):
        self.activeChilds.append(object)
    
    def make_inactive(self, object):
        self.activeChilds.remove(object)
    
    def adoptChild(self, child):            # tweaked version of the Node.adoptChild method to avoid scenes including themselves
        if type(child) == type(self):
            raise Exception("Cannot adopt Scene object as child node for Scene object")
        
        self.childNodes.append(child)
        child.parentNode = self
    
    def killChild(self, child):
        self.childNodes.append(child)
        child.parentNode = self             # debating whether to make the parent node the scene itself, since the child node is technically
                                            # in the highest hierarchy of the scene
    