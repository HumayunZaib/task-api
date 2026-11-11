from sqlalchemy import Column, Integer, String, Boolean
from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
class Task(Base):
    __tablename__ = "tasks"
    owner = Column(String, ForeignKey("users.username"))
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)