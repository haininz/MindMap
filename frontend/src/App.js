import React, { useState } from 'react';
import './App.css';
import MindMap from './MindMap';

function App() {
    const [input, setInput] = useState('');
    const [showMindMap, setShowMindMap] = useState(false);
    const [mindMapData, setMindMapData] = useState(null);

    const handleInputChange = (e) => {
        setInput(e.target.value);
    };

    const handleSubmit = async () => {
        try {
            const response = await fetch('http://127.0.0.1:5000/submit', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ userInput: input })
            });
            const data = await response.json();
            console.log(data);
            setMindMapData(data);
            setShowMindMap(true);
        } catch (error) {
            console.error('Failed to send input:', error);
        }
    };

    return (
        <div className="App">
            <div className="search-wrapper">
                <h1>Mind Map Generation</h1>
                <input
                    type="text"
                    value={input}
                    onChange={handleInputChange}
                    placeholder="Enter your thoughts here"
                />
                <button onClick={handleSubmit}>Submit</button>
                {/* {showMindMap && <MindMap />} */}
                {showMindMap && mindMapData && <MindMap data={mindMapData} />}
            </div>
        </div>
    );
}

export default App;
