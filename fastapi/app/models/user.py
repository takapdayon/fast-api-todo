from sqlalchemy import Boolean, Column, String
from database import Base
from models import MixinModel

class User(Base, MixinModel):
    __tablename__ = "user"

    username = Column(String(256))
    email = Column(String(256), unique=True, index=True)
    password = Column(String(256))
    is_active = Column(Boolean, default=True)