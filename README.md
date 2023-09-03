# **Falcon_LLM**

## **Требования**: 
#### - Linux 
#### - Для использования LLM с Falcon-40B необходимо наличие GPU, так как LLM требует высокой графической производительности. Вам потребуется не менее 85-100 ГБ оперативной памяти для быстрого выполнения логического вывода с Falcon 40B.
### GPU:
#### - 2x RTX 6000 Ada (не A6000 или RTX 6000)
#### - 2x A6000 – более бюджетное
### CPU:
#### - 8 ядер.
#### - Например Intel Core i9-11900K или аналогичный AMD Ryzen 9 5900X

### Библиотеки:
#### - Для клиента на JS: axios.
#### - Для FastAPI: fastapi.
#### - Для Falcon: asyncio, nats.
```
python -m pip install -r requirements.txt
```
## **Инструкция для использования локальной копии модели Falcon 40B**
### NATS
#### - Позволяет надежно, быстро и гибко обмениваться сообщениями между API сервером и Falcon 40B.
#### Команда запуска:
```
docker run --network host -p 4222:4222 nats -js
```


### Falcon 40B


### API сервер


### Клиент JS
