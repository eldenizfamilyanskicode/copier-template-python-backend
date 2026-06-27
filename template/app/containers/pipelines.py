from dependency_injector import containers
from dependency_injector.providers import DependenciesContainer


class PipelinesContainer(containers.DeclarativeContainer):
    orchestrators = DependenciesContainer()
