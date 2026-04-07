import React, { useState } from 'react';

const InputForm = () => {
    const [input, setInput] = useState('');

    const handleChange = (e) => {
        setInput(e.target.value);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Form submitted with input:', input);
        // Additional logic to handle form submission can be added here.
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Generate circuit requirements:
                <input type="text" value={input} onChange={handleChange} />
            </label>
            <button type="submit">Submit</button>
        </form>
    );
};

export default InputForm;