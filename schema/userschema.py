from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from utils.config.database import Base
import uuid


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True, default=str(uuid.uuid4()))
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)

    # reviews = relationship("ReviewModel", back_populates="user")

    def __repr__(self):
        return f"<User {self.email}"
