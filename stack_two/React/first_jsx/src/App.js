import logo from './logo.svg';
import './App.css';
import React from 'react';
// allows us to write JSX

function App() {
  return (
    <div className="App">
      <h1>Hello Dojo!</h1>
      <h2>Things i need to do</h2>
      <ul>
        <li>Climb everest</li>
        <li>Feed the dogs</li>
        <li>Learn React</li>
      </ul>
    </div>
  );
}

export default App;
