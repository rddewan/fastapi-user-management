
from typing import Annotated
from fastapi import Depends, status
from app.core.router.router import get_versioned_router
from app.features.admin.country.application.country_service import CountryService
from app.features.admin.country.interface.dependencies import get_country_service
from app.features.admin.country.interface.mappers.map_create_country_schema_to_entity import mapCreateCountrySchemaToEntity
from app.features.admin.country.interface.mappers.map_update_country_schema_to_entity import mapUpdateCountrySchemaToEntity
from app.features.admin.country.interface.schemas import CountryListResponse, CountryResponse, CreateCountryRequest, UpdateCountryRequest
from app.features.admin.country.domain.country_entity import CountryEntity

v1_router = get_versioned_router("v1")

@v1_router.get("/admin/countries", status_code=status.HTTP_200_OK)
def get_countries(
    country_service: Annotated[CountryService, Depends(get_country_service)]
) -> CountryListResponse:
    # call the service method to get the countries
    result = country_service.get_all_countries()
    # return CountryListResponse(status="success", data=result) 
    return CountryListResponse(status="success", data=result)



@v1_router.get("/admin/countries/{country_id}", status_code=status.HTTP_200_OK)
def get_country_by_id(
    country_id: int,
    country_service: Annotated[CountryService, Depends(get_country_service)]
) -> CountryResponse:
    # call the service method to get the country by the country id
    result = country_service.get_country_by_id(country_id)
    # return CountryResponse(status="success", data=result) 
    return CountryResponse(status="success", data=result)

@v1_router.post("/admin/countries", status_code=status.HTTP_201_CREATED)
def create_country(
    data: CreateCountryRequest,
    country_service: Annotated[CountryService, Depends(get_country_service)]
) -> CountryResponse:
    # map the request to entity
    country_entity = mapCreateCountrySchemaToEntity(data)
    
    # call the service method to create the country
    result = country_service.create_country(country_entity)
    # return CountryResponse(status="success", data=result) 
    return CountryResponse(status="success", data=result)

@v1_router.patch("/admin/countries/{country_id}", status_code=status.HTTP_200_OK)
def patch_country(
    country_id: int,
    data: UpdateCountryRequest,
    country_service: Annotated[CountryService, Depends(get_country_service)]
) -> CountryResponse:
    # map the request to entity
    country_entity = mapUpdateCountrySchemaToEntity(data)
    # call the service method to patch the country
    result = country_service.update_country(country_id, country_entity)
    # return CountryResponse(status="success", data=result) 
    return CountryResponse(status="success", data=result)

@v1_router.delete("/admin/countries/{country_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_country(
    country_id: int,
    country_service: Annotated[CountryService, Depends(get_country_service)]
) -> None:
    # call the service method to delete the country
    country_service.delete_country(country_id)
    # return CountryResponse(status="success", data=result) 
    # return CountryResponse(status="success", data=result)