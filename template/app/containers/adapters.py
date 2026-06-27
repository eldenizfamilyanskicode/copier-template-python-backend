from dependency_injector import containers
from dependency_injector.providers import DependenciesContainer


class AdaptersContainer(containers.DeclarativeContainer):
    clients = DependenciesContainer()
    config = DependenciesContainer()
