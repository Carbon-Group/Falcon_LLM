const axios = require('axios');

// Замените следующими значениями ваш токен авторизации и текст запроса
const authToken = 'Ваш_токен_авторизации';
const textRequest = 'Запрос_на_генерацию_текста';

// URL API сервера
const apiUrl = 'https://localhost/generate_text'; // Замените на фактический URL вашего API сервера

// Объект с данными для запроса
const requestData = {
  authToken: authToken,
  textRequest: textRequest,
};

// Отправка POST-запроса
axios.post(apiUrl, requestData)
  .then(response => {
    // Обработка ответа от сервера
    console.log('Ответ от сервера:', response.data);
  })
  .catch(error => {
    // Обработка ошибок
    console.error('Произошла ошибка:', error);
  });
