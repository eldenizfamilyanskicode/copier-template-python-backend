from dependency_injector import containers
from dependency_injector.providers import DependenciesContainer


class ClientsContainer(containers.DeclarativeContainer):
    config = DependenciesContainer()
