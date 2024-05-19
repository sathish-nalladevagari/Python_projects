import './App.css';
import React, { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState([]);
  const [showData, setShowData] = useState(false);


  const fetchData = async () => {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos');
    const jsonData = await response.json();
    setData(jsonData);
  };
  const toggleData = () => {
    setShowData(!showData);
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div>
      <button onClick={toggleData}>show data</button>
    {showData &&
      data.map((item, index) => (
        <div key={index}>
          <h1 className='todo-title'>{item.title}</h1>
        </div>
      ))}
  </div>
  );
}

export default App;