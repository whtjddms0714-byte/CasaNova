Technical Overview
==================

This section describes the internal architecture of CasaNova.

High-Level Architecture
-----------------------

CasaNova consists of:

- **Django backend**

  - Project: ``casanova_server``
  - App: ``casanova_app``
  - API endpoints under ``/api/``

- **Engine layer**

  - Located under ``backend/casanova_app/engine/``
  - Contains core business logic for finance and infrastructure

- **Data layer**

  - CSV datasets stored under ``data/``
  - Loaded via the engine data loader

- **Static web frontend**

  - Jekyll pages (``index.html``, ``loans.html``, ``properties.html``)
  - Communicates with the backend APIs via HTTP requests

Backend Project Structure
-------------------------

Typical backend layout:

.. code-block:: text

   backend/
   ├── manage.py
   ├── casanova_server/
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   ├── casanova_app/
   │   ├── urls.py
   │   ├── views.py
   │   └── engine/
   │       ├── data_loader.py
   │       ├── finance.py
   │       ├── infra.py
   │       └── pipeline.py
   └── data/
       ├── estate.csv
       ├── station.csv
       ├── park.csv
       ├── mart.csv
       └── school.csv

Engine: Data Loading (engine.data_loader)
-----------------------------------------

The data loader centralizes file paths and dataset loading.

- ``BASE_DIR``: project base directory
- ``DATA_DIR``: directory containing CSV datasets

Functions:

- ``load_loan_products() -> List[dict]``

  Returns a list of loan product dictionaries with fields such as:

  - ``name``
  - ``rate``
  - ``years``
  - ``benefit_condition``
  - ``min_income``
  - ``min_credit``

- ``load_estate_and_infra() -> Tuple[pd.DataFrame, Dict[str, pd.DataFrame]]``

  Loads:

  - ``estate.csv`` as the main property dataset,
  - ``station.csv``, ``park.csv``, ``mart.csv``, ``school.csv`` as infrastructure datasets.

Engine: Financial Logic (engine.finance)
----------------------------------------

Key functions:

- ``check_preferential(user, loan) -> bool``

  Checks whether the user satisfies any preferential condition described in
  ``loan["benefit_condition"]`` (e.g., newlywed, young adult, low-income).

- ``check_eligibility(user, loan) -> bool``

  Ensures user meets minimum income and credit score requirements.

- ``calculate_max_loan(user, loan) -> int``

  Computes the maximum loan amount based on:

  - monthly income,
  - DSR ratio,
  - existing debt principal and/or monthly payment,
  - loan interest rate and duration.

  Uses a PMT-like formula:

  .. code-block:: python

     max_loan = available_monthly * (1 - (1 + r) ** (-n)) / r

- ``recommend_loans(user, loan_products) -> List[Tuple[str, float, int]]``

  Iterates over loan products, computes:

  - maximum loan per product,
  - a composite score based on loan capacity and interest rate,
  - optional preferential bonus.

  Returns a sorted list of ``(name, score, max_loan)`` tuples.

Engine: Infrastructure Logic (engine.infra)
------------------------------------------

Key functions:

- ``classify_grade(value: float) -> int``

  Maps walking time (in minutes) to a score in the range 30–100.

- ``haversine_vec(lat1, lon1, lat2, lon2)``

  Vectorized Haversine implementation to compute distances (km) between
  arrays of coordinates.

- ``nearest_infra_vectorized(houses_df, infra_df)``

  For each property, finds the nearest infrastructure point and returns the
  walking time in minutes (assuming 4 km/h).

- ``calculate_distance(df_estate, infra_df, col_name)``

  Adds a walking-time column (e.g., ``"Park (min)"``, ``"Transport (min)"``)
  to the estate DataFrame.

- ``calculate_infra_score(df, weights)``

  Computes an aggregated ``Infrastructure Score`` by weighted sum of:

  - ``Park Score``
  - ``School Score``
  - ``Mart Score``
  - ``Transport Score``

Engine: Recommendation Pipeline (engine.pipeline)
-------------------------------------------------

The pipeline brings finance and infrastructure together.

- ``recommend_estate(user, loan_amount, df)``

  Steps:

  1. Compute total budget:

     .. code-block:: python

        total_budget_won = user["asset"] + loan_amount
        total_budget_10k = total_budget_won / 10_000

     Optionally cap with ``user["budget_limit"]``.

  2. Filter by preferred district (``target_gu``) using the ``address`` column.

  3. Compute infrastructure score via ``calculate_infra_score``.

  4. Filter properties with ``price_10k <= total_budget_10k``.

  5. Sort by ``Infrastructure Score`` descending.

Data Schema
-----------

Estate Dataset (estate.csv)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``address``: full property address
- ``building_name``: name of the building or complex
- ``price_10k``: price in units of 10,000 KRW
- ``latitude``: latitude (WGS84)
- ``longitude``: longitude (WGS84)

Infrastructure Datasets
~~~~~~~~~~~~~~~~~~~~~~~

- ``station.csv``

  - ``station_name``
  - ``latitude``
  - ``longitude``

- ``park.csv``

  - ``park_name``
  - ``region``
  - ``address``
  - ``latitude``
  - ``longitude``

- ``mart.csv``

  - ``lot_address``
  - ``road_address``
  - ``mart_name``
  - ``mart_type``
  - ``longitude``
  - ``latitude``

- ``school.csv``

  - ``school_name``
  - ``school_level``
  - ``lot_address``
  - ``road_address``
  - ``latitude``
  - ``longitude``

Frontend Workflow
-----------------

- ``index.html``: collects user profile and preferences, stores them in
  ``localStorage`` and navigates to ``/loans.html``.

- ``loans.html``: requests ``/api/recommend-loans/``, displays loan products,
  and stores the chosen loan in ``localStorage`` before navigating to
  ``/properties.html``.

- ``properties.html``: sends the final user info and selected loan to
  ``/api/recommend-properties/`` and displays the recommended properties.


