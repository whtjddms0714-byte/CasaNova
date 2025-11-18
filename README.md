# 🏠 CasaNova: Financial-Based Personalized Housing Recommendation System

**_New Home, New Start._**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Latest Release](https://img.shields.io/github/v/release/whtjddms0714-byte/CasaNova?color=success)](https://github.com/whtjddms0714-byte/CasaNova/releases/tag/v0.0.1)
[![Contributors](https://img.shields.io/github/contributors/whtjddms0714-byte/CasaNova)](https://github.com/whtjddms0714-byte/CasaNova/graphs/contributors)

---

## 🌟 Project Introduction (프로젝트 소개)

CasaNova is an open-source web application designed to help **young adults in their 20s** confirm a **realistic housing budget** based on their current assets and income.

Unlike traditional real estate platforms, CasaNova integrates and analyzes complex factors—such as **DSR/DTI-emulating loan regulations** and youth-targeted mock financial products—to support financially savvy and stable housing decisions.

This project is fully open-source and free for anyone to use and contribute to.

---

## ✨ Core Features (주요 기능)

The heart of CasaNova lies in its two primary engines: **Financial Analysis** and **Preference Matching**.

| Feature | Status | Description |
| :--- | :--- | :--- |
| **💰 Financial Simulation Engine** | `Planned` | DSR/DTI logic to calculate max loan amount and monthly repayment. |
| **📈 Budget Confirmation & Visualization** | `In Progress` | Calculates budget as **Asset + Max Loan**, visualized with Chart.js. |
| **🎯 Lifestyle Matching Engine** | `Ready` | Weighted scoring algorithm for lifestyle preferences. |
| **🧭 Integrated Filtering** | `Planned` | Filters properties within budget and ranks them by matching score. |

---

## 🛠️ Development Environment Setup (개발 환경 설정)

CasaNova uses both Python and Node.js.  
To run the project, set up the **Backend API** and **Frontend App**.

---

### 1. Technical Stack

- **Backend:** Python 3.10+ / Django 5.x / MySQL  
- **Frontend:** TypeScript / React / Tailwind CSS  
- **Tooling:** Git, GitHub Actions, Chart.js

---

### 2. Prerequisite (필수 요구 사항)

Install the following tools:

- **Git**  
- **Python 3.10+** (with pip)  
- **Node.js** (npm or yarn)  
- **MySQL client** (for local DB connection)

---

### 3. Running the Development Server (서버 실행)

Clone the repository and follow the setup steps.

```bash
# 1. Clone the repository
git clone https://github.com/whtjddms0714-byte/CasaNova.git
cd CasaNova
```

#### 3-1. Backend Server Setup (Django API - Python 기반)

```bash
# (Optional) Create and activate a Python virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux/Git Bash

# Install backend dependencies
pip install -r requirements.txt

# Run database migrations (requires MySQL setup)
python manage.py makemigrations
python manage.py migrate

# Start the Django API server
python manage.py runserver
```
API accessible at: ➡ http://localhost:8000
 (Django default port)

#### 3-2. Frontend Server Setup (Vite + React/TypeScript)

```bash
# Move into the frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server (Vite)
npm run dev
```
App accessible at: ➡ http://localhost:5173
 (Vite default port)


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


 


 



