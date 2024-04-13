import { useState } from "react";

const NewTodo = (props: { getTodos: () => void }) => {

  const [newTodo, setNewTodo] = useState("");

  const addTodo = async () => {
    
    const response = await fetch('http://localhost:8000/api/todo/new', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
      body: JSON.stringify({ title: newTodo }),
    });
    const data = await response.json();
    console.log(data);
    setNewTodo("");
    props.getTodos();
  }

  const handlePressEnter = (e:React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') addTodo() 
  }

  const handleOnChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setNewTodo(e.target.value)
  }

  return (
    <div className="flex justify-center">
      <input className="w-1/3 border border-gray-300 rounded py-2 px-4" 
        placeholder="Ingresa tu tarea y presiona Enter" 
        onChange={handleOnChange} 
        onKeyDown={handlePressEnter} 
        value={newTodo}
        type="text" />
      <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 ml-2 rounded"
        onClick={addTodo}
      >Agregar</button>
    </div>
  )
}

export default NewTodo