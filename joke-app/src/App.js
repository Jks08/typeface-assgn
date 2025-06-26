import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [joke, setJoke] = useState('');
  const [isLoading, setIsLoading] = useState(true);

  const fetchJoke = async () => {
    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:5000/api/joke');
      const data = await response.json();
      setJoke(data.joke);
    } catch (error) {
      console.error('Error fetching joke:', error);
      setJoke('Failed to load joke');
    }
    setIsLoading(false);
  };

  useEffect(() => {
    fetchJoke();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Random Joke Generator</h1>
        <div className="joke-container">
          {isLoading ? (
            <p>Loading...</p>
          ) : (
            <p>{joke}</p>
          )}
        </div>
        <button onClick={fetchJoke}>Get New Joke</button>
      </header>
    </div>
  );
}

export default App;