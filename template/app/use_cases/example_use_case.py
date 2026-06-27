from app.contracts.use_case_contract import UseCaseContract
from app.schemas.dto.example_dto import ExampleInputDTO, ExampleOutputDTO


class ExampleUseCase(UseCaseContract[ExampleInputDTO, ExampleOutputDTO]):
    def run(self, input_data: ExampleInputDTO) -> ExampleOutputDTO:
        return ExampleOutputDTO(name=input_data.name, count=input_data.count)
