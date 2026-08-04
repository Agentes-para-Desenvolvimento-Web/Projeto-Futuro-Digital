from pydantic import BaseModel, EmailStr, ConfigDict


class UserBase(BaseModel):
    username: str
    email: EmailStr
    celular: str | None = None
    cep: str | None = None
    type_user: str = "lead"
    complete_registration: bool = False

class UserCreate(UserBase):
    password:  str

class UserResponse(UserBase):
    id: int


model_config = ConfigDict(from_attributes = True)
