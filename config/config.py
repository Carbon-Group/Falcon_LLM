# Конфигурационные настройки проекта

# Настройки для API сервера
class APIServerConfig:
    HOST = "0.0.0.0"
    PORT = 8000
    SECRET_TOKEN = "your_secret_token"  # Замените на ваш реальный токен
    NATS_URL = "nats://localhost:4222"  # Добавьте адрес NATS из конфигурации модельного сервиса

# Настройки для модельного сервиса
class ModelServiceConfig:
    NATS_URL = "nats://localhost:4222"
    MODEL_NAME = "tiiuae/falcon-40b-instruct"
    MAX_GENERATION_LENGTH = 200
    DO_SAMPLE = True
    TOP_K = 10
    NUM_RETURN_SEQUENCES = 1
    EOS_TOKEN_ID = None  # Установите значение, если есть специальный токен окончания
