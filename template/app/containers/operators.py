from dependency_injector import containers
from dependency_injector.providers import DependenciesContainer


class OperatorsContainer(containers.DeclarativeContainer):
    pipelines = DependenciesContainer()
