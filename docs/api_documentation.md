# API Documentation

This documentation provides an overview of the API endpoints, their usage, and authentication for the project.

## Table of Contents
- [Authentication](#authentication)
- [Endpoints](#endpoints)
  - [Process Request](#process-request)
- [Example Usage](#example-usage)

## Authentication

To access the API endpoints, you need to include a Bearer token in the request header. The token should be passed as an "Authorization" header in the format:

```
Authorization: Bearer your_secret_token
```

Replace `your_secret_token` with the actual token for authentication.

## Endpoints

### Process Request

**Endpoint**: `/process_request/`

**Method**: `POST`

This endpoint allows you to send a request for text generation using a pre-trained model.

#### Request Body

- `prompt` (string, required): The text prompt or input for text generation.

#### Response

- `response` (string): The generated text as a response to the provided prompt.

**HTTP Status Codes:**

- `200 OK`: Successful request with the generated response.
- `400 Bad Request`: Invalid request format.
- `401 Unauthorized`: Missing or invalid Bearer token.
- `403 Forbidden`: Bearer token is invalid.
- `500 Internal Server Error`: NATS error or other internal server issues.

## Example Usage

Here is an example of how to use the API in JavaScript:

```javascript
const axios = require('axios');

// URL of your API server
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
const userPrompt = 'Translate: I love programming.'; // Replace with your request
sendRequest(userPrompt);
```

This documentation provides you with the necessary information to interact with the API, including authentication details and endpoint descriptions. Make sure to replace placeholders with actual values when making requests to the API.