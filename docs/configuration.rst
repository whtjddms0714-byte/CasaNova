

# 설정 가이드
=======
Configuration Guide
===================

This guide explains how to configure CasaNova for local development and
customization.

Django Settings
---------------

The main settings module is:

- ``casanova_server/settings.py``

Key options include:

- ``DEBUG``: development flag (default ``True``).
- ``ALLOWED_HOSTS``: list of allowed hostnames in production.
- ``INSTALLED_APPS``: includes ``casanova_app`` and ``corsheaders``.
- ``MIDDLEWARE``: includes CORS middleware and standard Django middleware.
- ``DATABASES``: default SQLite configuration.
- ``LANGUAGE_CODE`` and ``TIME_ZONE``: localization and timezone.

CORS Configuration
------------------

The project enables cross-origin requests for development:

.. code-block:: python

   INSTALLED_APPS += [
       "corsheaders",
   ]

   MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")

   CORS_ALLOW_ALL_ORIGINS = True

For production, you should restrict allowed origins using:

.. code-block:: python

   CORS_ALLOW_ALL_ORIGINS = False
   CORS_ALLOWED_ORIGINS = [
       "https://your-frontend-domain",
   ]
=======
Configuration Guide
===================

This guide explains all configuration options for running the CasaNova system.
It covers backend Django settings, environment variables, frontend configurations,
and optional customization for development or production environments.

Overview
--------

CasaNova consists of two separate applications:

1. **Backend** (Python + Django): Financial simulation engine, loan logic, and API layer  
2. **Frontend** (React + TypeScript): User interface for visualization and property search  

Proper configuration ensures both services operate smoothly and securely.

-------------------------------------------------------------
Backend Configuration (Django)
-------------------------------------------------------------

Environment Variables
---------------------

The backend uses environment variables to load sensitive configuration data.
Create a `.env` file in the project root with the following:

::

    DJANGO_SECRET_KEY=your-secret-key
    DEBUG=True
    DB_NAME=casanova
    DB_USER=root
    DB_PASSWORD=your-password
    DB_HOST=localhost
    DB_PORT=3306

Description of Variables
~~~~~~~~~~~~~~~~~~~~~~~~

- **DJANGO_SECRET_KEY**  
  Required for Django security (sessions, encryption). Must be unique per installation.

- **DEBUG**  
  Set `True` for development, `False` for production.

- **DB_* variables**  
  Configure the MySQL database used by Django.


Database Configuration
----------------------

<<<<<<< HEAD
Default database (development):

.. code-block:: python

   DATABASES = {
       "default": {
           "ENGINE": "django.db.backends.sqlite3",
           "NAME": BASE_DIR / "db.sqlite3",
       }
   }

For production, you can switch to PostgreSQL or MySQL, for example:

.. code-block:: python

   DATABASES = {
       "default": {
           "ENGINE": "django.db.backends.postgresql",
           "NAME": "casanova",
           "USER": "casanova_user",
           "PASSWORD": "password",
           "HOST": "localhost",
           "PORT": "5432",
       }
   }

Data Files
----------

CasaNova expects CSV datasets in a ``data/`` directory. Example layout:

.. code-block:: text

   data/
   ├── estate.csv
   ├── station.csv
   ├── park.csv
   ├── mart.csv
   └── school.csv

You can replace these files with your own data as long as:

- column names remain consistent with the engine implementation, or
- you adjust the engine code accordingly.

Frontend API Base URL
---------------------

In the Jekyll pages, the API base URL is defined in JavaScript:

.. code-block:: javascript

   const API_BASE = "http://127.0.0.1:8000/api";

For deployment, this should be changed to the production backend URL.

Logging and Debugging
---------------------

For development:

- ``DEBUG = True`` provides detailed error pages.
- You can add logging configuration to ``settings.py`` to track API calls and errors.

For production:

- Set ``DEBUG = False``.
- Configure logging and error reporting according to your environment.

Documentation Build Requirements
--------------------------------

For building the documentation (locally or on ReadTheDocs), the following
Python packages are required. They are listed in ``docs/requirements.txt``:

.. code-block:: text

   pandas
   sphinx
   sphinx-rtd-theme

You can install them with:

.. code-block:: bash

   pip install -r docs/requirements.txt
>>>>>>> Stashed changes
=======
Example entry in `settings.py`:

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv("DB_NAME"),
            'USER': os.getenv("DB_USER"),
            'PASSWORD': os.getenv("DB_PASSWORD"),
            'HOST': os.getenv("DB_HOST", "localhost"),
            'PORT': os.getenv("DB_PORT", 3306),
        }
    }

Static Files
------------

Django collects static assets such as:

- Loan product reference JSON  
- Preprocessed infrastructure data  
- UI assets (if served from backend)

Run:

.. code-block:: bash

    python manage.py collectstatic

API Configuration
-----------------

Optional API settings in `settings.py`:

.. code-block:: python

    API_BASE_URL = "/api/"
    PAGINATION_SIZE = 50
    ENABLE_LOGGING = True

These can be customized depending on deployment needs.

-------------------------------------------------------------
Frontend Configuration (React + Vite)
-------------------------------------------------------------

Project Configuration File
--------------------------

The frontend uses **Vite** for configuration, controlled through:

- `vite.config.ts`
- `.env` files for environment variables

Frontend Environment Variables
------------------------------

Create `.env` files inside the `frontend/` directory:

**.env.development**

::

    VITE_API_BASE_URL=http://127.0.0.1:8000/api/
    VITE_ENV=development

**.env.production**

::

    VITE_API_BASE_URL=https://your-production-url/api/
    VITE_ENV=production

Using Variables in Code
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ts

    const api = import.meta.env.VITE_API_BASE_URL;

Available Frontend Configurations
---------------------------------

- **API endpoint URL**
- **Chart.js behavior options**
- **Default UI theme**
- **Default weight profiles for lifestyle preferences**

Example:

.. code-block:: ts

    export const defaultWeights = [5, 4, 3, 2];

-------------------------------------------------------------
Infrastructure Data Configuration
-------------------------------------------------------------

CasaNova requires several datasets to compute infrastructure distances:

- Park locations
- School locations
- Mart locations
- Transportation nodes
- Real estate listings

These files are expected to exist as dataframes or CSV files loaded inside the backend.

Example loading code:

.. code-block:: python

    df_estate = pd.read_csv("data/estate.csv")
    station = pd.read_csv("data/station.csv")

Paths may be customized through:

.. code-block:: python

    DATA_DIRECTORY = "data/"

-------------------------------------------------------------
Loan Product Configuration
-------------------------------------------------------------

CasaNova generates 150 mock loan products automatically:

.. code-block:: python

    loan_products = [
        {"name": f"Dream Home {i}", "rate": 0.03 + 0.0001 * i}
        for i in range(1, 151)
    ]

To change:

- Number of products  
- Rate increments  
- Eligibility rules  

Edit the loan generation section in the backend utility file.

-------------------------------------------------------------
User Preference Configuration
-------------------------------------------------------------

Default weighting profile:

::

    weights = [5, 4, 3, 2]  # Park, School, Mart, Transport

Users may adjust these preferences in the frontend UI.
Different default presets can be offered:

- Balanced
- Cost-efficient
- Education-focused
- Nature-focused

-------------------------------------------------------------
Troubleshooting Configuration Issues
-------------------------------------------------------------

- If backend fails to start → Check `.env` variables  
- If frontend cannot reach backend → Check `VITE_API_BASE_URL`  
- If infrastructure scores are missing → Ensure CSV datasets exist  
- If loan results are empty → Verify eligibility requirements and DSR settings  

-------------------------------------------------------------
End of Configuration Guide
-------------------------------------------------------------

