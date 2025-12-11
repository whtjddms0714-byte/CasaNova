About the Project
=================

Purpose
-------

CasaNova is a financial-based housing recommendation system. It helps users:

- estimate a realistic housing budget based on income, debt, and loan constraints, and  
- find properties that match both financial capacity and lifestyle preferences.

> **Note:**  
> Real loan data cannot be used in this project due to data access limitations.  
> Therefore, the current system uses **synthetically generated loan products** as placeholders,  
> while keeping the architecture compatible with real datasets in the future.

Target Users
------------

The system is designed primarily for:

- young adults in their 20s and 30s,  
- first-time home seekers,  
- users who want to understand how financial constraints influence housing choices.

High-Level Features
-------------------

### **Loan Recommendation**
- Generates a set of 150 placeholder loan products (temporary synthetic data).  
  Each includes:
  - interest rate,
  - repayment period,
  - minimum income & credit requirements,
  - preferential conditions expressed as text patterns.
- Computes:
  - DSR-based monthly repayment capacity,
  - maximum loan amount using a PMT-style formula with `Decimal`,
  - a composite ranking score that includes preferential benefits.
- Existing debt handling:
  - If the user provides a monthly repayment amount → it is used directly.  
  - If only the principal is provided → a PMT-based estimate is used.

### **Budget Estimation**
- Total budget = **user assets + selected loan amount**.
- Supports optional user-defined **budget cap** (in 10,000 KRW units).
- Budget is applied before property filtering.

### **Infrastructure-Based Property Recommendation**
- Four infrastructure types:
  **transportation, parks, schools, marts**.
- Infrastructure distance is computed by:
  - vectorized Haversine formula,
  - converting distance to walking time (4 km/h).
- Walking time is mapped into scores using a grade table (`classify_grade`).
- User-defined drag-and-drop priorities are converted into weight values (4 → 1).
- These weights are used to compute a weighted infrastructure score.

### **Web-Based Workflow**
- **Step 1 — User Input**  
  `/info-1/` collects financial profile, lifestyle preferences, and infrastructure priorities.

- **Step 2 — Loan Recommendation**  
  `/loans.html` sends the user profile to the Django API and displays ranked loan products.

- **Step 3 — Property Recommendation**  
  `/properties.html` filters and ranks properties using:
  - the user’s budget,
  - selected loan amount,
  - infrastructure scoring.

Core Components
---------------

### **Backend (Django)**
- REST-style API endpoints under `/api/`:
  - `/api/recommend-loans/` (POST)
  - `/api/recommend-properties/` (POST)
- Engine modules for computation:
  - DSR-based financial logic,
  - Haversine distance computation & scoring,
  - integrated filtering pipeline.
- Property and infrastructure data are loaded from CSV files.

### **Engine Layer**
- `engine.finance`  
  DSR logic, PMT calculation, synthetic loan product evaluation.
- `engine.infra`  
  Vectorized distance calculation and scoring mechanisms.
- `engine.pipeline`  
  Budget filtering → region filtering → scoring → ranking.

### **Frontend (Jekyll Website)**
- Static HTML/JavaScript pages:
  - `/info-1/` — input form  
  - `/loans.html` — loan recommendation  
  - `/properties.html` — property recommendation
- Communicates with Django via `fetch()` requests.
- Uses `localStorage` to store user inputs and selections across steps.

Licensing
---------

CasaNova is an open-source educational and experimental project.  
The license is provided in the `LICENSE` file at the repository root.

