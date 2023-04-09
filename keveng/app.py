# this will be behind everything

class App:

    scenes = []
    active_scene = None
    exitBool = False

    def __init__():
        pass

    def setup():
        pass
    
    def update():
        pass

    def exit_app(this):
        this.exitBool = True
    
    def run(this):

        this.setup()
        while (this.exitBool):
            this.update()
        