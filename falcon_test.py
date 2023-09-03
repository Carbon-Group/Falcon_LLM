import asyncio
import nats
from nats.errors import ConnectionClosedError

async def main():
    nc = await nats.connect("nats://localhost:4222")

    async def message_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()

        print(f"Received a message on '{subject} {reply}': {data}")

        # Просто отправляем обратно полученное сообщение
        await nc.publish(reply, data.encode())

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
