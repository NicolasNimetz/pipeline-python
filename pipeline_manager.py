class PipelineManager(object):

    def __init__(self, *handlers):
        super(PipelineManager, self).__init__()
        self.global_context = {}

    def __call__(self, items, *handlers):
        for handler in handlers:
            stage = handler(items, self.global_context)
            items = stage()
