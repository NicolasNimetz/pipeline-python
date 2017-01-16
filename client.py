from pipeline_manager import PipelineManager
from handler_1 import Handler1
from handler_2 import Handler2
from handler_3 import Handler3


class Client(object):

    def __init__(self):
        super(Client, self).__init__()
        self.pipeline = PipelineManager()

    def __call__(self, items):
        print('Client: run Pipeline')
        self.pipeline(
            items,
            Handler1,
            Handler2,
            Handler3,
        )


if __name__ == "__main__":
    client = Client()
    client([
        'Test un tweet de 140 caracteres!',
        'Travailler avec python!',
        'Faire des tests!',
    ])
