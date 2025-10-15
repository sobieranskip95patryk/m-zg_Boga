# Mozg Boga MIGI

## Overview
GOK:AI is a hybrid, ethical, self-evolving consciousness system designed as a modular, auditable, and scalable core for the MIGI project. It integrates advanced AI techniques to provide decision support, planning, and simulation capabilities while ensuring ethical considerations and environmental impacts are monitored.

## Features
- **AGI Kernel**: The core processing unit that implements the consciousness model and decision-making algorithms.
- **Multi-Agent System**: A set of specialized agents (Reasoner, Planner, Researcher, Vision, Ethics, Gaia Monitor) that collaborate to achieve complex tasks.
- **API Endpoints**: RESTful API for interacting with the system, including endpoints for querying, ingesting data, planning, simulating, and auditing decisions.
- **Vector Database**: A storage solution for managing embeddings and facilitating efficient retrieval of information.
- **Knowledge Graph**: Integration with a knowledge graph to enhance reasoning and contextual understanding.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd Mozg_Boga_MIGI
   ```

2. **Environment Variables**:
   Copy the `.env.example` to `.env` and fill in the required variables.

3. **Docker Setup**:
   Navigate to the `infra` directory and run:
   ```bash
   docker-compose up -d
   ```

4. **Install Requirements**:
   Create a virtual environment and install the necessary packages:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Run the API**:
   Start the API server:
   ```bash
   uvicorn core.api.main:app --host 0.0.0.0 --port 8000 --reload
   ```

## Usage
- **API Endpoints**: Use tools like Postman or curl to interact with the API. Refer to the documentation in the `core/api/endpoints` directory for details on each endpoint.
- **Testing**: Unit tests are available in the `tests` directory. Run them to ensure the system is functioning correctly.

## Contribution
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE.txt file for more details.