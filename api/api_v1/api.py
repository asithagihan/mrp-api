from fastapi import APIRouter

from .endpoints import accounts, integrations, items

router = APIRouter()
router.include_router(accounts.router, prefix="/accounts", tags=["Accounts"])
router.include_router(
    integrations.router, prefix="/integrations", tags=["Integrations"]
)
router.include_router(items.router, prefix="/items", tags=["Items"])
