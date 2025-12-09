Contribution Guidelines
=======================

We welcome contributions that improve CasaNova’s reliability, features,
and documentation.

Code Style
----------

Python
~~~~~~

- Follow PEP 8 as a general guideline.
- Use clear, descriptive function and variable names.
- Keep business logic in the engine modules rather than in views.

Django
~~~~~~

- Keep views thin and delegate complex logic to the engine layer.
- Group related endpoints logically under ``casanova_app``.

JavaScript
~~~~~~~~~~

- Prefer clear, explicit code for browser-based logic.
- Handle API errors gracefully and inform the user.

Branching and Commits
---------------------

- Use feature branches for non-trivial changes.

  Example naming:

  - ``feat/add-loan-api``
  - ``fix/infra-scoring``
  - ``docs/update-usage``

- Write commit messages in imperative form:

  - ``Add loan recommendation endpoint``
  - ``Refine infrastructure scoring weights``

Pull Requests
-------------

- Describe the purpose and scope of the change.
- Include before/after behavior when relevant.
- Link to any related issues or design documents.

Tests
-----

If you introduce new logic:

- Add or update unit tests where appropriate.
- Ensure tests pass locally before opening a pull request.

Documentation Contributions
---------------------------

- Update or add pages under ``docs/`` when the architecture or APIs change.
- Keep examples in sync with the actual code.

Reporting Issues
----------------

When reporting an issue, include:

- Environment details (Python version, OS, etc.),
- Steps to reproduce,
- Expected vs. actual behavior,
- Relevant logs or stack traces.

Feature Requests
----------------

For feature requests, describe:

- The problem or user need,
- Proposed behavior or UI changes,
- Any constraints or assumptions.

License and Ownership
---------------------

By contributing code or documentation, you agree that your contributions
may be included under the project's license as specified in ``LICENSE``.

