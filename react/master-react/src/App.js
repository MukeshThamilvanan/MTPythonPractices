/*
import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>

        <p>
        Project by Mukesh Thamilvanan
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;

*/

// code below from pirple
import React from 'react';

function App(){ // function name can be anything
  // return(
  //   <div>
  //    <h1 ti>heading</h1>
  //    This is JSX 
  //   </div>
  // )

  return React.createElement("h1", {title: "this is a secret text"} , "Heading")
}

export default App; 
// exporting connects this App with the import in index.js 