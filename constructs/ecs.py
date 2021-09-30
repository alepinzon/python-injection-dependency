from constructs.log_group import LogGroup
from service import Service
from config import ConfigService
from dependency_injector.wiring import inject, Provide

class ECS():

    @inject
    def __init__(self, 
            name:str = None, 
            age: int = 0, 
            service: Service = Provide['service'], 
            configService:ConfigService = Provide['configService']) -> None:

        self.name = name
        self.age = age
        self.service = service
        self.configService = configService
        self.LogGroup = None

    def say_hi(self):
        if self.name == None:
            firstname = self.configService.get_config('service')
            self.name = self.service.display_upper_name(firstname)
        return "Hola {0}, with {1} age".format(self.name, self.age)


    def get_from_log_group(self):
        if self.LogGroup == None:
            self.LogGroup = LogGroup()

        return "from LogGroup - "+self.LogGroup.get_foo()