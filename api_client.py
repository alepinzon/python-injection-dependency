class ApiClient:

    def __init__(self, api_key: str, timeout: str):
        self.api_key = api_key
        self.timeout = timeout

    def get_upper_name(self, name:str):
        return name.upper()

    def get_api_key(self):
        return self.api_key

    def get_timeout(self):
        return self.timeout