import asyncio
import nats
import pytest
from model_service.main import main

@pytest.fixture
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

# Тесты для сервиса модели

@pytest.mark.asyncio
async def test_model_service():
    async def simulate_request():
        nc = await nats.connect("nats://localhost:4222")
        await nc.publish("user_requests", b"Translate: I love programming.", reply="response")
        response = await nc.timed_request("response", b"", timeout=5)
        await nc.close()
        return response.data.decode()

    async with main() as model_service:
        response = await simulate_request()
        assert response.startswith("Translation: I adore programming.")

# Добавьте другие тесты, если необходимо

