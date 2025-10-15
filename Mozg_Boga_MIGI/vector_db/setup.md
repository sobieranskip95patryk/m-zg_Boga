# Setup Instructions for Vector Database

## Overview
This document provides instructions for setting up the vector database used in the GOK:AI project. The vector database is essential for storing and retrieving high-dimensional vectors that represent the data processed by the AI system.

## Prerequisites
- Ensure that you have Docker installed on your machine.
- Familiarity with command line interface (CLI) operations.

## Setup Steps

1. **Clone the Repository**
   Clone the project repository to your local machine if you haven't done so already.
   ```
   git clone <repository-url>
   cd Mozg_Boga_MIGI
   ```

2. **Navigate to the Vector Database Directory**
   Change to the vector_db directory where the setup files are located.
   ```
   cd vector_db
   ```

3. **Configure Environment Variables**
   Create a `.env` file based on the `.env.example` provided in the root directory. Ensure to set the necessary environment variables for the vector database configuration.

4. **Start the Vector Database Service**
   Use Docker to start the vector database service defined in the `docker-compose.yml` file located in the `infra` directory.
   ```
   cd infra
   docker-compose up -d
   ```

5. **Verify the Setup**
   After the containers are up and running, verify that the vector database service is operational by checking the logs.
   ```
   docker-compose logs vector_db
   ```

6. **Access the Vector Database**
   Depending on the configuration, you can access the vector database through the specified port. Refer to the `docker-compose.yml` file for the exact port mapping.

## Additional Information
For further details on using the vector database, refer to the `README.md` file located in the `vector_db` directory. This file contains information on how to interact with the database, including API endpoints and usage examples.

## Troubleshooting
If you encounter any issues during the setup, please check the following:
- Ensure Docker is running and properly configured.
- Review the logs for any error messages that can provide insight into the problem.
- Consult the project documentation for additional guidance.

By following these instructions, you should have a fully operational vector database ready for use in the GOK:AI project.