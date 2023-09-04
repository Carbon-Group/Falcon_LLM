# Falcon 40B Instruct Model Service Documentation

## Overview

This documentation provides an overview of the Falcon 40B Instruct Model Service. The service utilizes the Falcon-40B Instruct model for text generation and communicates with clients over the NATS messaging system.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Getting Started](#getting-started)
3. [Message Handling](#message-handling)
4. [Model Configuration](#model-configuration)
5. [API Endpoint](#api-endpoint)
6. [Usage](#usage)
7. [Shutting Down the Service](#shutting-down-the-service)

## Prerequisites

Before using the Falcon 40B Instruct Model Service, ensure you have the following prerequisites in place:

- Python 3.6 or later
- NATS messaging system (running on `localhost:4222`)

## Getting Started

To run the Falcon 40B Instruct Model Service, follow these steps:

1. Install the required Python dependencies using `pip`:

    ```bash
    pip install transformers torch nats-py
    ```

2. Start the NATS messaging system on `localhost` with port `4222`.

3. Run the `model_service/main.py` script:

    ```bash
    python model_service/main.py
    ```

## Message Handling

The Falcon 40B Instruct Model Service subscribes to the "user_requests" subject on NATS and handles incoming requests from clients. When a message is received, it processes the request, generates a response using the model, and publishes the generated text as a reply.

## Model Configuration

The service uses the Falcon-40B Instruct model for text generation. The model and tokenizer are loaded using the Hugging Face Transformers library. The following configuration options are applied to the model:

- Model: "tiiuae/falcon-40b-instruct"
- Max sequence length: 200
- Sampling method: Top-K sampling with K=10
- Number of return sequences: 1
- End-of-sequence token ID: Obtained from the tokenizer

## API Endpoint

The Falcon 40B Instruct Model Service does not expose a traditional REST API. Instead, it listens for incoming messages on the NATS subject "user_requests." Clients can send requests as messages, and the service replies with the generated text.

## Usage

To use the Falcon 40B Instruct Model Service, you can send requests as messages to the "user_requests" NATS subject. The service will process the request, generate a response, and publish the generated text as a reply.

Example client usage (JavaScript):

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

## Shutting Down the Service

To shut down the Falcon 40B Instruct Model Service, simply terminate the Python script by pressing `Ctrl + C` in the terminal where the service is running.