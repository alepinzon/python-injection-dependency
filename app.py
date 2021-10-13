
from blueprint import Blueprint
from container import Container
import constructs

class App():

    def __init__(self) -> None:
        Blueprint()
       
if __name__ == '__main__':
    container = Container()
    container.wire(packages=[constructs])

    App()