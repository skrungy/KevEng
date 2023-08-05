# this will be behind everything
import pickle

class App:

    active_scene = None # perfectly fine as objects are stored as pointers, so "duping" isnt an issue
    __exit_bool = False

    def __setup(): # to be defined
        pass
    
    def __update(): # to be defined
        pass
    
    def load_scene(this, path):
        with open(path, "rb") as f:
            this.active_scene = pickle.load(f)
            f.close()
        # extra code idk

    # app control stuff
    def exit_app(this):
        this.__exit_bool = True
    
    def run(this):

        this.__setup()
        while (this.__exit_bool):
            this.__update()
        