<<<<<<< HEAD
FAQ
===

<<<<<<< Updated upstream
자주 묻는 질문과 답변.
=======
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

- property listings (price and location),
- infrastructure locations (stations, parks, marts, schools).

Only geospatial and price-related fields are required by the engine.
Additional metadata fields may be included for display purposes.

Q: Can I use my own datasets?
-----------------------------

Yes. You can replace the CSV files in the ``data/`` directory with your own
as long as:

- the required columns are present, or
- the engine code is updated to match the new schema.

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
>>>>>>> Stashed changes
=======
.. _faq:

Frequently Asked Questions (FAQ)
================================

Q: Are the DSR/Loan Simulation results guaranteed to be accurate by real banks?
---------------------------------------------------------------------------------

A: **No, they are not guaranteed to be exact.** CasaNova uses a **mock dataset** of loan products and applies the standard **Present Value (PMT)** formula to estimate the maximum loan amount. While the simulation results are designed to be **highly similar** to typical banking results, they are for **pre-budget determination and planning purposes only.** You should always consult with a financial institution for final, legally binding loan quotes.

Q: Where does the property and infrastructure data come from?
------------------------------------------------------

A: All data currently used by the CasaNova application is sourced from open public APIs for demonstration and educational purposes. The data sources are as follows:

- [cite_start]**Property Listings (Price & Coordinates):** Sourced from the **Seoul Real Estate API** [cite: 1] (Data Source: Seoul Open Data Plaza).
- [cite_start]**School Data:** Derived from the **National Elementary and Secondary School Data (Seoul Extraction)** [cite: 2] (Data Source: Data.go.kr).
- [cite_start]**Park Data:** Sourced from the **Seoul Public Park Information** [cite: 3] (Data Source: Seoul Open Data Plaza).
- [cite_start]**Mart Data:** Sourced from the **Seoul Large Mart Store Information** [cite: 4] (Data Source: Seoul Open Data Plaza).
- [cite_start]**Public Transport (Subway):** Sourced from the **Seoul Subway Station Information** [cite: 5] (Data Source: Seoul Open Data Plaza).
- **Loan Products:** Currently using a **Mock Data Set** based on generalized market interest rates for simulation.

Q: Can I change the importance of parks, schools, or public transport?
--------------------------------------------------------------------------

A: **Yes.** CasaNova's **Lifestyle Matching Engine** is designed to be highly customizable. During the second step of the process, you can **manually set the priority/weight** for each key infrastructure element (Park, School, Mart, Public Transport). This personalization ensures the final property recommendations accurately reflect your unique lifestyle needs.
>>>>>>> 99cfac16b797d7549dabf44f88a13845caa126e3
