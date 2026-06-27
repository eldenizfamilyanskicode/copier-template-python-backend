from base_pydantic_schemas import MutableDTO

from app.schemas.typings.integers import ExampleInteger
from app.schemas.typings.strings import ExampleString


class ExampleInputDTO(MutableDTO):
    name: ExampleString
    count: ExampleInteger


class ExampleOutputDTO(MutableDTO):
    name: ExampleString
    count: ExampleInteger
