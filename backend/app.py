from typing import List

from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models
from models import Todo
from pydantic_models.Todo import TodoCreate, TodoResponse

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
# List Todos
@app.get("/api/todo/list", response_model=List[TodoResponse], status_code=status.HTTP_200_OK)
def get_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()

# New Todo
@app.post("/api/todo/new", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def new_todo(todo_in: TodoCreate, db: Session = Depends(get_db)):
    print(">>>> Attempting to add todo: ", todo_in)
    new_todo = Todo(title=todo_in.title)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo

# Update Todo
@app.patch("/api/update/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, db: Session = Depends(get_db)):
    print(">>>> Attempting to update todo: ", todo_id)
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.complete = not todo.complete
    db.commit()

    return todo


# Delete todo
@app.delete("/api/delete/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    print(">>>> Attempting to delete todo: ", todo_id)
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()

    return {"message": "Todo deleted"}
