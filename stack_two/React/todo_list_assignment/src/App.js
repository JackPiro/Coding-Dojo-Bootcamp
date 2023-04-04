import React, { useState } from 'react';
import './App.css';

function App() {
  const [input, setInput] = useState("");
  const [toDos, setToDos] = useState([]);

  const submitHandler = (e) => {
    e.preventDefault();
    setToDos([...toDos, input])
    console.log(toDos);
  }

  return (
    <div className="App">
      <form onSubmit={submitHandler}>
        <label htmlFor='to do input'>write todo here</label>
        <input type = 'text' id = 'to do input' value = {input} onChange = {(e) => setInput(e.target.value)} />
        <input type = 'submit' value = 'add todo' />
      </form>
      {
        (toDos = toDos) => {
          let index = 0;
          while (index <= toDos.length){
            return(
              <div>
                <label htmlFor='item'>{toDos[index]}</label>
                <input type = 'checkbox' id = 'item' />
                <input type = 'button' value = 'delete' onClick={toDos.pop[index]} />
              </div>
            );
          }
          index = index + 1;
        }
      }
    </div>
  );
}

export default App;
