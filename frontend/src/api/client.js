import axios from 'axios';

// Create an axios instance with default settings for API communication.
const apiClient = axios.create({
    baseURL: 'https://api.example.com', // Replace with your backend API URL
    timeout: 1000,
    headers: {'Content-Type': 'application/json'}
});

export default apiClient;