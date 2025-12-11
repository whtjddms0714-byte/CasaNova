Getting Started
===============

This guide explains how to set up and run the CasaNova backend locally.
The frontend (Jekyll static pages) runs separately and is optional for backend testing.

Prerequisites
-------------

Before starting, ensure the following tools are installed:

- Python 3.10+ and ``pip``
- Git
- (Optional) Conda / Anaconda
- A modern web browser

For macOS users, the guide assumes usage of the terminal.
Windows is fully supported with PowerShell.

1. Clone the Repository
-----------------------

.. code-block:: bash

   git clone https://github.com/whtjddms0714-byte/CasaNova.git
   cd CasaNova

If the folder already exists, delete it before cloning again:

.. code-block:: bash

   rm -rf ~/CasaNova

2. Disable Conda (Important)
----------------------------

If Conda/Anaconda is active, it may override Python paths:

.. code-block:: bash

   conda deactivate

If Conda is not installed, ignore this step.

3. Create and Activate a Virtual Environment
--------------------------------------------

Create a new virtual environment:

.. code-block:: bash

   python3 -m venv venv

Activate it:

**macOS / Linux**

.. code-block:: bash

   source venv/bin/activate

**Windows (PowerShell)**

.. code-block:: bash

   venv\Scripts\Activate.ps1

If activation is successful, the prompt will look like:

::

   (venv) username@computer:~/CasaNova

4. Move into the Backend Folder
-------------------------------

Django code resides inside the ``backend`` directory:

.. code-block:: bash

   cd backend

Make sure ``manage.py`` exists here.  
Running Django from the wrong folder will cause:

::

   python: can't open file 'manage.py'

5. Install Required Python Packages
-----------------------------------

The root ``requirements.txt`` does **not** include backend dependencies.

Install them manually:

.. code-block:: bash

   pip install django djangorestframework django-cors-headers pandas numpy

Package summary:

- **django** — web framework  
- **djangorestframework** — API utilities  
- **django-cors-headers** — CORS support  
- **pandas / numpy** — used in recommendation logic  

(Optional) check Django installation:

.. code-block:: bash

   python -c "import django; print(django.get_version())"

6. Apply Database Migrations
----------------------------

.. code-block:: bash

   python manage.py migrate

This creates the default SQLite database.

If you see:

::

   You have X unapplied migration(s).

simply run ``migrate`` again.

7. Run the Django Development Server
------------------------------------

Start the server:

**macOS / Linux**

.. code-block:: bash

   python3 manage.py runserver

**Windows**

.. code-block:: bash

   python manage.py runserver

Expected output:

::

   Watching for file changes with StatReloader
   Django version X.X, using settings 'casanova_server.settings'
   Starting development server at http://127.0.0.1:8000/

API endpoints will be available at:

- ``http://127.0.0.1:8000/api/recommend-loans/``
- ``http://127.0.0.1:8000/api/recommend-properties/``

Stop the server with ``CTRL + C``.

8. (Optional) Running the Jekyll Frontend
-----------------------------------------

CasaNova includes a static HTML simulator located in the ``website/`` directory.

If you want to test the full workflow:

.. code-block:: bash

   cd ../website
   bundle install
   bundle exec jekyll serve --livereload

The site will run at:

::

   http://127.0.0.1:4000/

The frontend communicates with Django using:

.. code-block:: javascript

   const API_BASE = "http://127.0.0.1:8000/api";

9. Required Data Files
----------------------

The backend expects CSV datasets in the ``data/`` directory:

.. code-block:: text

   data/
   ├── estate.csv
   ├── station.csv
   ├── park.csv
   ├── mart.csv
   └── school.csv

If these files are missing, the recommendation API will raise a 500 error.

Refer to :doc:`technical_overview` for the expected column structure.

End of Getting Started
----------------------
