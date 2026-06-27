from base_typed_id import BasePrefixedTypedId, BaseTypedId


class ExampleId(BaseTypedId):
    pass


class ExamplePrefixedId(BasePrefixedTypedId):
    prefix = "example"
