from fastapi.exceptions import HTTPException
from fastapi import status

EMAIL_EXISTS = HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Email Already Exists !!')

