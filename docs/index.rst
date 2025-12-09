<<<<<<< HEAD
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
=======
CasaNova Documentation
======================

Welcome to the official documentation for **CasaNova: Financial-Based Personalized Housing Recommendation System**.

CasaNova is an open-source platform designed to help young adults in their 20s determine a realistic housing budget based on financial simulations and personalized lifestyle matching.

This documentation provides installation instructions, technical architecture details, API specifications, configuration manuals, contribution guidelines, and release notes.
>>>>>>> 99cfac16b797d7549dabf44f88a13845caa126e3

------------------------------------------------------------
Contents
------------------------------------------------------------
<<<<<<< HEAD
>>>>>>> Stashed changes

.. toctree::
   :maxdepth: 2
   :caption: Contents:
=======

.. toctree::
   :maxdepth: 2
   :caption: User Documentation
>>>>>>> 99cfac16b797d7549dabf44f88a13845caa126e3

   about
   getting_started
   usage
<<<<<<< HEAD
=======

.. toctree::
   :maxdepth: 2
   :caption: Technical Documentation

>>>>>>> 99cfac16b797d7549dabf44f88a13845caa126e3
   technical_overview
   api_reference
   configuration
   maintenance_troubleshooting
<<<<<<< HEAD
   contribution
   faq
<<<<<<< Updated upstream
   release_notes
=======
=======

.. toctree::
   :maxdepth: 2
   :caption: Project Information

   contribution
   faq
>>>>>>> 99cfac16b797d7549dabf44f88a13845caa126e3
   release_notes

------------------------------------------------------------
Project Overview
------------------------------------------------------------

<<<<<<< HEAD
CasaNova provides:

- a **loan recommendation engine** using DSR-based capacity and eligibility rules,
- a **property recommendation engine** using distance-based infrastructure scoring, and
- a **simple three-step web workflow** (input → loan selection → property results).

This documentation describes how to install, configure, and extend CasaNova.
=======
CasaNova integrates:

- **Financial Simulation Engine** (loan eligibility, DSR-based repayment logic)
- **Lifestyle Matching Algorithm** (distance-based infrastructure scoring)
- **Housing Budget Visualization & Recommendation**
- **Mock loan dataset of 150 products**
- **Vectorized NumPy computation pipeline for performance**

CasaNova is fully open-source and encourages developers to contribute improvements,
algorithm enhancements, UI/UX extensions, or real-estate data integrations.

------------------------------------------------------------
Getting Help
------------------------------------------------------------

- For common issues, refer to: :doc:`faq`
- For API usage, refer to: :doc:`api_reference`
- To contribute, read: :doc:`contribution`
>>>>>>> 99cfac16b797d7549dabf44f88a13845caa126e3

------------------------------------------------------------
Index
------------------------------------------------------------

* :ref:`genindex`
* :ref:`search`
<<<<<<< HEAD
>>>>>>> Stashed changes
=======
>>>>>>> 99cfac16b797d7549dabf44f88a13845caa126e3
