
class ConfigService:

    configs = None

    def __init__(self) -> None:
        self.configs = {
            "foo":"bar",
            "service":"proxy",
            "firstname":"Mario",
            "lastname":"Bros"
        }

    def get_config(self, key):
        return self.configs[key]