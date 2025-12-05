Getting Started
===============

This page explains how to set up and run the CasaNova project
for local development.

Prerequisites
-------------

- Git
- Python 3.10+ (with ``pip``)
- Node.js (npm or yarn)
- MySQL client (for local DB connection)

Clone the Repository
--------------------

.. code-block:: bash

   git clone https://github.com/whtjddms0714-byte/CasaNova.git
   cd CasaNova

Backend Setup (Django API)
--------------------------

.. code-block:: bash

   # (Optional) Create and activate virtual environment
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate

   # Install backend dependencies
   pip install -r requirements.txt

   # Run database migrations
   python manage.py makemigrations
   python manage.py migrate

   # Start the Django API server
   python manage.py runserver

The API will be available at: ``http://127.0.0.1:8000/``

Frontend Setup (Vite + React/TypeScript)
----------------------------------------

.. code-block:: bash

   cd frontend

   # Install dependencies
   npm install

   # Start the development server
   npm run dev

The web app will be available at: ``http://localhost:5173``
