# API Client for Interacting with the API Server

This is a JavaScript client designed to interact with the API server of the project. It allows you to send requests to the server and receive responses. You can use this client as a starting point for integrating the API into your applications.

## Getting Started

### Prerequisites

Before using the client, make sure you have the following prerequisites installed:

- [Node.js](https://nodejs.org/)
- [npm](https://www.npmjs.com/)

### Installation

1. Clone the project repository to your local machine:

   ```shell
   git clone https://github.com/Carbon-Group/Falcon_LLM.git
   cd Falcon_LLM/client_js
   ```

2. Install the required dependencies:

   ```shell
   npm install
   ```

3. Update the `bearerToken` variable in `client.js` with your authentication token. You can obtain the token from the project administrator.

## Usage

You can use the API client to send requests to the API server and receive responses. Here's how to use it:

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

Replace `userPrompt` with your desired request, and then run the client using the following command:

```shell
npm start
```

## Contributing

If you would like to contribute to this project, please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md). We welcome contributions from the community!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was created by the Carbon Group.
- Special thanks to our contributors and the open-source community.