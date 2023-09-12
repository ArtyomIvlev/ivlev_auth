from fastapi import APIRouter


router = APIRouter(
    prefix="/api/v0/auth",
    tags=["Auth"]
)


@router.get("/")
async def home(name: str):
    return f'Hello, {name}'
