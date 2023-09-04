# Falcon 40B Local Language Model (LLM) API

Welcome to the Falcon 40B Local Language Model (LLM) API repository. This API allows you to interact with a powerful language model, Falcon 40B, locally on your machine. Falcon 40B is a high-performance model, so please ensure that your hardware meets the following requirements:

## System Requirements
- GPU: 2x RTX 6000 Ada (not A6000 or RTX 6000) or equivalent for optimal performance.
- CPU: 8 cores, for example, Intel Core i9-11900K or AMD Ryzen 9 5900X.
- RAM: At least 85-100 GB of RAM for efficient processing.

## Project Structure
The project is organized as follows:

- `api_server/main.py`: The FastAPI-based API server that serves as an interface to the Falcon 40B model. It handles incoming requests and communicates with the model via NATS.
- `client_js/client.js`: A JavaScript client for interacting with the API server. It demonstrates how to send requests to the API server.
- `model_service/main.py`: The component responsible for running the Falcon 40B model and handling requests sent via NATS.
- `config/.env`: Configuration file for environment variables.
- `config/config.py`: Configuration settings for the project.
- `tests/api_tests.py`: Unit tests for the API server.
- `tests/model_service_tests.py`: Unit tests for the model service.

## Getting Started
To use this Falcon 40B LLM API locally, follow these steps:

1. **Start NATS**:
   - Run the following command to start the NATS server:
   ```
   docker run --network host -p 4222:4222 nats -js
   ```

2. **Start the Model Service**:
   - Run the Falcon 40B model service by executing the following command:
   ```
   python model_service/main.py
   ```

3. **Start the API Server**:
   - Run the API server with the following command:
   ```
   python api_server/main.py
   ```

4. **Install Dependencies for JavaScript Client**:
   - Install the Axios library for the JavaScript client by running:
   ```
   npm install axios
   ```

5. **Run the JavaScript Client**:
   - Use the provided JavaScript client to test the connection to the API server. Modify the `client_js/client.js` file if needed.
   ```
   node client_js/client.js
   ```

## API Documentation
For detailed API documentation and usage instructions, please refer to the [API documentation](docs/api_documentation.md).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

If you encounter any issues or have questions, please don't hesitate to [create an issue](https://github.com/your-repo/issues).

Thank you for using Falcon 40B LLM API!