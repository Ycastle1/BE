from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.deps import get_current_user
from app.core.security import create_access_token
from app.models.user import User
from app.schemas.user import Token, UserCreate, UserLogin, UserRead
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def signup(body: UserCreate, db: Session = Depends(get_db)):
    try:
        return auth_service.create_user(db, body)
    except auth_service.UserIdAlreadyExistsError:
        raise HTTPException(status.HTTP_409_CONFLICT, "User ID already registered")
    except auth_service.EmailAlreadyExistsError:
        raise HTTPException(status.HTTP_409_CONFLICT, "Email already registered")
    except IntegrityError:
        db.rollback()
        raise HTTPException(status.HTTP_409_CONFLICT, "User already registered")


@router.post("/login", response_model=Token)
def login(body: UserLogin, db: Session = Depends(get_db)):
    try:
        user = auth_service.authenticate_user(db, body.email, body.password)
    except auth_service.InvalidCredentialsError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid email or password")
    token, expires_in = create_access_token(user.user_id)
    return Token(access_token=token, expires_in=expires_in)


@router.get("/me", response_model=UserRead)
def me(current: User = Depends(get_current_user)):
    return current
