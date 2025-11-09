from app.core.exceptions.domain import AlreadyExistsException, NotFoundException


class CountryNotFoundException(NotFoundException):
    def __init__(self, entity: str, key: str):
        message = f"{entity} not found with {key}"
        self.message = message

        super().__init__(message)


class CountryAlreadyExistsException(AlreadyExistsException):
    def __init__(self, entity: str, key: str):
        message = f"{entity} already exists with {key}"
        self.message = message
        super().__init__(message)
