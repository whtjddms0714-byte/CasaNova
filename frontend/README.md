# 🏠 CasaNova: Financial-Based Personalized Housing Recommendation System

**_New Home, New Start._**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Latest Release](https://img.shields.io/github/v/release/whtjddms0714-byte/CasaNova?color=success)](https://github.com/whtjddms0714-byte/CasaNova/releases/tag/v0.0.1)
[![Contributors](https://img.shields.io/github/contributors/whtjddms0714-byte/CasaNova)](https://github.com/whtjddms0714-byte/CasaNova/graphs/contributors)

## 🌟 Project Introduction (프로젝트 소개)

CasaNova is an open-source web application designed to help **young adults in their 20s** confirm a **realistic housing budget** based on their current assets and income.
Unlike traditional real estate platforms, CasaNova integrates and analyzes complex factors—such as **DSR/DTI-emulating loan regulations** and mock youth-specific financial products—to support financially savvy and stable housing decisions.

This project is developed as a **fully open-source project**, free for anyone to use and contribute to.

---

## ✨ Core Features (주요 기능)

The heart of CasaNova lies in its two primary engines: **Financial Analysis** and **Preference Matching**.

| Feature | Status | Description |
| :--- | :--- | :--- |
| **💰 Financial Simulation Engine** | `Planned` | Applies DSR/DTI logic to calculate max loan amount and monthly repayment based on user input. |
| **📈 Budget Confirmation & Visualization** | `In Progress` | Confirms final budget as $$Asset + Max Loan$$ and visualizes the repayment burden rate using **Chart.js**. |
| **🎯 Lifestyle Matching Engine** | `Ready` | Calculates a matching score for residential preferences (transportation, amenities, etc.) using a weighted algorithm. |
| **🧭 Integrated Filtering** | `Planned` | Filters properties **only within the confirmed budget**, then presents the final recommendation list by matching score. |

---

## 🛠️ Development Environment Setup (개발 환경 설정)

CasaNova is built using a dual Python/Node.js stack. To get started, you must set up both the Backend API and the Frontend App.

### 1. Technical Stack

* **Backend:** Python 3.10+ / **Django 5.x** / **MySQL**
* **Frontend:** **TypeScript** / **React** / **Tailwind CSS**
* **Tooling:** Git/GitHub, GitHub Actions, Chart.js

### 2. Prerequisite (필수 요구 사항)

The following tools must be installed on your system:
* **Git**
* **Python** (3.10+ with pip)
* **Node.js** (with npm/yarn)
* **MySQL client** (for local development)

### 3. Running the Development Server (서버 실행)

Clone the repository and follow the two-part setup process:

```bash
# 1. Clone the repository
git clone [https://github.com/whtjddms0714-byte/CasaNova.git](https://github.com/whtjddms0714-byte/CasaNova.git)
cd CasaNova

### 3-1. Backend Server Setup (Django API - Python-Based) Since the core logic is in the Django backend, this is the primary setup
