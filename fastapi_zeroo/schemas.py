from pydantic import BaseModel


class Message(BaseModel):
    messege: str
