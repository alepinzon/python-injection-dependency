from config import ConfigService
from dependency_injector.wiring import inject, Provide

class LogGroup:

    @inject
    def __init__(self, configService:ConfigService = Provide['configService']) -> None:
        self.configService = configService

    def get_foo(self):
        return self.configService.get_config('foo')