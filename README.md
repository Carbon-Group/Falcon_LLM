# Falcon_LLM

## **Requirements**:
- Linux
- To use LLM with Falcon-40B, a GPU is required, as LLM demands high graphical performance. You will need at least 85-100 GB of RAM for fast execution of logical inference with Falcon 40B.

### GPU:
- 2x RTX 6000 Ada (not A6000 or RTX 6000)
- 2x A6000 – a more budget-friendly option

### CPU:
- 8 cores.
- For example, Intel Core i9-11900K or a similar AMD Ryzen 9 5900X.

### Libraries:
- For the JS client: axios.
- For FastAPI: fastapi.
- For Falcon: asyncio, nats.

### Dependencies Installation:
```bash
python -m pip install -r requirements.txt
```

## **Instructions for Using a Local Copy of the Falcon 40B Model**

### NATS
- Enables reliable, fast, and flexible message exchange between the API server and Falcon 40B.
- Command to start NATS:
```bash
docker run --network host -p 4222:4222 nats -js
```

### Falcon 40B
- Command to start the model:
```bash
python falcon.py
```

### API Server
- Command to start the server:
```bash
python api_server.py
```

### JS Client
- Dependency installation:
```bash
npm install axios
```
- To check the connection, you can use the Node.js client:
```bash
node client.js
```

### Developers:
```bash
https://github.com/Carbon-Group
```