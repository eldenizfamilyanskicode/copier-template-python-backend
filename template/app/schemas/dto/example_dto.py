from base_pydantic_schemas import MutableDTO


class ExampleInputDTO(MutableDTO):
    value: str


class ExampleOutputDTO(MutableDTO):
    value: str
