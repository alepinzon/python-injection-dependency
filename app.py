
from blueprint import Blueprint
from container import Container
from constructs import log_group, ecs

class App():

    def __init__(self) -> None:
        Blueprint()
       
if __name__ == '__main__':
    container = Container()
    container.wire(modules=[ecs, log_group])

    App()