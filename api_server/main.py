import asyncio
import nats.aio.client as nats
from fastapi import FastAPI, Depends, HTTPException, Header
from dotenv import load_dotenv  # Добавьте эту строку

# Загрузите переменные окружения из файла .env
load_dotenv()

app = FastAPI()

# Задайте токен, который будет использоваться для аутентификации клиентов
SECRET_TOKEN = os.getenv("SECRET_TOKEN")  # Извлеките токен из переменных окружения

# Инициализация соединения с NATS
async def initialize_nats_connection():
    nc = nats.Client()
    await nc.connect(os.getenv("NATS_URL"))  # Извлеките адрес NATS из переменных окружения
    return nc

# Зависимость для проверки Bearer token
def check_token(authorization: str = Header(None)):
    if authorization is None:
        raise HTTPException(status_code=401, detail="Bearer token is missing")
    if authorization != f"Bearer {SECRET_TOKEN}":
        raise HTTPException(status_code=403, detail="Bearer token is invalid")

# Эндпоинт для получения запросов и возвращения ответов
@app.post("/process_request/")
async def process_request(request_body: dict, nc: nats.Client = Depends(initialize_nats_connection), token: str = Depends(check_token)):
    try:
        # Отправляем запрос на модель через NATS
        response = await nc.request("user_requests", payload=str(request_body).encode(), timeout=5)
        return {"response": response.data.decode()}
    except nats.NatsError as e:
        raise HTTPException(status_code=500, detail=f"NATS error: {str(e)}")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host=os.getenv("API_HOST"), port=int(os.getenv("API_PORT")))  # Извлеките хост и порт из переменных окружения
