from dependency_injector import containers
from dependency_injector.providers import Singleton

from app.schemas.configurations.example_config import ExampleConfig
from app.utilities.config_helpers.example_config_assembler import get_example_config


class ConfigContainer(containers.DeclarativeContainer):
    example_config: Singleton[ExampleConfig] = Singleton(get_example_config)
