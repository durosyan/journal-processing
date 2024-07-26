import React from 'react';
import { createRoot } from 'react-dom/client';
// import './index.css';
import App from './App.tsx';

const node = document.getElementById('root');

if (node) {
    createRoot(node).render(
        <React.StrictMode>
            <App />
        </React.StrictMode>
    );
}
