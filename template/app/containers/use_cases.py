from dependency_injector import containers
from dependency_injector.providers import DependenciesContainer, Factory

from app.use_cases.example_use_case import ExampleUseCase


class UseCasesContainer(containers.DeclarativeContainer):
    facilitators = DependenciesContainer()
    registries = DependenciesContainer()
    repositories = DependenciesContainer()
    time_provider = DependenciesContainer()
    transformers = DependenciesContainer()
    utilities = DependenciesContainer()

    example_use_case: Factory[ExampleUseCase] = Factory(ExampleUseCase)
