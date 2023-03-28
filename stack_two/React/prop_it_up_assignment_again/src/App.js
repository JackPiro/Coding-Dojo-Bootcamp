import logo from './logo.svg';
import './App.css';
import PersonCard from './components/PersonCard'

function App() {
  return (
    <div className="App">
      <PersonCard firstName = {'Jack'} lastName = {'Piro'} hairColor = {'brown'}></PersonCard>
      <PersonCard firstName = {'Em'} lastName = {'Schulze'} hairColor = {'green'}></PersonCard>
    </div>
  );
}

export default App;
