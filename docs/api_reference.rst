API Reference
=============

This document provides the API specification for CasaNova’s backend service.
All endpoints follow RESTful conventions and return JSON responses.

Base URL
--------

For local development:

``http://127.0.0.1:8000/api/``


Authentication
--------------

All current endpoints are **open** for development purposes.  
Future versions may require:

- Token-based authentication
- OAuth2 or JWT integration


Endpoints Overview
------------------

The CasaNova backend exposes APIs across three domains:

1. **User Financial Analysis**
2. **Loan Simulation & Recommendation**
3. **Property Scoring & Recommendation**

The sections below describe each endpoint in detail.

-------------------------------------------------------------

1. User Financial Analysis API
-------------------------------

### **POST /api/financial/analysis/**

Evaluates the user's financial profile and computes:

- Available monthly repayment capacity (after DSR)
- Maximum loan amount
- Final recommended housing budget

**Request Body Example**

.. code-block:: json

    {
        "income_monthly": 2500000,
        "income_annual": 30000000,
        "asset": 30000000,
        "existing_debt": 0,
        "existing_annual_payment": 0,
        "credit_score": 650,
        "dsr_ratio": 0.4
    }

**Response Example**

.. code-block:: json

    {
        "monthly_repayment_capacity": 1000000,
        "max_loan_amount": 123500000,
        "recommended_budget": 153500000
    }

-------------------------------------------------------------

2. Loan Recommendation API
---------------------------

### **GET /api/loans/**

Returns the list of available loan products loaded from an external financial
dataset or API (e.g., open financial data, institutional disclosures, or
locally maintained loan product tables).

**Sample Response (truncated)**

.. code-block:: json

    [
        {
            "name": "Sample Youth Housing Loan",
            "rate": 0.021,
            "years": 30,
            "preferential_condition": "Youth / first-job support",
            "min_income": 2000000,
            "min_credit": 600
        },
        ...
    ]



### **POST /api/loans/recommend/**

Computes personalized loan recommendations using CasaNova’s scoring algorithm.

**Request Body Example**

.. code-block:: json

    {
        "income_monthly": 2500000,
        "credit_score": 650,
        "married": false,
        "first_job": true,
        "dsr_ratio": 0.4
    }

**Response Example**

.. code-block:: json

    [
        {
            "name": "Dream Home 12",
            "score": 85.23,
            "max_loan": 123500000
        },
        {
            "name": "Dream Home 44",
            "score": 80.51,
            "max_loan": 117200000
        }
    ]

-------------------------------------------------------------

3. Property Recommendation API
-------------------------------

### **POST /api/properties/recommend/**

Returns ranked property recommendations based on:

- Financial limit (total budget)
- Vectorized infrastructure scoring
- Lifestyle weights

**Request Body Example**

.. code-block:: json

    {
        "asset": 30000000,
        "selected_loan": 120000000,
        "weights": [5, 4, 3, 2],
        "target_gu": "강남구"
    }

**Response Example**

.. code-block:: json

    {
        "recommended_properties": [
            {
                "address": "서울 강남구 …",
                "building": "○○아파트",
                "price": 22000,
                "infrastructure_score": 87.5
            }
        ]
    }

-------------------------------------------------------------

Response Codes
--------------

- **200 OK** — Successful request  
- **400 Bad Request** — Missing or invalid parameters  
- **500 Internal Server Error** — Server-side computation issues  

-------------------------------------------------------------

Error Response Example
----------------------

.. code-block:: json

    {
        "error": "Invalid credit score. Must be >= 300."
    }

-------------------------------------------------------------

Notes
-----

- The API structure described here reflects the planned design for CasaNova.
- Actual implementation details may evolve as the project scales.
- Loan product data is loaded from external financial datasets or APIs and is not hard-coded in the source code.
- Frontend clients should not rely on internal scoring logic, only on returned results.

End of API Reference.
