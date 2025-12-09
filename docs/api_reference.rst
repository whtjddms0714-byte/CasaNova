<<<<<<< HEAD
<<<<<<< Updated upstream
# API 문서
=======
API Reference
=============

This section describes the HTTP API endpoints exposed by the Django backend.
=======
API Reference
=============

This document provides the API specification for CasaNova’s backend service.
All endpoints follow RESTful conventions and return JSON responses.
>>>>>>> 99cfac16b797d7549dabf44f88a13845caa126e3

Base URL
--------

<<<<<<< HEAD
In development, the default base URL is:

- ``http://127.0.0.1:8000/api/``

All examples assume this base.
=======
For local development:

``http://127.0.0.1:8000/api/``

>>>>>>> 99cfac16b797d7549dabf44f88a13845caa126e3

Authentication
--------------

<<<<<<< HEAD
No authentication is required in the current prototype.  
All endpoints accept and return JSON.

Endpoints
---------

Loan Recommendation
-------------------

**URL**

- ``POST /api/recommend-loans/``

**Description**

Evaluates loan products for a given user and returns a ranked list based on
loan capacity and preferential conditions.

**Request Body**

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

**Response (200 OK)**

.. code-block:: json

   {
     "loan_recommendations": [
       {
         "name": "Sample Loan Product",
         "score": 82.35,
         "max_loan": 123000000
       },
       {
         "name": "Another Loan Product",
         "score": 79.42,
         "max_loan": 110000000
       }
     ]
   }

**Error Responses**

- ``400 Bad Request``: missing or invalid ``user_info``.
- ``405 Method Not Allowed``: method other than POST.
- ``500 Internal Server Error``: unexpected error.

Property Recommendation
-----------------------

**URL**

- ``POST /api/recommend-properties/``

**Description**

Recommends properties based on:

- user profile,
- selected loan limit,
- infrastructure accessibility scores.

**Request Body**

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
     },
     "selected_loan_amount": 123000000
   }

**Response (200 OK, success)**

.. code-block:: json

   {
     "message": "success",
     "properties": [
       {
         "address": "서울특별시 강남구 ...",
         "building_name": "Sample Residence",
         "price_10k": 22000,
         "Infrastructure Score": 87.5
       }
     ]
   }

**Response (no properties found)**

.. code-block:: json

   {
     "message": "No suitable properties were found. Please adjust your budget or location."
   }

**Error Responses**

- ``400 Bad Request``: missing ``user_info`` or ``selected_loan_amount``.
- ``405 Method Not Allowed``: method other than POST.
- ``500 Internal Server Error``: unexpected error.

Admin Interface
---------------

The default Django admin interface is available at:

- ``/admin/``

It is not directly used by the frontend but can be leveraged for future extensions.
>>>>>>> Stashed changes
=======
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
>>>>>>> 99cfac16b797d7549dabf44f88a13845caa126e3
