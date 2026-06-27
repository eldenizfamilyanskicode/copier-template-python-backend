from dependency_injector import containers
from dependency_injector.providers import Container

from app.containers.adapters import AdaptersContainer
from app.containers.clients import ClientsContainer
from app.containers.config import ConfigContainer
from app.containers.facilitators import FacilitatorsContainer
from app.containers.gateways import GatewaysContainer
from app.containers.operators import OperatorsContainer
from app.containers.orchestrators import OrchestratorsContainer
from app.containers.pipelines import PipelinesContainer
from app.containers.registries import RegistriesContainer
from app.containers.repositories import RepositoriesContainer
from app.containers.time_provider import TimeProviderContainer
from app.containers.transformers import TransformersContainer
from app.containers.use_cases import UseCasesContainer
from app.containers.utilities import UtilitiesContainer


class AppContainer(containers.DeclarativeContainer):
    config = Container(ConfigContainer)
    clients = Container(ClientsContainer, config=config)
    adapters = Container(AdaptersContainer, clients=clients, config=config)
    repositories = Container(RepositoriesContainer, adapters=adapters)
    registries = Container(RegistriesContainer, repositories=repositories)
    utilities = Container(UtilitiesContainer)
    facilitators = Container(
        FacilitatorsContainer,
        adapters=adapters,
        config=config,
    )
    transformers = Container(TransformersContainer)
    time_provider = Container(TimeProviderContainer)
    use_cases = Container(
        UseCasesContainer,
        facilitators=facilitators,
        registries=registries,
        repositories=repositories,
        time_provider=time_provider,
        transformers=transformers,
        utilities=utilities,
    )
    orchestrators = Container(OrchestratorsContainer, use_cases=use_cases)
    pipelines = Container(PipelinesContainer, orchestrators=orchestrators)
    operators = Container(OperatorsContainer, pipelines=pipelines)
    gateways = Container(GatewaysContainer)
