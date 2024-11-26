import axios from 'axios';

const BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost';

export const authService = {
  async login(username, password) {
    try {
      const response = await axios.post(`${BASE_URL}:5000/login`, { 
        username, 
        password 
      });
      return response.data;
    } catch (error) {
      throw error.response ? error.response.data : new Error('Login failed');
    }
  },

  async register(username, password) {
    try {
      const response = await axios.post(`${BASE_URL}:5001/register`, { 
        username, 
        password 
      });
      return response.data;
    } catch (error) {
      throw error.response ? error.response.data : new Error('Registration failed');
    }
  }
};