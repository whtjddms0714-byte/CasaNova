CasaNova Documentation
======================

Welcome to the documentation for **CasaNova: Financial-Based Personalized Housing Recommendation System**.

CasaNova is a web-based system that:

- analyzes a user's financial status to estimate a realistic housing budget, and  
- recommends properties based on accessibility to key infrastructure (transportation, schools, parks, marts).

The project consists of:

- a Django-based backend providing JSON APIs,
- an engine layer for financial and infrastructure scoring logic,
- CSV-based datasets for properties and infrastructure, and
- a static Jekyll website for the user-facing simulator.

------------------------------------------------------------
Contents
------------------------------------------------------------

.. toctree::
   :maxdepth: 2
   :caption: User Documentation

   about
   getting_started
   usage

.. toctree::
   :maxdepth: 2
   :caption: Technical Documentation

   technical_overview
   api_reference
   configuration
   maintenance_troubleshooting

.. toctree::
   :maxdepth: 2
   :caption: Project Information

   contribution
   faq
   release_notes

------------------------------------------------------------
Project Overview
------------------------------------------------------------

CasaNova provides:

- a **loan recommendation engine** using DSR-based capacity and eligibility rules,
- a **property recommendation engine** using distance-based infrastructure scoring, and
- a **simple three-step web workflow** (input → loan selection → property results).

This documentation describes how to install, configure, and extend CasaNova.

------------------------------------------------------------
Index
------------------------------------------------------------

* :ref:`genindex`
* :ref:`search`
