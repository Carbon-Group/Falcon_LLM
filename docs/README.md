# Falcon_LLM Documentation

Welcome to the documentation for Falcon_LLM, a project that utilizes the Falcon-40B language model for various text generation tasks. This documentation provides an overview of the project structure, setup instructions, and usage guidelines.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Requirements](#requirements)
3. [Setup Instructions](#setup-instructions)
    - [NATS](#nats)
    - [Falcon 40B](#falcon-40b)
    - [API Server](#api-server)
    - [JS Client](#js-client)
4. [Usage](#usage)
5. [Developers](#developers)

## Project Structure <a name="project-structure"></a>

The project is organized into several components:

- `api_server/main.py`: The FastAPI-based API server that handles user requests and communicates with the Falcon 40B model.
- `client_js/client.js`: A JavaScript client for interacting with the API server.
- `config/.env`: Configuration file for environment variables.
- `config/config.py`: Configuration settings for the project.
- `tests/api_tests.py`: Unit tests for the API server.
- `tests/model_service_tests.py`: Unit tests for the Falcon 40B model service.
- `README.md`: The main project README with general information.
- `docs/README.md`: Documentation README (you are currently reading it).

## Requirements <a name="requirements"></a>

- Linux
- GPU (e.g., 2x RTX 6000 Ada or 2x A6000)
- CPU with 8 cores (e.g., Intel Core i9-11900K or AMD Ryzen 9 5900X)
- Libraries: axios (for the JS client), fastapi, asyncio, nats, transformers, torch (for the Python components)

## Setup Instructions <a name="setup-instructions"></a>

### NATS <a name="nats"></a>

NATS is used for reliable message exchange between the API server and Falcon 40B.

- Command to start NATS:
  ```bash
  docker run --network host -p 4222:4222 nats -js
  ```

### Falcon 40B <a name="falcon-40b"></a>

- Command to start the Falcon 40B model:
  ```bash
  python falcon.py
  ```

### API Server <a name="api-server"></a>

- Command to start the API server:
  ```bash
  python api_server.py
  ```

### JS Client <a name="js-client"></a>

- Dependency installation for the JS client:
  ```bash
  npm install axios
  ```

- To check the connection using the Node.js client:
  ```bash
  node client.js
  ```

## Usage <a name="usage"></a>

For details on how to use the Falcon_LLM project, please refer to the main project README.

## Developers <a name="developers"></a>

- [GitHub Repository](https://github.com/Carbon-Group)

Feel free to explore the codebase, run tests, and contribute to the project's development.

Thank you for using Falcon_LLM! If you have any questions or encounter issues, please refer to the documentation or reach out to the project's developers on GitHub.