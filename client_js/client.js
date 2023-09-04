const axios = require('axios');

// URL вашего API сервера
const apiUrl = 'http://localhost:8000/process_request/';

// Bearer токен для аутентификации
const bearerToken = 'your_secret_token'; // Замените на ваш реальный токен

// Функция для отправки запроса к API серверу
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

// Пример использования
const userPrompt = 'Translate: I love programming.'; // Замените на ваш запрос
sendRequest(userPrompt);
