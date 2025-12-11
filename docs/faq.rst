FAQ
===

Frequently Asked Questions
--------------------------

Q: What does CasaNova do?
-------------------------

CasaNova estimates a realistic housing budget from a user's financial
information and recommends properties based on both budget and
infrastructure accessibility.

Q: How is the loan limit calculated?
------------------------------------

The loan limit is calculated using a DSR-based approach. The engine:

- computes the maximum affordable monthly payment based on income and DSR,
- subtracts existing monthly debt payments,
- applies a PMT-like formula given the loan rate and tenor.

Q: What data is used for property recommendations?
--------------------------------------------------

The system uses CSV datasets that include:

property listings (price and location),

infrastructure locations (stations, parks, marts, schools).

Only geospatial and price-related fields are required by the engine. Additional metadata fields may be included for display purposes.

Data Source Note: All underlying data, including the comprehensive Seoul Metropolitan Real Estate data (from the Korea National Statistical Office) and various infrastructure location data, are sourced from the Seoul Metropolitan Government Public Data Portal (서울시 공공데이터 포털).
Q: Can I use my own datasets?
-----------------------------

Yes. You can replace the CSV files in the ``data/`` directory with your own
as long as:

- the required columns are present, or
- the engine code is updated to match the new schema.

Note on Data Format: All custom datasets must adhere to the required geospatial and price schemas to function correctly with the core recommendation engine.

Q: Is authentication required to use the APIs?
----------------------------------------------

No. The current version does not require authentication.  
For production use, you should add appropriate authentication and access control.

Q: Does CasaNova store user data?
---------------------------------

The reference implementation does not persist user profiles in the backend.
The browser temporarily stores user input in ``localStorage`` for the
duration of the session.

Q: How do I change the API URL used by the frontend?
----------------------------------------------------

In the Jekyll pages, update the ``API_BASE`` constant:

.. code-block:: javascript

   const API_BASE = "http://your-backend-domain/api";

Q: Can I deploy this in production?
-----------------------------------

The current implementation is designed as a prototype and educational example.
Before a production deployment, you should:

- review security settings,
- secure the API,
- configure CORS appropriately,
- set up a production-ready database and hosting environment.

