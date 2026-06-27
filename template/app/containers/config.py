from dependency_injector import containers
from dependency_injector.providers import Configuration


class ConfigContainer(containers.DeclarativeContainer):
    config = Configuration()
