from dependency_injector import containers
from dependency_injector.providers import DependenciesContainer


class RegistriesContainer(containers.DeclarativeContainer):
    repositories = DependenciesContainer()
