from fastapi import FastAPI, Request, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

import models
from models import Todo
from pydantic_models.Todo import TodoCreate

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

# CRUD for API
@app.get("/api/todo/list")
def get_todos(db: Session = Depends(get_db)):
  todos = db.query(Todo).all()
  todos_data = [todo.__dict__ for todo in todos]
  # Exclude metadata for serialization
  todos_data = [{k: v for k, v in todo.items() if k != "_sa_instance_state"} for todo in todos_data]
  
  return JSONResponse(status_code=status.HTTP_200_OK, content=todos_data)

@app.post("/api/todo/new")
def new_todo(todo_in: TodoCreate, db: Session = Depends(get_db)):
    print(">>>> Attempting to add todo: ", todo_in)
    todo = Todo(title=todo_in.title)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    
    return todo

@app.patch("/api/update/{todo_id}")
def update_todo(request: Request, todo_id: int, db: Session = Depends(get_db)):
  print(">>>> Attempting to update todo id: ", todo_id)
  todo = db.query(Todo).filter(Todo.id == todo_id).first()

  todo.complete = not todo.complete
  todo_data = todo.__dict__
  todo_data = {k: v for k, v in todo_data.items() if k != "_sa_instance_state"}
  db.commit()
  
  return JSONResponse(status_code=status.HTTP_200_OK, content=todo_data)

@app.delete("/api/delete/{todo_id}")
def delete_todo(request: Request, todo_id: int, db: Session = Depends(get_db)):
  print(">>>> Attempting to delete todo id: ", todo_id)
  todo = db.query(Todo).filter(Todo.id == todo_id).first()
  db.delete(todo)
  db.commit()

  return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content={"message": "Todo deleted"})
