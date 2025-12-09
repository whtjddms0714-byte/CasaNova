<<<<<<< HEAD
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
=======
.. _usage:

How to Use CasaNova
================================

CasaNova guides users through a clear, three-step process to determine their financial capacity and find the most suitable property based on their preferences.

1. Financial Assessment (Budget Confirmation)
--------------------------------------------

The system first establishes your realistic purchasing power by analyzing your financial inputs.

- **Input Required:** Enter your **Monthly Income**, **Available Savings**, and **Existing Monthly Debt Payments**.
- **Loan Simulation:** The system automatically calculates your **Debt Service Ratio (DSR)** and determines the maximum loan amount you qualify for.
- **Loan Product Recommendation:** Based on your financial profile, the system recommends **multiple, simulated loan products** (e.g., Dream Home, Future Plan).
- **Selection:** You must then **select one loan product number** to integrate that specific amount into your final budget.

2. Customizing Preference Weights
-----------------------------------

After confirming your budget, you define what matters most to your lifestyle.

- **Manual Adjustment:** You are presented with four key infrastructure factors: **Park**, **School**, **Mart**, and **Public Transport**.
- **Weight Setting:** You **manually adjust the priority (weight)** for each factor within the application interface. The system allows you to directly control the weights of these factors to ensure the scoring matches your personal needs.
    - *Example:* If proximity to schools is critical, set a higher weight for 'School'.

3. Final Property Recommendation
--------------------------------

The final engine combines your confirmed budget and lifestyle preferences to present the optimal housing recommendations.

- **Budget Filtering:** The system automatically **filters out any properties** that exceed your confirmed total budget (Savings + Selected Loan Amount).
- **Matching Score:** The **Infrastructure Score** is calculated for the remaining properties by multiplying the property's proximity to amenities by your personalized preference weights.
- **Final Result:** Properties are ranked and displayed in descending order based on their **Infrastructure Score**, offering you the most financially feasible and desirable housing options.
>>>>>>> 99cfac16b797d7549dabf44f88a13845caa126e3
