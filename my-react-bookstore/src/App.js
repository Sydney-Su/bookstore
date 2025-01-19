import logo from './logo.svg';
import './App.css';
import AddBookForm from './AddBookForm';


function App() {
  return(
    <div>
      <h1>Welcome to BookNexus</h1>
      <AddBookForm />
    </div>
  );
}

export default App;


/*
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Welcome to BookNexus
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
*/
