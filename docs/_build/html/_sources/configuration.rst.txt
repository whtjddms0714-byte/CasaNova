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
