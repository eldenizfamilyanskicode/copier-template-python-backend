from dependency_injector import containers
from dependency_injector.providers import DependenciesContainer


class OrchestratorsContainer(containers.DeclarativeContainer):
    use_cases = DependenciesContainer()
