from handler import Handler

class Handler3(Handler):

    def instruction(self):
        return 'Save text'

    def do_process(self, index, item):
        super(Handler3, self).do_process(index, item)
        return True
