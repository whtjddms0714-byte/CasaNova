.. CasaNova documentation master file, created by
   sphinx-quickstart on Wed Dec  3 20:25:52 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

CasaNova documentation
======================

<<<<<<< Updated upstream
Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.

=======
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
>>>>>>> Stashed changes

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   about
   getting_started
   usage
   technical_overview
   api_reference
   configuration
   maintenance_troubleshooting
   contribution
   faq
<<<<<<< Updated upstream
   release_notes
=======
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
>>>>>>> Stashed changes
