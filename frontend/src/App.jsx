import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Welcome from './pages/Welcome';
import InputForm from './pages/InputForm';
import Results from './pages/Results';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path='/' element={<Welcome />} />
                <Route path='/input' element={<InputForm />} />
                <Route path='/results' element={<Results />} />
            </Routes>
        </Router>
    );
};

export default App;