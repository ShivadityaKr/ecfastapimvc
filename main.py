# just load all the controllers
import controllers
from utils.config import settings
import uvicorn
from utils.middleware import LogIncomingRequest, exception_handler, validation_exception_handler
from utils.middleware.exception_handlers import http_exception_handler
from fastapi import FastAPI, Depends
from fastapi.exceptions import RequestValidationError
from fastapi import HTTPException
from fastapi_router_controller import Controller, ControllersTags


#########################################
#### Configure the main application #####
#########################################
app = FastAPI(
    title= settings.PROJECT_NAME,
    version= settings.PROJECT_VERSION,
    docs_url= settings.PROJECT_API_DOCS,
    openapi_tags=ControllersTags)

# configuring handler for validation error in order to format the response
app.exception_handler(RequestValidationError)(validation_exception_handler)

# configuring handler for generic error in order to format the response
app.exception_handler(Exception)(exception_handler)

# configuring handler for generic error in order to format the response
app.exception_handler(HTTPException)(http_exception_handler)

# add middleware to process the request before it is taken by the router func
app.add_middleware(LogIncomingRequest)
#########################################
#### Configure all the implemented  #####
####  controllers in the main app   #####
#########################################
for router in Controller.routers():
    app.include_router(router)

# Server configuration
if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8001, reload= True, workers= 2)