import asyncio
import nats.aio.client as nats
from fastapi import FastAPI, Depends, HTTPException, Header

app = FastAPI()

# Задайте токен, который будет использоваться для аутентификации клиентов
SECRET_TOKEN = "your_secret_token"

# Инициализация соединения с NATS
async def initialize_nats_connection():
    nc = nats.Client()
    await nc.connect("nats://localhost:4222")
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
    uvicorn.run(app, host="0.0.0.0", port=8000)