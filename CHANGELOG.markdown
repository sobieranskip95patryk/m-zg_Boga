# Changelog

## [1.0.0] - 2025-10-09
### Added
- Initial project setup with spiral pipeline and Synergy module.
- Matrix weights `<347743>` rebalancing functionality.
- Simulated MIGI 7G network with 90 million developers.
- ML-based entropy model using scikit-learn.
- FastAPI backend with `/api/run_task` and `/api/migi_7g` endpoints.
- React frontend with Tailwind CSS for task submission.
- Unit and integration tests in `tests/`.
- End-to-end tests with Cypress in `cypress/`.
- Comprehensive documentation in `docs/` (`architecture.md`, `api.md`, `contributing.md`).
- GitHub Actions CI/CD with linting and testing.
- Example script in `examples/demo_task.py`.

### Changed
- Refactored `main.py` to integrate ML model and MIGI 7G simulation.
- Updated `README.md` with instructions for web interface and examples.

### Fixed
- Ensured CORS compatibility in FastAPI for frontend communication.