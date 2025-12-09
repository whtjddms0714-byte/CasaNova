Getting Started
===============

This guide explains how to set up and run the CasaNova backend and the Jekyll-based simulator locally.

Prerequisites
-------------

Install the following tools:

- Python 3.10+ and ``pip``
- Git
- Node.js (for any optional frontend tooling, if used)
- A modern web browser

Clone the Repository
--------------------

.. code-block:: bash

   git clone https://github.com/whtjddms0714-byte/CasaNova.git
   cd CasaNova

Python Environment
------------------

Optionally create and activate a virtual environment:

.. code-block:: bash

   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate

Install Python dependencies:

.. code-block:: bash

   pip install -r requirements.txt

Database Setup
--------------

By default, CasaNova uses SQLite.

Apply migrations:

.. code-block:: bash

   python manage.py migrate

Running the Django Backend
--------------------------

Start the development server:

.. code-block:: bash

   python manage.py runserver

The API will be available at:

- ``http://127.0.0.1:8000/api/recommend-loans/``
- ``http://127.0.0.1:8000/api/recommend-properties/``

Static Web Frontend (Jekyll)
----------------------------

The Jekyll-based static website provides:

- ``/index.html``: user input form,
- ``/loans.html``: loan recommendation and selection,
- ``/properties.html``: property recommendations.

For local development you can:

- Serve the ``frontend`` or website folder via a simple HTTP server, or
- Use GitHub Pages to host the Jekyll site (configured in the repository).

Data Files
----------

The backend expects CSV datasets in ``backend/data/`` (or equivalent ``data/`` directory), including:

- ``estate.csv``: property listings,
- ``station.csv``: transit stations,
- ``park.csv``: parks,
- ``mart.csv``: marts,
- ``school.csv``: schools.

Ensure that these files are present and follow the expected schema described in :doc:`technical_overview`.

