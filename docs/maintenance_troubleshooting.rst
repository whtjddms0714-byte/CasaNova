Maintenance and Troubleshooting
===============================

This section covers routine maintenance tasks and common issues.

Routine Tasks
-------------

Database Migrations
~~~~~~~~~~~~~~~~~~~

Whenever models or database-related code is updated, apply migrations:

.. code-block:: bash

   python manage.py makemigrations
   python manage.py migrate

Server Management
~~~~~~~~~~~~~~~~~

Start the development server:

.. code-block:: bash

   python manage.py runserver

To run on a specific host/port:

.. code-block:: bash

   python manage.py runserver 0.0.0.0:8000

Dataset Updates
~~~~~~~~~~~~~~~

If property or infrastructure data changes:

1. Replace the relevant CSV files under ``data/``.
2. Ensure the column names and formats are still compatible.
3. Restart the Django server if necessary.

Common Issues
-------------

No Properties Returned
~~~~~~~~~~~~~~~~~~~~~~

Symptom:

- The ``/api/recommend-properties/`` endpoint returns:

  .. code-block:: json

     {
       "message": "No suitable properties were found. Please adjust your budget or location."
     }

Possible causes:

- Budget is too low for available properties.
- ``target_gu`` filter is too restrictive.
- Datasets do not contain properties for the requested region.

Resolution:

- Increase asset amount or selected loan amount.
- Remove or change the ``target_gu``.
- Verify dataset coverage in ``estate.csv``.

Missing user_info or selected_loan_amount
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Symptom:

- API responds with:

  .. code-block:: json

     {
       "error": "user_info required"
     }

or

  .. code-block:: json

     {
       "error": "selected_loan_amount required"
     }

Possible causes:

- Frontend did not send the expected JSON fields.
- ``localStorage`` does not contain user information.

Resolution:

- Ensure that ``index.html`` completes successfully and stores
  ``casanova_user_info``.
- Check the request body in the browser developer tools.

CORS Errors in Browser
~~~~~~~~~~~~~~~~~~~~~~

Symptom:

- Browser console shows CORS-related errors when calling the API.

Resolution:

- Confirm that ``corsheaders`` is installed and configured.
- In development, ensure ``CORS_ALLOW_ALL_ORIGINS = True``.
- In production, configure ``CORS_ALLOWED_ORIGINS`` properly.

CSV Loading Errors
~~~~~~~~~~~~~~~~~~

Symptom:

- Backend returns a 500 error mentioning missing CSV files.

Possible causes:

- ``data/`` directory is missing.
- CSV filenames differ from what ``data_loader.py`` expects.

Resolution:

- Ensure all required CSV files exist in the configured directory.
- Verify paths in ``engine/data_loader.py``.

Performance Considerations
--------------------------

The current implementation uses vectorized NumPy operations for
distance calculations, which should be sufficient for moderate dataset sizes.

For very large datasets, consider:

- precomputing certain scores,
- aggregating data,
- or moving to a database with geospatial support.

Backup and Version Control
--------------------------

- Keep the code and configuration under version control (Git).
- Back up the ``data/`` directory if you maintain custom datasets.
- For production, regularly back up the database.

