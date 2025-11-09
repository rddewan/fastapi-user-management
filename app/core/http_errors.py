
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.exceptions.repository import ConnectionFailure, RepositoryException, TransactionFailure, UniqueConstraintFailure

def register_exception_handler(app: FastAPI):

    """
    Register exception handlers for repository exceptions.
    """
    @app.exception_handler(RepositoryException)
    async def handle_repository_exception(request: Request, exception: RepositoryException): # type: ignore

        if isinstance(exception, ConnectionFailure):
            code = "DB_CONNECTION_FAILURE"
        elif isinstance(exception, TransactionFailure):
            code = "DB_TRANSACTION_FAILURE"
        elif isinstance(exception, UniqueConstraintFailure):
            code = "DB_UNIQUE_CONSTRAINT_FAILURE"
        else:
            code = "DB_UNKNOWN_FAILURE"

        return JSONResponse(
            status_code=503,
            content={
                "code": code,
                "message": "Database service temporary unavailable",
            }
        )