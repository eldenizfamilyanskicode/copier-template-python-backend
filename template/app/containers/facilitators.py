from dependency_injector import containers
from dependency_injector.providers import DependenciesContainer


class FacilitatorsContainer(containers.DeclarativeContainer):
    adapters = DependenciesContainer()
    config = DependenciesContainer()
