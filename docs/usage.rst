How to Use
==========

<<<<<<< Updated upstream
사용법, 예제
=======
This guide explains how users interact with CasaNova to obtain financial insights
and personalized housing recommendations.

Overview
--------

The workflow is divided into three main steps:

1. **User Profile Input (index.html)**  
   User enters financial and preference information.

2. **Loan Recommendation (loans.html)**  
   System recommends loan products and the user selects one.

3. **Property Recommendation (properties.html)**  
   System ranks properties based on the final budget and infrastructure scores.

User Inputs
-----------

The following fields are collected on the first page:

Financial Information
~~~~~~~~~~~~~~~~~~~~~

- Monthly income
- Credit score
- DSR ratio
- Existing debt principal
- Existing monthly debt payment (optional)
- Asset amount

Personal Attributes
~~~~~~~~~~~~~~~~~~~

- Marital status
- First-job (young adult) status
- Preferred region (district name, e.g. "강남구")

Lifestyle Preferences
~~~~~~~~~~~~~~~~~~~~~

Infrastructure weights:

- Park weight
- School weight
- Mart weight
- Transport weight

These are combined in the engine as:

.. code-block:: python

   weights = [w_park, w_school, w_mart, w_transport]

Loan Recommendation Usage
-------------------------

On ``loans.html``, the frontend:

1. Loads the saved user profile from ``localStorage``.
2. Sends a POST request to ``/api/recommend-loans/``:

   .. code-block:: json

      {
        "user_info": {
          "income_monthly": 4000000,
          "credit_score": 750,
          "dsr_ratio": 0.4,
          "existing_debt": 0,
          "existing_debt_monthly_payment": 0,
          "married": false,
          "first_job": true,
          "asset": 30000000,
          "budget_limit": 60000,
          "target_gu": "강남구",
          "weights": [5, 4, 3, 2]
        }
      }

3. Displays a table of recommended loan products with:

   - product name,
   - score,
   - maximum loan amount.

4. When the user selects a loan, the frontend stores:

   - ``casanova_selected_loan_amount``,
   - ``casanova_selected_loan_name`` (optional),

   in ``localStorage`` and redirects to ``/properties.html``.

Property Recommendation Usage
-----------------------------

On ``properties.html``, the frontend:

1. Reads ``user_info`` and the selected loan amount from ``localStorage``.
2. Displays a short summary:

   - whether a loan is used,
   - selected loan product name (if any),
   - loan limit.

3. Calls the backend:

   .. code-block:: http

      POST /api/recommend-properties/

   with body:

   .. code-block:: json

      {
        "user_info": { ... },
        "selected_loan_amount": 123000000
      }

4. Receives a list of properties with:

   - address,
   - building_name,
   - price_10k,
   - Infrastructure Score.

5. Renders the top results in a table.

End of Process
--------------

The user receives:

- a recommended loan product (optional),
- the final housing budget (asset + loan),
- a ranked list of properties that match the budget and preference profile.

The web workflow is designed to be simple and can be embedded into a
static site or GitHub Pages deployment.
>>>>>>> Stashed changes
