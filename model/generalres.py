from pydantic import BaseModel
from fastapi.responses import JSONResponse

class GeneralMessage(BaseModel):
    status: int
    message: str


USER_CREATED = JSONResponse(content= GeneralMessage(status= 201, message= "User Created Successfully").__dict__, status_code= 201)