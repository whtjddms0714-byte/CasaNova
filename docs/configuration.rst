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

Database Configuration
----------------------

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

