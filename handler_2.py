from handler import Handler

class Handler2(Handler):

    def instruction(self):
        return 'Reverse text'

    def do_process(self, index, item):
        super(Handler2, self).do_process(index, item)
        print self.get_global_context('Handler1', index)
        return item[::-1]
