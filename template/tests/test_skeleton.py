from app.containers.app import AppContainer
from app.containers.use_cases import UseCasesContainer
from app.schemas.dto.example_dto import ExampleInputDTO
from app.use_cases.example_use_case import ExampleUseCase


def test_app_container_can_be_created() -> None:
    app_container: AppContainer = AppContainer()
    assert app_container is not None


def test_use_cases_container_builds_example_use_case() -> None:
    use_cases_container: UseCasesContainer = UseCasesContainer()
    example_use_case: ExampleUseCase = use_cases_container.example_use_case()
    output = example_use_case.run(
        ExampleInputDTO(value="example"),
    )

    assert output.value == "example"
