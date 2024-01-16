from fastapi_router_controller import Controller
from fastapi import APIRouter,Depends
from utils.logger import Logger
from services.userservice import UserService
from utils.config.database import get_db
from sqlalchemy.orm import Session
from model.usermodel import RegisterUser
from schema.userschema import User
from environment.router.urls import URLs

logger = Logger()

base_router = APIRouter(prefix= URLs.user, tags=["Users"])
controller = Controller(base_router, openapi_tag={'name': 'chatbot-controller'})

@controller.use()
@controller.resource()
class UserController: 

    def __init__(self, userService: UserService = Depends(UserService)) -> None:
        self.service = userService
    
    @controller.route.get("/", tags=['Users'])
    def getAllUser(self, db: Session = Depends(get_db)):
        return self.service.get_allUser(db= db)

    @controller.route.post('/', tags=['Users'])
    def createUser(self, user: RegisterUser, db: Session = Depends(get_db)):
        return self.service.create_user(user= user, db= db)

    @controller.route.get('/me', tags=['Users'])
    def getMe(self, current_user: User = Depends()):
        pass

    @controller.route.put('/{userID}', tags=['Users'])
    def updateUser(self, userID: str, user: RegisterUser, db: Session = Depends(get_db)):
        return self.service.update_user(userid= userID, user= user, db= db)

    @controller.route.delete("/{userID}", tags=['Users'])
    def deleteUser(self, userID: str, db: Session = Depends(get_db)):
        return self.service.deleteUser(userid= userID, db= db)
