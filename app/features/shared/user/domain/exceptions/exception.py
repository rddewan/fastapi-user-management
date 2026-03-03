

from app.core.exceptions.domain import AlreadyExistsException, DomainException, NotFoundException


class UserNotFound(NotFoundException):
    def __init__(self, entity: str, key: str):
        message = f"{entity} not found with {key}"
        self.message = message
        super().__init__(message)


class UserAlreadyExistException(AlreadyExistsException):
    def __init__(self, entity: str, key: str):
        message = f"{entity} already exists with {key}"
        self.message = message
        super().__init__(message)
        
        
class InvalidPasswordException(DomainException):
    def __init__(self, message: str = "Invalid password"):        
        self.message = message
        super().__init__(message)