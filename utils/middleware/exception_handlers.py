from fastapi import Request
from schema.errors import Errors, throw_error
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi import status

from utils.logger import Logger
logger = Logger.get_logger(__name__)

def validation_exception_handler(_: Request, exc: RequestValidationError):
    try:
        error = exc.errors()
        return throw_error(status= status.HTTP_400_BAD_REQUEST, message="Validation Error", error= error['msg'])
    except:
        return throw_error(status= status.HTTP_400_BAD_REQUEST, message="Validation Error", error= str(error))

async def exception_handler(req: Request, exc: Exception):
    func_handler = req.state.func_name
    
    logger.error('An error occured during {} handling. Error: {}'.format(func_handler, exc))
    return throw_error(status= status.HTTP_500_INTERNAL_SERVER_ERROR, message= "An error occured", error_code= 500, error= str(exc) )

async def http_exception_handler(req: Request, exc: HTTPException):
    return throw_error(status= exc.status_code, message= exc.detail, error= "")