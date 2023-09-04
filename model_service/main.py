import asyncio
import nats
from nats.errors import ConnectionClosedError
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch
from config.config import ModelServiceConfig  # Импорт настроек

async def main():
    nc = await nats.connect(ModelServiceConfig.NATS_URL)  # Использование настроек

    # Загружаем модель и токенизатор Falcon-40B Instruct
    model = ModelServiceConfig.MODEL_NAME
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
        sequences = pipeline(data, max_length=ModelServiceConfig.MAX_GENERATION_LENGTH, do_sample=ModelServiceConfig.DO_SAMPLE, top_k=ModelServiceConfig.TOP_K, num_return_sequences=ModelServiceConfig.NUM_RETURN_SEQUENCES, eos_token_id=ModelServiceConfig.EOS_TOKEN_ID)
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
