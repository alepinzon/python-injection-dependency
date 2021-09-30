from api_client import ApiClient

class Service:

    def __init__(self, api_client: ApiClient):
        self.api_client = api_client  # <-- dependency is injected

    def display_api_key(self):
        return self.api_client.get_api_key()

    def display_timeout(self):
        return self.api_client.get_timeout()

    def display_upper_name(self, name):
        return self.api_client.get_upper_name(name)