from fastapi import APIRouter

from app.schemas.version import VersionResponse

router = APIRouter(prefix="/version", tags=["version"])


@router.get("/", name="Version", description="Get application version", response_model=VersionResponse)
async def versao():
    return {"version": "1.0.0"}

