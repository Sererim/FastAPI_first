from pydantic import BaseModel


class Task(BaseModel):
    Name: str
    Description: str
    Status: bool
