const axios = require('axios');
const dotenv = require('dotenv');

// Загрузите переменные окружения из файла .env
dotenv.config();

// Чтение переменных окружения из .env
const apiUrl = process.env.API_URL; // Замените на имя переменной из .env
const bearerToken = process.env.SECRET_TOKEN; // Замените на имя переменной из .env

async function sendRequest(prompt) {
  try {
    const response = await axios.post(
      apiUrl,
      { prompt },
      {
        headers: {
          Authorization: `Bearer ${bearerToken}`,
        },
      }
    );

    if (response.status === 200) {
      console.log('Response from API:', response.data.response);
    } else {
      console.error('API request failed:', response.statusText);
    }
  } catch (error) {
    console.error('Error sending API request:', error.message);
  }
}

const userPrompt = 'Translate: I love programming.'; // Замените на ваш запрос
sendRequest(userPrompt);
