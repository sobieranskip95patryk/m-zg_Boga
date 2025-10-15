# README for Vector Database Component

## Overview

The Vector Database component is a crucial part of the GOK:AI project, designed to efficiently store and retrieve high-dimensional vector representations of data. This allows for advanced querying capabilities and supports the overall functionality of the AI system.

## Setup Instructions

1. **Prerequisites**: Ensure you have the following installed:
   - Python 3.10 or higher
   - Docker (for containerized setup)
   - Docker Compose (for managing multi-container Docker applications)

2. **Installation**:
   - Clone the repository:
     ```
     git clone <repository-url>
     cd Mozg_Boga_MIGI
     ```
   - Navigate to the `vector_db` directory:
     ```
     cd vector_db
     ```

3. **Configuration**:
   - Create a `.env` file based on the `.env.example` template in the root directory. Ensure to set the necessary environment variables for your setup.

4. **Running the Database**:
   - Use Docker Compose to start the vector database service:
     ```
     docker-compose up -d
     ```

5. **Accessing the Database**:
   - The vector database will be accessible at the configured endpoint. Refer to the `docker-compose.yml` file for specific details on ports and services.

## Usage

- The vector database is designed to handle operations such as:
  - Ingesting new vector data.
  - Querying for similar vectors.
  - Managing vector embeddings for various data types.

- Refer to the API documentation for specific endpoints and usage examples.

## Contribution

Contributions to the Vector Database component are welcome. Please follow the standard contribution guidelines outlined in the main project README.

## License

This project is licensed under the MIT License. See the LICENSE.txt file for more details.