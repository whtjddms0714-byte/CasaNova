About the Project
=================

<<<<<<< HEAD
<<<<<<< Updated upstream
CasaNova
=======
Purpose
-------

CasaNova is an open-source financial-based housing recommendation system.
It helps users:

- estimate a realistic housing budget based on income, debt, and loan constraints, and
- find properties that match both financial capacity and lifestyle preferences.

Technology Stack
----------------

Backend:

- Python 3.10+
- Django 5.x
- Relational database (SQLite for development; MySQL or PostgreSQL recommended for production)

Frontend:

- Primary web application: TypeScript / React / Tailwind CSS (Vite dev server)
- Simulator / prototype pages: static HTML (Jekyll / GitHub Pages–friendly layout)

Tooling:

- Git and GitHub
- Optional GitHub Actions for CI/CD
- Chart.js for budget and result visualization on the frontend

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

  - Combines the user's asset amount with the selected loan limit.
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

- **Simulator Frontend (Jekyll / Static HTML)**

  - Simple HTML/JavaScript pages:
    - ``index.html`` (input form),
    - ``loans.html`` (loan selection),
    - ``properties.html`` (property results).
  - Communicates with Django APIs via ``fetch`` calls.

Licensing
---------

CasaNova is released under the **Apache License 2.0**.  
For full license terms, see the ``LICENSE`` file in the repository root.
>>>>>>> Stashed changes
=======
CasaNova: Financial-Based Personalized Housing Recommendation System
--------------------------------------------------------------------

CasaNova is an open-source web application designed to help young adults in their 20s
determine a realistic housing budget based on their current financial status.

Unlike traditional real estate platforms, CasaNova analyzes real-world financial products
and applies loan eligibility logic using actual bank loan datasets or publicly available
financial APIs. Each loan recommendation reflects authentic market conditions such as
interest rates, minimum income requirements, credit requirements, and preferential rules.

Key Objectives
--------------

- Provide transparent, data-driven housing budget estimation
- Use *real financial products* for accurate loan simulation
- Support stable and realistic housing decisions for young adults
- Offer personalized property recommendations using lifestyle preference scoring

Core Features
-------------

**1. Financial Simulation Engine**
   - Computes maximum loan amount using real loan data
   - Applies bank-specific eligibility rules and preferential conditions
   - Uses PMT-based monthly payment formula  
   - Calculates maximum loan amount under DSR constraints  
   - Evaluates loan eligibility based on income, credit score, and preferential benefits  

**2. Budget Confirmation & Visualization**
   - Total housing budget = user asset + approved maximum loan
   - Visualized using Chart.js tools  

**3. Lifestyle Matching Engine**
   - Weighted scoring algorithm based on access to parks, schools, marts, and transit  

**4. Integrated Filtering & Ranking**
   - Filters properties within realistic budgets
   - Ranks results by combined infrastructure score  

Why This Project Matters
------------------------

Housing affordability is a major challenge for young adults.
CasaNova provides a realistic, transparent, and data-grounded approach to help users
understand *what they can truly afford* using actual financial options.
>>>>>>> 99cfac16b797d7549dabf44f88a13845caa126e3
