import asyncio
import nats
from nats.errors import ConnectionClosedError
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch
import os

# Чтение переменных окружения из .env файла
from dotenv import load_dotenv
load_dotenv()

NATS_URL = os.getenv("NATS_URL")  # Получите значение из .env

async def main():
    nc = await nats.connect(NATS_URL)

    # Загружаем модель и токенизатор Falcon-40B Instruct
    model = os.getenv("MODEL_NAME")
    tokenizer = AutoTokenizer.from_pretrained(model)
    pipeline = transformers.pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        device_map="auto",
    )

    async def message_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()

        print(f"Received a message on '{subject} {reply}': {data}")

        # Генерируем ответ с помощью модели Falcon-40B Instruct
        sequences = pipeline(data, max_length=int(os.getenv("MAX_GENERATION_LENGTH")), do_sample=bool(os.getenv("DO_SAMPLE")), top_k=int(os.getenv("TOP_K")), num_return_sequences=int(os.getenv("NUM_RETURN_SEQUENCES")), eos_token_id=int(os.getenv("EOS_TOKEN_ID")))
        generated_text = sequences[0]['generated_text']

        # Отправляем сгенерированный ответ обратно
        await nc.publish(reply, generated_text.encode())

    # Подписываемся на запросы от пользователя
    sub = await nc.subscribe("user_requests", cb=message_handler)

    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        pass

    # Отписываемся и завершаем соединение с NATS
    await sub.unsubscribe()
    await nc.drain()

if __name__ == '__main__':
    asyncio.run(main())
