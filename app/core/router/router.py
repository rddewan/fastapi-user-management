from fastapi import APIRouter



def get_versioned_router(version: str):
    """
    Get versioned router

    Args:
        version (str): Version

    Returns:
        APIRouter: Versioned router
    """
    return APIRouter(prefix=f"/{version}")  