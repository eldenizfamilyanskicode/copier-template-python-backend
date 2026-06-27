from base_pydantic_schemas import BaseDocument

from app.schemas.typings.ids import ExampleId
from app.schemas.typings.integers import ExampleInteger
from app.schemas.typings.strings import ExampleString


class ExampleDocument(BaseDocument):
    example_id: ExampleId
    name: ExampleString
    count: ExampleInteger
