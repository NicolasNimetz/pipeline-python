import abc

class Handler():
    __metaclass__ = abc.ABCMeta

    def __init__(self, items, global_context):
        self.items = items;
        self.global_context = global_context;
        self.global_context[self.namespace] = {};

    @property
    def namespace(self):
    	return self.__class__.__name__

    @property
    def local_context(self):
        return self.global_context[self.namespace]

    @abc.abstractmethod
    def instruction(self):
        return

    @abc.abstractmethod
    def do_process(self, index, item):
        return

    def get_global_context(self, handler, index):
        return self.global_context[handler][index]

    def __call__(self):
        for i, v in enumerate(self.items):
            self.items[i] = self.do_process(i, v)
            print "Job = {} completed".format(self.instruction())
        print "Completed Task = ", self.__class__.__name__
        return self.items
