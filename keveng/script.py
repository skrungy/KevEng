class Script():

    __active = True
    __started = False

    def __init__(self):
        pass

    def setup():
        pass

    def update():
        pass

    def tick(this):
        if (this.__active):
            if (this.__started == False):
                this.__started = True
                this.setup()
            this.update()