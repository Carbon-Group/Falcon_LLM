import asyncio
import nats

async def main():
    # Подключение к локальному NATS серверу
    nc = await nats.connect("nats://localhost:4222")

    async def message_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        print("Received a message on '{subject} {reply}': {data}".format(
            subject=subject, reply=reply, data=data))

    # Подписка на тему "foo" и обработка сообщений
    sub = await nc.subscribe("foo", cb=message_handler)

    # Отправка нескольких сообщений
    await nc.publish("foo", b'Hello')
    await nc.publish("foo", b'World')
    await nc.publish("foo", b'!!!!!')

    # Ожидание получения сообщений (можно указать количество)
    await asyncio.sleep(1)  # Даем время на обработку сообщений

    # Отмена подписки и завершение соединения
    await sub.unsubscribe()
    await nc.drain()

if __name__ == '__main__':
    asyncio.run(main())
