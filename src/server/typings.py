from pydantic import BaseModel


class EncodeRequest(BaseModel):
    inputs: str | list[str]
