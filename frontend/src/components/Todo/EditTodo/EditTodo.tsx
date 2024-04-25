import { useEffect, useRef, useState } from "react";
import { useParams } from 'react-router-dom';

interface Todo {
  id: number;
  title: string;
  complete: boolean;
  variables: {key:number, value: string}[];
}

const EditTodo = () => {

  const { id } = useParams();
  const [ todo, setTodo ] = useState<Todo>();
  const [ result, setResult ] = useState<number | string>();

  const inputRefs = useRef<{ [key: string]: HTMLInputElement | null }>({});
  
  const getTodo = async (id:string) => {
    const response = await fetch(`http://localhost:8000/api/todo/${id}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
    })
    const data = await response.json();
    setTodo(data)
  };

  const onCalculate = () => {

    if (!todo) return
    
    const variables = todo.variables
    let formula = ""
    const letters:string[] = []
    const numbers: number[] = []

    Object.entries(variables).forEach(([key,value]) => {
      console.log("🚀 ~ Object.entries ~ key:", key)
      const inputValue = inputRefs.current[value.toString()]?.value
      letters.push(value.toString())
      numbers.push(Number(inputValue))
    });

    formula += "return "+todo.title+";"
    const toEval = new Function(...letters,formula)
    const evalResult = toEval(...numbers)
    
    if (typeof evalResult === 'number') {
      setResult(evalResult)
    }else{
      setResult("Invalid formula"); return 
    } 
  }

  useEffect(() => {
    getTodo(id!);
  }, [])


  return (
    <div className='container'>
      <div className="card">
        <h2>{todo?.title}</h2>
        {
          todo?.variables ? Object.entries(todo.variables).map(([key,value]) => (
            <div key={key}>
              <label>{value.toString()}</label>
              <input 
                ref={el => inputRefs.current[value.toString()] = el} 
                type="text" 
                className="border ml-2"
              />
            </div>
          ))
          : <p>No variables</p>
        }
        <p>Result: {result}</p>
        <button onClick={onCalculate}>Calculate</button>
      </div>
    </div>
  )
}

export default EditTodo