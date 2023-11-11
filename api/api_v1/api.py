from fastapi import APIRouter

from .endpoints import accounts, integrations

router = APIRouter()
router.include_router(accounts.router, prefix="/accounts", tags=["Accounts"])
router.include_router(
    integrations.router, prefix="/integrations", tags=["Integrations"]
)
