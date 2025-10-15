# MVP Roadmap

## D+0–7 (Setup)
- Clone the repository to your local machine.
- Fill in the `.env` file with necessary environment variables.
- Run `docker-compose up -d` to start the services.
- Initialize the API by running `uvicorn core.api.main:app --reload`.

## D+8–30 (Local MVP)
- Implement the AGI Kernel with initial configurations.
- Set up an in-memory vector store or configure Qdrant.
- Develop a simple chat UI or use Postman to test endpoints.
- Ensure the `ask`, `ingest`, and `metrics` endpoints are operational.
- Implement retrieval-augmented generation (RAG) for document retrieval.
- Set up basic telemetry for monitoring API performance.
- Conduct unit tests for the kernel and endpoints.
- Deliverable: A working demo on local machine with first 10 interactions.

## D+31–60 (Integration)
- Integrate NATS or Kafka for agent orchestration.
- Implement agents: Reasoner, Planner, and Researcher as microservices.
- Prototype the Knowledge Graph using Neo4j and establish connectors.
- Develop logic for unlocking features based on data quality and user feedback.
- Create a pitch deck and compile a contact list of potential partners.
- Deliverable: Multi-agent local demo and a draft of a 30–40 page e-book.

## D+61–90 (Scale & Governance)
- Strengthen infrastructure with Kubernetes manifests, secrets management, and TLS.
- Implement a reinforcement learning from human feedback (RLHF) pipeline and reward modeling.
- Develop the Gaia module for environmental impact modeling and visualization.
- Launch a landing page for user registration and paid downloads.
- Deliverable: Beta release, partner demos, and a monetization pipeline.