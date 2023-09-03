import asyncio
import nats
import json

async def run_model():
    # Инициализируем NATS-клиент
    nc = await nats.connect()

    # Создаем подписчика на NATS-сообщения
    async def message_handler(msg):
        data = json.loads(msg.data.decode())
        input_text = data.get("input_text", "")
        num_return_sequences = data.get("num_return_sequences", 1)

        # Простой генератор случайных строк
        import random
        import string

        def generate_random_string(length):
            return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

        generated_text = [generate_random_string(len(input_text)) for _ in range(num_return_sequences)]

        # Отправляем сгенерированный текст обратно по NATS
        await nc.publish(msg.reply, json.dumps({"generated_text": generated_text}))

    # Подписываемся на NATS-сообщения для обработки
    await nc.subscribe("text_generation_requests", cb=message_handler)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_model())
