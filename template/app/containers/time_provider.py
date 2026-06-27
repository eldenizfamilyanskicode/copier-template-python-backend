from dependency_injector import containers
from dependency_injector.providers import Dependency


class TimeProviderContainer(containers.DeclarativeContainer):
    monotonic_clock: Dependency[object] = Dependency()
    wall_clock: Dependency[object] = Dependency()
