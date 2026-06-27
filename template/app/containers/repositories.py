from dependency_injector import containers
from dependency_injector.providers import DependenciesContainer


class RepositoriesContainer(containers.DeclarativeContainer):
    adapters = DependenciesContainer()
