About the Project
=================

Purpose
-------

CasaNova is a financial-based housing recommendation system. It helps users:

- estimate a realistic housing budget based on income, debt, and loan constraints, and
- find properties that match both financial capacity and lifestyle preferences.

Target Users
------------

The system is designed primarily for:

- young adults in their 20s and 30s,
- first-time home seekers,
- users who need to understand how loan constraints affect housing options.

High-Level Features
-------------------

- **Loan Recommendation**

  - Evaluates multiple loan products with different interest rates, tenors, and eligibility conditions.
  - Applies DSR-based capacity logic using a PMT-style formula.
  - Computes the maximum loan amount per product and ranks products by a composite score.

- **Budget Estimation**

  - Combines user's asset amount with the selected loan limit.
  - Supports an optional user-defined budget cap in 10,000 KRW units.

- **Infrastructure-Based Property Recommendation**

  - Uses distance to transportation, parks, schools, and marts.
  - Converts walking time into scores and aggregates them into an infrastructure score.
  - Filters properties within the budget and ranks them by score.

- **Web-Based Workflow**

  - Step 1: User input (financial profile, preferences).
  - Step 2: Loan recommendation and selection.
  - Step 3: Property recommendation based on the final budget.

Core Components
---------------

- **Backend (Django)**

  - REST-like API endpoints under ``/api/``.
  - Engine modules for finance and infrastructure logic.
  - CSV-based datasets loaded at runtime.

- **Engine Layer**

  - ``engine.finance``: loan capacity and recommendation logic.
  - ``engine.infra``: distance-based scoring.
  - ``engine.pipeline``: end-to-end property recommendation.

- **Frontend (Jekyll Website)**

  - Simple HTML/JavaScript pages:
    - ``index.html`` (input form),
    - ``loans.html`` (loan selection),
    - ``properties.html`` (property results).
  - Communicates with Django APIs via ``fetch`` calls.

Licensing
---------

CasaNova is intended to be used as an open-source educational and experimental project.  
The exact license is defined in the project's ``LICENSE`` file in the repository root.

