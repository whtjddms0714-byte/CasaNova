Technical Overview
==================

This section provides an overview of CasaNova’s system architecture, core algorithms,
and financial-based property recommendation pipeline.

System Architecture
-------------------

CasaNova consists of two major subsystems:

1. **Backend (Django + Python)**
   - Financial simulation logic
   - Loan recommendation engine
   - Property scoring and filtering
   - API endpoints for property and financial data

2. **Frontend (React + TypeScript)**
   - User interface for input forms
   - Budget visualization (Chart.js)
   - Interactive property explorer
   - API client for backend communication

Financial Simulation Engine
---------------------------

CasaNova uses a PMT-based financial model to compute the maximum loan available to the user.
The engine considers:

- Monthly income
- Credit score
- DSR ratio
- Existing debt
- Loan product conditions (interest rate, tenure, preferential benefits)

**Loan Calculation Formula**

If monthly repayment capacity is ``P``, interest rate ``r``, and number of payments ``n``:

::

    max_loan = P * (1 - (1+r)^(-n)) / r

Preferential conditions such as "사회초년생 우대" or "신혼부부 금리 인하" are evaluated through:

- marital status
- first-job status
- income level

Loan Product Data Source
------------------------

CasaNova does not generate mock loan products.  
Instead, it loads **real-world loan data** from an external dataset or public financial API.

Loan products may include:

- product name
- financial institution
- interest rate (fixed/variable)
- loan tenure
- minimum income and credit requirements
- preferential conditions (e.g., 청년, 신혼부부, 서민우대 등)

Example (CSV/DB/API loading):

.. code-block:: python

    import pandas as pd

    df_loans = pd.read_csv("data/loan_products.csv")
    loan_products = df_loans.to_dict(orient="records")


Lifestyle Matching Engine
-------------------------

CasaNova assigns weighted scores to nearby infrastructure:

- Parks
- Schools
- Marts
- Transportation hubs

Vectorized distance computation uses Haversine formulas for performance:

.. code-block:: python

    distances = haversine_vec(lat1, lon1, lat2, lon2)
    min_distances = distances.min(axis=1)

Grades from 30–100 are assigned based on distance brackets, then aggregated into a final score:

.. code-block:: python

    df['Infrastructure Score'] = (
        df['Park Score'] * w1 +
        df['School Score'] * w2 +
        df['Mart Score'] * w3 +
        df['Transport Score'] * w4
    ) / (w1 + w2 + w3 + w4)

Property Recommendation Pipeline
--------------------------------

Final recommendations follow this pipeline:

1. Estimate maximum loan amount  
2. Compute total housing budget:  
   ``asset + max_loan``  
3. Compute infrastructure scores  
4. Filter properties within budget  
5. Rank by combined lifestyle score  

This pipeline allows CasaNova to generate personalized, financially grounded property recommendations.

