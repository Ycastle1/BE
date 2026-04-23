from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.deps import require_role
from app.models.user import User, UserRole
from app.schemas.user import RoleUpdate, UserRead

router = APIRouter(
    prefix="/professor",
    tags=["professor"],
    dependencies=[Depends(require_role(UserRole.professor))],
)


@router.get("/users", response_model=list[UserRead])
def list_users(db: Session = Depends(get_db)):
    return db.scalars(select(User).order_by(User.user_id)).all()


@router.patch("/users/{user_id}/role", response_model=UserRead)
def update_role(user_id: str, body: RoleUpdate, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    user.role = body.role
    db.commit()
    db.refresh(user)
    return user
