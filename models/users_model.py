from pydantic import BaseModel

# Creating model for the user


class User(BaseModel):
    given_name: str
    last_name: str
    email: str
    password: str

    # class Config:
    #     orm_mode = True
