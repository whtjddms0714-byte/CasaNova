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

Common Request Shape
--------------------

Most endpoints expect a top-level JSON object containing a ``user_info`` field:

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
       "weights": [4, 3, 2, 1]
     }
   }

- ``weights`` is an array of four integers derived from the drag-and-drop
  infrastructure priorities on the frontend.

  The current implementation uses a descending scheme:

  - 1st priority → weight 4  
  - 2nd priority → weight 3  
  - 3rd priority → weight 2  
  - 4th priority → weight 1  

  and passes them to the engine as:

  - ``weights[0]``: Park weight  
  - ``weights[1]``: School weight  
  - ``weights[2]``: Mart weight  
  - ``weights[3]``: Transport weight  

Error Format
------------

On errors, endpoints generally return a JSON object with an ``error`` field,
for example:

.. code-block:: json

   {
     "error": "user_info required"
   }

HTTP status codes are used to distinguish error types.

Endpoints
---------

Loan Recommendation
-------------------

**URL**

- ``POST /api/recommend-loans/``

**Description**

Evaluates loan products for a given user and returns a ranked list based on
loan capacity and preferential conditions.

In the current prototype, loan products are **synthetically generated** in the
backend (e.g., ``"Dream Home 1"``–``"Dream Home 150"``), but the API contract
is designed to be compatible with real loan datasets in the future.

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
       "weights": [4, 3, 2, 1]
     }
   }

**Response (200 OK)**

.. code-block:: json

   {
     "loan_recommendations": [
       {
         "name": "Dream Home 1",
         "score": 82.35,
         "max_loan": 123000000
       },
       {
         "name": "Dream Home 2",
         "score": 79.42,
         "max_loan": 110000000
       }
     ]
   }

- ``name``: internal loan product name (synthetic in the current prototype).
- ``score``: composite recommendation score (higher is better).
- ``max_loan``: maximum loan amount (KRW) under the user's DSR constraint.

**Error Responses**

- ``400 Bad Request``: missing or invalid ``user_info``.

  .. code-block:: json

     { "error": "user_info required" }

- ``405 Method Not Allowed``: method other than POST.

  .. code-block:: json

     { "error": "POST only" }

- ``500 Internal Server Error``: unexpected error in the backend.

  .. code-block:: json

     { "error": "..." }

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
       "weights": [4, 3, 2, 1]
     },
     "selected_loan_amount": 123000000
   }

- ``selected_loan_amount``: the loan limit chosen on the loan recommendation page.
  If the user **skips loan selection**, this value can be ``0``; in that case,
  recommendations are based on the user's assets only.

**Response (200 OK, success)**

.. code-block:: json

   {
     "message": "success",
     "properties": [
       {
         "address": "서울특별시 강남구 ...",
         "building_name": "Sample Residence",
         "price_10k": 22000,
         "Infrastructure Score": 87.5,
         "school_distance_min": 8,
         "mart_distance_min": 12,
         "transport_distance_min": 5,
         "park_distance_min": 15
       }
     ]
   }

Field meanings:

- ``address``: full text address of the property.
- ``building_name``: name of the building (some rows may contain generic or missing names).
- ``price_10k``: price in units of 10,000 KRW.
- ``Infrastructure Score``: aggregated infrastructure score (higher is better).
- ``*_distance_min``: approximate walking time (minutes) to the nearest:
  - ``school_distance_min`` – school
  - ``mart_distance_min`` – mart / supermarket
  - ``transport_distance_min`` – station / public transport
  - ``park_distance_min`` – park

If no valid infrastructure data is available for a category, the corresponding
distance may be ``null`` in the JSON response.

**Response (no properties found)**

If no suitable properties match the budget and filters, the backend returns:

.. code-block:: json

   {
     "message": "No suitable properties were found. Please adjust your budget or location."
   }

In this case, the ``properties`` field is omitted.

**Error Responses**

- ``400 Bad Request``: missing ``user_info`` or ``selected_loan_amount``.

  .. code-block:: json

     { "error": "user_info required" }

  or

  .. code-block:: json

     { "error": "selected_loan_amount required" }

- ``405 Method Not Allowed``: method other than POST.

  .. code-block:: json

     { "error": "POST only" }

- ``500 Internal Server Error``: unexpected error.

  .. code-block:: json

     { "error": "..." }

Admin Interface
---------------

The default Django admin interface is available at:

- ``/admin/``

It is not directly used by the frontend but can be leveraged for future extensions
(e.g., managing datasets, configuration, or user profiles).

