# Tests Documentation

This directory contains unit tests for the Mozg Boga MIGI project. The tests are designed to ensure the functionality and reliability of the various components of the system.

## Test Files

- **test_kernel.py**: Contains unit tests for the AGI Kernel, verifying its decision-making processes and overall functionality.
  
- **test_ingest.py**: Includes tests for the ingest endpoint, ensuring that documents are correctly processed and stored in the system.
  
- **test_endpoints.py**: Focuses on testing the API endpoints, validating that they respond correctly to requests and handle data as expected.

## Running Tests

To run the tests, ensure that you have the necessary dependencies installed as specified in the `requirements.txt` file. You can execute the tests using a testing framework such as `pytest`. 

```bash
pytest tests/
```

## Contribution

If you wish to contribute to the tests, please follow the project's coding standards and ensure that new tests are added alongside any new features or changes to existing functionality.