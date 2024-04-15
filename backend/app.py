from typing import List
from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from models import Todo, Base
from pydantic_models.Todo import TodoCreate, TodoResponse
from database import SessionLocal, engine

# Initialize database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Set up CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get database session
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API Routes for CRUD operations on Todo items
@app.get("/api/todo/list", response_model=List[TodoResponse], status_code=status.HTTP_200_OK)
def get_todos(db: Session = Depends(get_db)) -> List[TodoResponse]:
    return db.query(Todo).all()

@app.post("/api/todo/new", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def new_todo(todo_in: TodoCreate, db: Session = Depends(get_db)) -> TodoResponse:
    new_todo = Todo(title=todo_in.title)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@app.patch("/api/todo/update/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, db: Session = Depends(get_db)) -> TodoResponse:
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.complete = not todo.complete
    db.commit()
    return todo

@app.delete("/api/todo/delete/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()