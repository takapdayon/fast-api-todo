from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy import Column, DateTime, Integer, String, Boolean
from database import Base
from models import MixinModel

class Todo(Base, MixinModel):
    __tablename__ = 'todo'

    user_id = Column(Integer, ForeignKey("users.id"))
    task = Column(String(256))
    deadline = Column(DateTime, nullable=False)
    is_done = Column(Boolean, default=False, nullable=False)