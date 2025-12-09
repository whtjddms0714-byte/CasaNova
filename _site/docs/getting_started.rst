<<<<<<< Updated upstream
# 설치 방법, 시작하기
=======
Getting Started
===============

This guide explains how to set up and run the CasaNova backend and the Jekyll-based simulator locally.


Prerequisites
-------------

Install the following tools before starting:

- Python 3.10+ and ``pip``
- Git
- Node.js (optional if using the React frontend)
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

   # macOS / Linux
   source venv/bin/activate

Install backend dependencies:

.. code-block:: bash

   pip install -r requirements.txt


Database Setup
--------------

CasaNova uses SQLite as the default development database.  
No additional database configuration is required for local execution.

Apply migrations to create the necessary schema:

.. code-block:: bash

   python manage.py migrate

If you intend to use MySQL or PostgreSQL in production environments,
refer to the advanced configuration settings in the project's ``settings.py``.


Running the Django Backend
--------------------------

Start the Django backend:

.. code-block:: bash

   python manage.py runserver

The API will be available at:

- ``http://127.0.0.1:8000/api/recommend-loans/``
- ``http://127.0.0.1:8000/api/recommend-properties/``


Frontend Application (React + Vite)
-----------------------------------

The main frontend is located under ``frontend/`` and is built with:

- React
- TypeScript
- Tailwind CSS
- Vite development server

To run the frontend:

.. code-block:: bash

   cd frontend
   npm install
   npm run dev

The web application will be served at:

- http://localhost:5173


Static Web Simulator (Jekyll-Based)
-----------------------------------

CasaNova also includes a lightweight Jekyll-compatible static website,
used as a simulator interface during early development.

The static pages include:

- ``index.html`` – User financial input
- ``loans.html`` – Loan recommendation and selection
- ``properties.html`` – Property recommendation results

These pages communicate with the Django backend using ``fetch`` API calls.

You may:

- Serve the static site using any lightweight local HTTP server
- Host it via GitHub Pages (recommended and already configured in the repository)


Data Files
----------

The backend requires several CSV datasets located under ``backend/data/``:

- ``estate.csv`` – Property listings
- ``station.csv`` – Transit station locations
- ``park.csv`` – Park locations
- ``mart.csv`` – Mart/store locations
- ``school.csv`` – School locations

Ensure these files exist and follow the schemas described in :doc:`technical_overview`.


You are now ready to run CasaNova locally!
>>>>>>> Stashed changes
