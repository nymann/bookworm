from bookworm.api import Api
from bookworm.core.config import Config
from bookworm.core.service_container import ServiceContainer

config = Config()
service_container = ServiceContainer(config=config)
api = Api(config=config, service_container=service_container).api
