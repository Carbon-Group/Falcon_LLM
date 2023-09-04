# API Server Documentation

This document provides an overview of the API server for the Falcon 40B Instruct model.

## Table of Contents

- [Overview](#overview)
- [Authentication](#authentication)
- [Endpoints](#endpoints)
  - [Process Request](#process-request)
- [Example Usage](#example-usage)
- [Testing](#testing)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Overview

The API server is designed to interact with the Falcon 40B Instruct model, allowing users to send requests for text generation. It provides a secure and authenticated interface for communication.

## Authentication

The API server uses Bearer token authentication. To access the API, clients must include a valid token in the `Authorization` header of their requests.

## Endpoints

### Process Request

- **URL:** `/process_request/`
- **Method:** POST
- **Description:** This endpoint allows clients to send a request for text generation to the Falcon 40B Instruct model.
- **Request Body:** JSON object with a `prompt` field containing the input text prompt.
- **Request Headers:** Include the Bearer token in the `Authorization` header.
- **Response:** The server responds with the generated text as a JSON object.

Example request:
```json
{
  "prompt": "Translate: I love programming."
}
```

Example response:
```json
{
  "response": "Generated text goes here."
}
```

## Example Usage

Here is an example of how to use the API server with JavaScript:

```javascript
const axios = require('axios');

// URL of the API server
const apiUrl = 'http://localhost:8000/process_request/';

// Bearer token for authentication
const bearerToken = 'your_secret_token'; // Replace with your actual token

// Function to send a request to the API server
async function sendRequest(prompt) {
  try {
    const response = await axios.post(
      apiUrl,
      { prompt },
      {
        headers: {
          Authorization: `Bearer ${bearerToken}`,
        },
      }
    );

    if (response.status === 200) {
      console.log('Response from API:', response.data.response);
    } else {
      console.error('API request failed:', response.statusText);
    }
  } catch (error) {
    console.error('Error sending API request:', error.message);
  }
}

// Example usage
const userPrompt = 'Translate: I love programming.'; // Replace with your own prompt
sendRequest(userPrompt);
```

## Testing

Testing of the API server is performed using the FastAPI TestClient. The provided tests ensure that authentication and endpoint functionality are working correctly. Tests can be found in the `tests/api_tests.py` file.

## Environment Variables

The API server relies on environment variables for configuration. These variables are defined in the `.env` file and loaded using the `python-decouple` library. Important variables include:

- `API_HOST`: Host IP or domain of the API server.
- `API_PORT`: Port on which the API server listens.
- `SECRET_TOKEN`: Bearer token for authentication.
- `NATS_URL`: URL of the NATS server for communication with the model service.
- Other model-related variables.

## Contributing

Contributions to this project are welcome. Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to the project.

## License

This project is licensed under the [MIT License](LICENSE).