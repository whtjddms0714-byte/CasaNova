Contribution Guidelines
=======================

<<<<<<< HEAD
<<<<<<< Updated upstream
기여 절차, 코딩 컨벤션, PR 방법 등.
=======
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

CasaNova is distributed under the Apache License 2.0.

By contributing code or documentation, you agree that your contributions
may be included under this license, as specified in the project's
``LICENSE`` file.
>>>>>>> Stashed changes
=======
Thank you for your interest in contributing to CasaNova!
We welcome developers, designers, and data contributors of all experience levels.

This document outlines the workflow, coding standards, and review policies
for contributing to the CasaNova open-source project.

------------------------------------------------------------
How to Get Started
------------------------------------------------------------

1. Fork the repository on GitHub  
2. Clone your fork:

.. code-block:: bash

    git clone https://github.com/<username>/CasaNova.git
    cd CasaNova

3. Create a feature branch  
4. Commit changes following the commit message format  
5. Submit a Pull Request (PR) for review  

------------------------------------------------------------
Branching Strategy
------------------------------------------------------------

CasaNova follows a lightweight variation of **GitHub Flow**.

- **main**  
  Contains stable and deployable code. All production-ready code lives here.

- **feature branches**  
  All new code must be implemented in a separate branch:

::

    type/issue-number-short-description

Examples:

- ``feat/12-add-loan-engine``  
- ``fix/30-loan-rate-bug``  
- ``docs/25-update-api-reference``  

------------------------------------------------------------
Commit Message Standards
------------------------------------------------------------

Commits must use imperative mood:

Examples:

- ``Add financial scoring function``  
- ``Fix distance calculation error``  
- ``Update API documentation``  

Rules:

- Keep the subject short (≤ 50 characters)  
- Body required for non-trivial changes  
- Explain *why* the change was needed  

------------------------------------------------------------
Pull Request (PR) Process
------------------------------------------------------------

1. Push your branch to your fork  
2. Open a Pull Request targeting **main**  
3. Add a descriptive title and summary  
4. Request reviews  

Minimum requirements:

- **At least 2 approvals** from maintainers  
- All CI checks (if configured) must pass  
- No merge conflicts  

PR Template Example:

::

    ## Summary
    Describe the purpose of this PR.

    ## Changes
    - Added ...
    - Updated ...

    ## Related Issues
    Closes #<issue-number>

------------------------------------------------------------
Coding Style Guidelines
------------------------------------------------------------

Backend (Python)
----------------

- Follow **PEP8** conventions  
- Automated formatting using **Black**:

.. code-block:: bash

    black .

- Lint with **Flake8**:

.. code-block:: bash

    flake8 .

Frontend (TypeScript + React)
-----------------------------

- Use **ESLint + Prettier**  
- Prefer functional components and hooks  
- Keep components small and modular  
- Avoid unnecessary re-renders (React.memo where applicable)  

General Rules
-------------

- Write clear, self-documenting code  
- Add comments where logic is non-obvious  
- Update documentation when APIs or features change  

------------------------------------------------------------
Testing Guidelines
------------------------------------------------------------

Testing ensures reliability and stability.

Backend:

- Unit test financial formulas  
- Test loan eligibility logic  
- Validate distance-based infrastructure calculations  

Frontend:

- Snapshot tests for components  
- API mock tests  
- Input validation tests  

Run all tests before requesting a review.

------------------------------------------------------------
Issue Reporting
------------------------------------------------------------

Before opening an issue:

1. Check existing issues  
2. Clearly describe the problem  
3. Provide reproduction steps  
4. Include stack traces or screenshot evidence  

Issue Types:

- ``bug`` — Incorrect behavior  
- ``feature`` — Request for new functionality  
- ``documentation`` — Docs or comment improvements  

------------------------------------------------------------
Community Standards
------------------------------------------------------------

CasaNova follows a welcoming and inclusive community philosophy.

Contributors must follow:

- **CONTRIBUTING.md**  
- **CODE_OF_CONDUCT.md**  

Expected behavior:

- Respect other contributors  
- Provide constructive feedback  
- Avoid personal attacks or toxic behavior  

------------------------------------------------------------
Thank You
------------------------------------------------------------

Your contributions make CasaNova better for everyone!
Whether you fix a typo, improve documentation, or develop a new algorithm—  
**we appreciate every contribution.**

End of Contribution Guidelines.
>>>>>>> 99cfac16b797d7549dabf44f88a13845caa126e3
