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

🛠️ Development Environment Setup (개발 환경 설정)CasaNova uses both Python and Node.js.To run the project, set up the Backend API and Frontend App.1. Technical StackBackend: Python 3.10+ / Django 5.x / MySQLFrontend: TypeScript / React / Tailwind CSSTooling: Git, GitHub Actions, Chart.js2. Prerequisite (필수 요구 사항)Install the following tools:GitPython 3.10+ (with pip)Node.js (npm or yarn)MySQL client (for local DB connection)3. Running the Development Server (로컬 서버 실행 가이드)This guide focuses on setting up and running the Backend (Django) server.3-1. Clone the Project and Environment SetupFirst, clone the repository and navigate into the project directory:Bash# 1. Navigate to your desired directory
cd ~

# 2. Clone the repository
git clone https://github.com/whtjddms0714-byte/CasaNova.git

# 3. Enter the project root directory
cd CasaNova
Note on Conda: If you have Conda/Anaconda active, it's recommended to deactivate it it before proceeding: conda deactivate.3-2. Backend Server Setup (Django API - Python)The Django backend is located in the backend directory. We will use a virtual environment (venv) to manage dependencies.a. Create and Activate Virtual Environment (venv)Bash# Create a Python virtual environment
python3 -m venv venv

# Activate the virtual environment (macOS/Linux)
source venv/bin/activate
# (Windows: venv\Scripts\Activate.ps1)
b. Navigate to the Backend DirectoryMove to the directory containing the manage.py file.Bashcd backend
Attention: Django commands must be run from this directory.c. Install Essential Python PackagesInstall all required backend dependencies manually, as the main requirements.txt may be incomplete:Bashpip install django djangorestframework django-cors-headers pandas numpy
PackagePurposedjangoThe core Django framework.djangorestframeworkUsed for implementing the project's REST APIs.django-cors-headersRequired for enabling cross-origin communication (CORS) with the frontend.pandas, numpyUsed in the recommendation and data processing logic.d. Run Database MigrationsApply necessary migrations to set up the local database tables:Bashpython manage.py migrate
e. Start the Django API ServerOnce migrations are complete, start the development server:Bash# For macOS/Linux/Git Bash:
python3 manage.py runserver

# For Windows:
python manage.py runserver
API accessible at: ➡ http://127.0.0.1:8000/3-3. Frontend Server Setup (Vite + React/TypeScript)To run the React frontend alongside the Django API:Bash# 1. Return to the project root directory
cd ..

# 2. Move into the frontend directory
cd frontend

# 3. Install dependencies
npm install

# 4. Start the development server (Vite)
npm run dev
App accessible at: ➡ http://localhost:5173 (Vite default port)


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


 


 



