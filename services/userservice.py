from fastapi import Depends
from utils.config.database import get_db
from schema.usermodels import User
from sqlalchemy.orm import Session
from model.userschema import RegisterUser
from utils.config.hashing import Hashing
from fastapi.exceptions import RequestValidationError, HTTPException
from exceptions.request_validation import EMAIL_EXISTS
from model.generalres import USER_CREATED
from fastapi.responses import JSONResponse

class UserService:

    def get_allUser(self, db: Session):
        return db.query(User).all()
    
    def get_user(self, email: str, db: Session = Depends(get_db)):
        return db.query(User).filter(User.email == email).first()

    def create_user(self, user: RegisterUser, db: Session = Depends(get_db)):
        # Verify User Email
        if self.get_user(email= user.email, db= db) != None:
            raise EMAIL_EXISTS
        
        db_user = User(
            name=user.name,
            email=user.email,
            password=Hashing.bcrypt(user.password),
            is_staff=user.is_staff,
            is_active=user.is_active,
        )
        db.add(db_user)
        db.commit()

        db.refresh(db_user)
        db_user.password = None

        return USER_CREATED
    
    def update_user(self, userid: int, user: RegisterUser, db: Session):
        db_userid = db.query(User).filter(User.id == userid).first()

        db_userid.name = user.name
        db_userid.email = user.email
        db_userid.password = Hashing.bcrypt(user.password)
        db_userid.is_staff = user.is_staff
        db_userid.is_active = user.is_active

        db.commit()

        return db_userid
    
    def deleteUser(self, userid: int, db: Session):
        db_userid = db.query(User).filter(User.id == userid).first()

        db.delete(db_userid)

        db.commit()

        return db_userid