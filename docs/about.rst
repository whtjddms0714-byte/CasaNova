About the Project
=================

Purpose
-------

CasaNova is a financial-based housing recommendation system. It helps users:

- estimate a realistic housing budget based on income, debt, and loan constraints, and  
- find properties that match both financial capacity and lifestyle preferences.

.. note::

   Real loan data cannot be used in this project due to dataset access limitations.  
   Therefore, the current system uses synthetically generated loan products as placeholders,  
   while keeping the architecture compatible with real datasets in the future.

Target Users
------------

The system is designed primarily for:

- young adults in their 20s and 30s,
- first-time home seekers,
- users who want to understand how financial constraints influence housing choices.

High-Level Features
-------------------

Loan Recommendation
~~~~~~~~~~~~~~~~~~~

- Generates 150 placeholder loan products (temporary synthetic data).
- Each product includes:
  
  - interest rate  
  - repayment period  
  - minimum income & credit requirements  
  - preferential conditions (text-based rules)

- Computes:

  - DSR-based repayment capacity  
  - maximum loan amount via PMT formula (Decimal-based)  
  - composite ranking score including preferential benefits  

- Existing debt handling:

  - If the user enters a monthly repayment amount → use it directly  
  - If the user enters debt principal only → estimate repayment using PMT  

Budget Estimation
~~~~~~~~~~~~~~~~~

- Total budget = user assets + selected loan amount  
- Supports optional user-defined budget cap (10,000 KRW units)  
- Applied to property filtering before ranking  

Infrastructure-Based Property Recommendation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Infrastructure categories:

  - transportation  
  - parks  
  - schools  
  - marts  

- Distance computation:

  - vectorized Haversine formula  
  - converted to walking time (4 km/h)  
  - mapped to a grade table (``classify_grade``)

- User priorities:

  - drag-and-drop UI assigns rank weights (4 → 1)  
  - weights are used to compute the final infrastructure score  

Web-Based Workflow
------------------

Step 1 — User Input
~~~~~~~~~~~~~~~~~~~

``/info-1/`` collects:

- financial profile  
- lifestyle preferences  
- infrastructure priorities  

Step 2 — Loan Recommendation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``/loans.html`` sends the user profile to the Django API and shows ranked loan products.

Step 3 — Property Recommendation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``/properties.html`` ranks and filters properties using:

- final budget  
- selected loan amount  
- infrastructure scoring  


