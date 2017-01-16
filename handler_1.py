from handler import Handler

class Handler1(Handler):

    def instruction(self):
        return 'Transform text on uppercase'

    def do_process(self, index, item):
        super(Handler1, self).do_process(index, item)
        self.local_context[index] = "something i need to share with other stages."
        return item.upper()
