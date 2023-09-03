from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

# Секретный ключ для проверки Bearer token
SECRET_KEY = "your_secret_key"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Функция для проверки токена
def authenticate_user(token: str = Depends(oauth2_scheme)):
    if token != SECRET_KEY:
        raise HTTPException(status_code=401, detail="Bearer token is invalid")

# Ендпоинт для отправки запросов к модели
@app.post("/generate_text/")
async def generate_text(request_data: dict, auth=Depends(authenticate_user)):
    # Отправляем запрос на NATS для генерации текста
    async def send_request():
        nc = await nats.connect()
        response = await nc.request("text_generation_requests", json.dumps(request_data).encode())
        return response

    response = await send_request()
    return response.data.decode()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
