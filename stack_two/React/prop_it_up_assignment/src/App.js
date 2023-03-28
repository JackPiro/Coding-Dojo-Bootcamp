import logo from './logo.svg';
import './App.css';
import PersonCard from './components/PersonCard';

function App() {
  return (
    <div className="App">
      <PersonCard firstName = {"Jane"} lastName = {"Doe"} age = {10} hairColor = {'Red'}></PersonCard>
      <PersonCard firstName = {"Jack"} lastName = {"Piro"} age = {20} hairColor = {'blue'}></PersonCard>
      <PersonCard firstName = {"Em"} lastName = {"Schulze"} age = {21} hairColor = {'green'}></PersonCard>
    </div>
  );
}

export default App;
