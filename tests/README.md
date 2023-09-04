# Tests for the Project

This directory contains tests for the project. There are two main test suites:

1. **API Tests (`api_tests.py`):** These tests are designed to test the functionality of the API server.

2. **Model Service Tests (`model_service_tests.py`):** These tests are designed to test the functionality of the model service.

## Running Tests

To run the tests, you can use the following command:

```bash
pytest
```

Ensure that you have set up the necessary environment and dependencies for running the tests.

## Writing Tests

You can add additional tests to these test suites as needed to cover various aspects of your project's functionality. Ensure that your tests are well-organized, follow best practices, and provide meaningful assertions.

## Test Fixtures

The `event_loop` fixture is used for asyncio testing in the `model_service_tests.py` suite.

## Contributing

If you'd like to contribute to the project, please follow the guidelines in the [CONTRIBUTING.md](../CONTRIBUTING.md) file.

Happy testing!