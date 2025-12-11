# 🏠 CasaNova: Financial-Based Personalized Housing Recommendation System

**_New Home, New Start._**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Latest Release](https://img.shields.io/github/v/tag/whtjddms0714-byte/CasaNova.svg?color=success&label=v0.0.1%20Release)](https://github.com/whtjddms0714-byte/CasaNova/releases/tag/v0.0.1)
[![Contributors](https://img.shields.io/github/contributors/whtjddms0714-byte/CasaNova)](https://github.com/whtjddms0714-byte/CasaNova/graphs/contributors)

---

## 🌟 Project Introduction (프로젝트 소개)

CasaNova is an open-source web application designed to help **young adults in their 20s** confirm a **realistic housing budget** based on their current assets and income.

Unlike traditional real estate platforms, CasaNova integrates and analyzes complex factors—such as **DSR/DTI-emulating loan regulations** and youth-targeted mock financial products—to support financially savvy and stable housing decisions.

This project is fully open-source and free for anyone to use and contribute to.

---
## 📚 Documentation

CasaNova project documentation is available at the link below:

➡ **https://casanova.readthedocs.io/en/latest/**

---

## 🌐 Project Website (GitHub Pages)

The official CasaNova project website is available at the link below:

➡ **https://whtjddms0714-byte.github.io/CasaNova/**

This website includes:
- Project overview & mission  
- Documentation links  
- Feature showcase  
- Community & contact sections  

---

## ✨ Core Features (주요 기능)

The heart of CasaNova lies in its two primary engines: **Financial Analysis** and **Preference Matching**.

| Feature | Status | Description |
| :--- | :--- | :--- |
| **💰 Financial Simulation Engine** | `In Progress` | DSR-based logic using the PMT formula to calculate maximum loan amount and monthly repayment. |
| **📈 Budget Confirmation & Visualization** | `In Progress` | Calculates budget as **Asset + Max Loan**, visualized with Chart.js. |
| **🎯 Lifestyle Matching Engine** | `In Progress` | Weighted scoring algorithm for lifestyle preferences. |
| **🧭 Integrated Filtering** | `In Progress` | Filters properties within budget and ranks them by matching score. |

---


## CasaNova — 🛠️ Local Run Guide (개발 환경 설정)

## Prerequisites (Recommended)

- Assumes **macOS** with **Terminal**.
- You should have the following installed:
  
  - `git`
  - `python3` (recommended: 3.10 / 3.11 or higher)
    
- Having Conda/Anaconda installed is fine, but to avoid side effects on your existing environments, this guide will use **`venv`**.
  - We will disable Conda with `conda deactivate` in a later step.
- This guide focuses on **running the backend (Django)**.  
  The frontend is handled separately.

---

## 1. Clone the project from GitHub

Run the following commands in your terminal:

```bash
cd ~
git clone https://github.com/whtjddms0714-byte/CasaNova.git
cd CasaNova
```

⚠️ If a folder with the same name already exists, you may see an error like:

fatal: destination path 'CasaNova' already exists...

To remove the existing folder and restart from a clean state:

```bash
rm -rf ~/CasaNova
cd ~
git clone https://github.com/whtjddms0714-byte/CasaNova.git
cd CasaNova
```
## 2. (Important) Deactivate Conda

If Conda/Anaconda is active, the python path may be different from what you expect.
Deactivate Conda first:

```bash

conda deactivate
```
It is not a problem if the prompt still shows (base).
We will explicitly use venv in the next step.

If Conda is not installed, this command will simply fail and can be ignored.

```bash
##Create and activate venv

```

From the project root (CasaNova folder), create a virtual environment:

```bash
python3 -m venv venv
```

macOS / Linux

```bash
source venv/bin/activate
```
Windows (PowerShell)

```bash
venv\Scripts\Activate.ps1
```

If activation succeeds, your shell prompt will show (venv) at the beginning, for example:

```bash
(venv) username@MacBook CasaNova %
```
⚠️ Do not type (venv) as part of your commands.
(venv) is only a prompt indicator, not part of the command itself.


## 4. Move into the backend folder
With the virtual environment activated, move into the folder that contains the Django code:

```bash
cd backend
```
A manage.py file should exist directly inside backend/.

If you run python manage.py ... from the wrong directory, you may see an error such as:

```bash
python: can't open file '/.../manage.py': [Errno 2] No such file or directory
```
## 5. Install required backend packages

The top-level requirements.txt does not include all backend dependencies,
so you need to install the Django backend requirements manually.

Install the required packages with a single command:

```bash
pip install django djangorestframework django-cors-headers pandas numpy
```
Main libraries and why they are needed:

- django

    - The Django framework itself (required).

- djangorestframework

    - Used to implement the REST API.

- django-cors-headers

     - Handles CORS for communication with the frontend.

     - This is already referenced in settings.py, and if it is missing you will get:


    ```bash
    ModuleNotFoundError: No module named 'corsheaders'

    ```
- pandas, numpy

    -  Used for recommendation and data processing logic.

Optional: verify Django installation

```bash
python -c "import django; print(django.get_version())"

```

Example output:

```bash
6.0

```

## 6. Run migrations (initialize the database)

Apply Django migrations to set up the database schema:

```bash
python manage.py migrate

```
On success, the required DB tables are created.

If you see a message like:

```bash
You have X unapplied migration(s).

```

then running migrate will resolve it.

❗ If migrate fails, read the error message carefully.
For example, if it complains about a missing package, go back to Step 5 and install the missing dependency, then run migrate again.

## 7. Start the Django development server

You are now ready to run the backend server.

macOS / Linux

```bash
python3 manage.py runserver
```

Windows

```bash
python manage.py runserver
```


If the server starts successfully, you will see output similar to:

```bash
Watching for file changes with StatReloader
Django version 6.0, using settings 'casanova_server.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```


## 🤝 How to Contribute (기여 방법)

We welcome contributions from everyone!
To maintain a clean and respectful workflow, please follow the contribution standards below.

### 🔹 Code Standards

- Commits: Use imperative mood

    - Example: Add user model

- Commit Body: Required for non-trivial changes — explain why the change was needed.

- Branch Naming
```bash
type/issue-number-short-description
```
  Example: feat/12-add-financial-engine
- Pull Requests: Require minimum 2 approvals before merging.

### 🔹 Code Style (Linting)

- Backend (Python): Black + Flake8

- Frontend (TypeScript/React): ESLint + Prettier

For full contribution guidelines, refer to:

- CONTRIBUTING.md
- CODE_OF_CONDUCT.md

## ⚖️ License (라이선스)

This project is licensed under the Apache License 2.0.


 


 



