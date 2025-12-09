API Reference
=============

This section describes the HTTP API endpoints exposed by the Django backend.

Base URL
--------

In development, the default base URL is:

- ``http://127.0.0.1:8000/api/``

All examples assume this base.

Authentication
--------------

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
