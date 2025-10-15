# Contributing to Mózg Boga

We welcome contributions to the Mózg Boga project! Here's how you can help:

## Getting Started
1. Fork the repository on GitHub.
2. Clone your fork: `git clone https://github.com/<your-username>/M_Boga.git`
3. Create a new branch: `git checkout -b my-feature`

## Development Guidelines
- Follow PEP 8 for Python code style.
- Write unit tests for new features in the `tests/` directory.
- Update documentation in `docs/` as needed.
- Ensure all tests pass: `python -m unittest discover tests`
- For frontend changes, ensure Cypress tests pass: `npx cypress run`

## Key Areas for Contribution
- **ML Model**: Optimize the BERT-based entropy model in `gokai_core/models/entropy_model.py`.
- **MIGI 7G**: Extend the Kafka-based network simulation in `migi_7g/`.
- **UI/UX**: Improve the React frontend in `web/src/App.jsx`.
- **API**: Add new endpoints to `api/server.py` for advanced features.
- **Testing**: Increase test coverage with additional unit and integration tests.

## Submitting Changes
1. Commit your changes: `git commit -m "Add my feature"`
2. Push to your fork: `git push origin my-feature`
3. Create a pull request on GitHub with a clear description of your changes.

## Code Review
All pull requests will be reviewed by maintainers. Please address feedback promptly.

## Issues
Feel free to open issues for bugs, feature requests, or questions. Check out the "Call for Contributors" issue for specific tasks.

Thank you for contributing to Mózg Boga!