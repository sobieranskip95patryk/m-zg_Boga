# MetaGeniusz Ecosystem

Modułowy ekosystem AI i kreatywnych platform, łączący autonomiczne agenty (np. AnonymousAgent, PinkMan) z centralnym dashboardem i integracjami (xAI, blockchain). Architektura oparta na mikroserwisach, Nx monorepo i Dockerze.

## Architektura

- Dashboard: Next.js SPA z dynamicznym routingiem do paneli agentów.
- Orchestrator: Node.js/Express, zarządza komunikacją między agentami (REST, plany na gRPC/Kafka).
- Auth: Centralny serwis JWT z RBAC (role: admin, user, agent).
- Agents: Niezależne mikroserwisy (Node.js dla web, Python dla AI).
- Integrations: xAI/Grok dla AI, Web3.js dla blockchain (future).

### Diagram Architektury
```mermaid
graph TD
    A[User] --> B[Dashboard SPA (Next.js)]
    B --> C[Orchestrator (Node.js)]
    C --> D[Auth Service (JWT)]
    C --> E[Agents: AnonymousAgent, PinkMan, etc.]
    E --> F[xAI Integration]
    E --> G[Future: Blockchain, IoT]
    F --> H[External: xAI API]
```

## Setup

1. Instalacja Nx:
   ```bash
   npx create-nx-workspace@latest metageniusz-ecosystem --preset=ts
   ```
2. Struktura:
   - apps/dashboard: Next.js SPA
   - packages/auth: JWT auth
   - packages/orchestrator: Centralny router
   - packages/agents/*: Mikroserwisy agentów
3. Uruchomienie:
   ```bash
   docker-compose up
   nx serve dashboard
   ```
4. CI/CD: GitHub Actions (zobacz `.github/workflows/ci.yml`).

## Development

- Testy: `nx test <package>` (Jest dla TS, Pytest dla Pythona).
- Build: `nx build <package>`.
- Deploy: Vercel (dashboard), Docker Hub (mikroserwisy).
