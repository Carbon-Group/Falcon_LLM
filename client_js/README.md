# JavaScript Client Documentation

## Introduction

This documentation provides instructions and information on how to use the JavaScript client for interacting with the API server. The client is designed to send requests to the server and receive responses generated by the Falcon 40B Instruct model.

## Prerequisites

Before using the JavaScript client, ensure that you have the following prerequisites installed:

- [Node.js](https://nodejs.org/): JavaScript runtime environment.
- [npm](https://www.npmjs.com/): Package manager for Node.js.
- Environment variables properly configured in a `.env` file (refer to [config/.env](../config/.env) for details).

## Installation

Follow these steps to set up and use the JavaScript client:

1. Clone the project repository to your local machine:

   ```bash
   git clone https://github.com/Carbon-Group/Falcon_LLM.git
   cd Falcon_LLM/client_js
   ```

2. Install the required dependencies:

   ```bash
   npm install
   ```

3. Configure Environment Variables:
   - Create a `.env` file in the root directory of the `client_js` folder.
   - Define the following environment variables in the `.env` file:

     ```
     API_URL=<Your_API_URL>                 # Replace with the API server URL
     SECRET_TOKEN=<Your_Bearer_Token>       # Replace with your Bearer token
     ```

   Example `.env` file content:

   ```
   API_URL=http://localhost:8000
   SECRET_TOKEN=your_secret_token
   ```

## Usage

To use the JavaScript client for sending requests to the API server, follow these steps:

1. Import the required dependencies in your JavaScript code:

   ```javascript
   const axios = require('axios');
   const dotenv = require('dotenv');
   ```

2. Load environment variables from the `.env` file:

   ```javascript
   dotenv.config();
   ```

3. Define the API URL and Bearer token from the environment variables:

   ```javascript
   const apiUrl = process.env.API_URL;
   const bearerToken = process.env.SECRET_TOKEN;
   ```

4. Create a function to send requests to the API server:

   ```javascript
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
   ```

5. Call the `sendRequest` function with your desired prompt:

   ```javascript
   const userPrompt = 'Translate: I love programming.'; // Replace with your request
   sendRequest(userPrompt);
   ```

## Testing

You can run tests for the JavaScript client by executing the following command:

```bash
npm test
```

This will run the tests located in the `tests` directory.

## License

This JavaScript client is open-source and is licensed under the terms of the [LICENSE](../LICENSE) file.
