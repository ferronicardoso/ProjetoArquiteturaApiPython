from fastapi import APIRouter

from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{user_id}", name="Get user by Id", response_model=UserResponse)
async def get_user_by_id(user_id: int):
    return {"id": 1, "name": "John Doe", "email": "john@example.com"}


@router.post("/", name="Create a new user")
async def create_new_user(user: UserCreate):
    return user
