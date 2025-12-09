# Contributing to CasaNova

Welcome to **CasaNova**! We're excited that you're interested in contributing to our open-source project. Your help is essential in making real estate and financial analysis accessible to young adults.

We operate under the **Apache License 2.0**. By contributing, you agree that your submissions will be licensed under the same terms.

## 🤝 How to Get Started

### 1. The Easy Way: Issues

We use GitHub Issues to track bugs, features, and questions.

* **[Bug]**: If you find a bug, please check if it has already been reported. If not, open a new issue using the **Bug Report template** (highly recommended) and provide clear steps to reproduce the error, your environment details, and screenshots.
* **[Feat] & [Enhancement]:** For new features or improvements, open a new issue using the **Feature Request template** (highly recommended) to discuss your idea before writing code. This ensures it aligns with the project's mission.

### 2. Code Contribution Workflow (Pull Requests)

All code contributions must follow this workflow to ensure code quality and stability.

1.  **Fork** the CasaNova repository.
2.  **Clone** your forked repository locally.
3.  **Create a new branch** for your work, following our naming convention (see below).
4.  **Make changes**, ensuring you include **test code** to cover your changes (see Code Standards).
5.  **Commit** your changes following the commit message rules (see Commit Standards).
6.  **Push** your branch to your forked repository.
7.  **Create a Pull Request (PR)** from your branch to the **`main`** branch of the CasaNova repository.

### 3. Branching and Naming Rules

We use a protected `main` branch. Direct commits to `main` are disabled.

* **Branch Naming Convention:** `[type]/[issue-number]-[short-description]`
    * **Examples:** `feat/12-loan-simulator`, `fix/34-login-error`
* **Pull Request (PR) Title:** Must use a clear prefix and link the relevant issue.
    * **Format:** `[type]: [Short Description of Change] (#IssueNumber)`
    * **Example:** `Fix: DSR calculation error (#34)`
* **PR Review:** **Minimum of 2 Approvals** from collaborators are required before a PR can be merged.

### 4. Code and Commit Standards 

#### Commit Message Standard
The message should communicate *what* was changed and *why*.

1.  **Subject Line (First Line):** Use the **imperative mood** (e.g., "Add," "Fix," "Refactor"). Keep it concise (under 50 characters).
    * **Good:** `Fix: Resolve API rate limit issue`
    * **Bad:** `Fixed API rate limit issue`
2.  **Body (Details):** Leave a blank line after the subject. Include the detailed motivation for the change, any assumptions made, and the approach taken. **This is mandatory** for non-trivial changes.
3.  **Issue Linking:** The PR body **must** include a link to the issue it resolves (e.g., `Closes #12` or `Fixes #34`).

#### Code Style and Testing (Linting & Formatting)

To maintain high code quality, we require the use of automated tools.

* **Testing:** All contributions must include **accompanying unit and integration tests** that pass successfully.
* **Backend (Python/Django):** We use **`Black`** for automatic code formatting and **`Flake8`** for linting (checking against PEP 8 style guide). All code must pass these checks.
* **Frontend (TypeScript/React):** We use **`ESLint`** for code quality and **`Prettier`** for automated code formatting.

## 📝 Other Essential Documents

Please refer to these files for more community guidelines:

* **[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md):** Defines the expected behavior and standards within our community.
* **[LICENSE](LICENSE):** Details the Apache License 2.0 under which this project is distributed.


