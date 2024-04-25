from sqlalchemy import Boolean, Column, Integer, String, JSON

from database import Base


class Todo(Base):
  __tablename__ = "todos"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  complete = Column(Boolean, default=False)
  variables = Column(JSON)