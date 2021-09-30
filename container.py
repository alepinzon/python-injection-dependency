import os
from dependency_injector import containers, providers
from api_client import ApiClient
from service import Service
from config import ConfigService

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    api_client = providers.Singleton(
        ApiClient,
        api_key=os.getenv('API_KEY'),
        timeout=os.getenv('TIMEOUT'),
    )

    configService = providers.Singleton(
        ConfigService
    )

    service = providers.Factory(
        Service,
        api_client=api_client,
    )