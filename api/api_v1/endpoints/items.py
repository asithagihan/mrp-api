from fastapi_crudrouter import SQLAlchemyCRUDRouter
from models.item import Item as ItemModel
from schemas.item import Item, ItemCreate
from database import get_db


router = SQLAlchemyCRUDRouter(
    schema=Item, create_schema=ItemCreate, db_model=ItemModel, db=get_db, paginate=10
)


# @router.get("/zoho/sync", response_model=list[Integration])
# def get(
#     skip: int = 0,
#     limit: int = 100,
#     db: Session = Depends(get_db),
# ):
#     return []
