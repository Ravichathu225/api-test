from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ResponseBody(BaseModel):
    message: str

@router.get("/hello-world")
def hello_world() -> ResponseBody:
    """
    A simple endpoint that returns a greeting message.
    """
    return ResponseBody(message="Hello, World! This is a smoke test endpoint.😒✔")