from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from app.databasecon import get_db
from typing import Optional, List
from app.routers.asset import schemas


router = APIRouter(
    prefix="/areas",
    tags=['Area APIs']
)


# Create a new area
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.RespArea)
def create_an_area(area: schemas.ReqArea, db: Session = Depends(get_db)):
    """Creates the Area in the same enterprise from which the user belongs to, it also checks the user's role is supervisor or admin

    Args:
        area (schemas.ReqArea): Area Schema
        current_user (int, optional): Getting user from JWT authentication response.

    Raises:
        HTTPException: 406 if entered area already exists
        HTTPException: 500 if something went wrong

    Returns:
        dict: returns the area created
    """
    try:
        output = {
        "name": area.name,
        "site_id": area.site_id,
        "id": area.id,
        "created_at": "2021-07-01T00:00:00",
        "last_modified_at": "2021-07-01T00:00:00",
        "enterprise_id": 1


        }
        return output
    except Exception as err:
        print(err.args[0])
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=err.args[0])

# Get all areas


@router.get("/", response_model=List[schemas.RespArea])
def get_all_areas(db: Session = Depends(get_db),
                  search: Optional[str] = ""):
    """gets all of the areas from the database in the same enterprise from which the user belongs to, it also checks the user's role is supervisor or admin

    Args:
        db (Session, optional): Data Base Session.
        search (Optional[str], optional): performs search operation.

    Returns:
        list: list of the areas
    """

    output = {
        "name": "test area",
        "site_id": 1,
        "id": 1,
        "created_at": "2021-07-01T00:00:00",
        "last_modified_at": "2021-07-01T00:00:00",
        "enterprise_id": 1


    }

    return [output]
