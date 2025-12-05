Maintenance and Troubleshooting
===============================

This guide provides routine maintenance procedures and solutions to common issues
encountered while running or developing the CasaNova system.

CasaNova consists of both backend and frontend services, as well as multiple datasets.
Proper maintenance ensures reliable performance and stable recommendation results.

------------------------------------------------------------
Routine Maintenance Tasks
------------------------------------------------------------

Database Management
-------------------

1. **Run migrations when models change**

.. code-block:: bash

    python manage.py makemigrations
    python manage.py migrate

2. **Backup the database regularly**

Schedule automatic database dumps (MySQL example):

.. code-block:: bash

    mysqldump -u root -p casanova > backup.sql

3. **Monitor DB size and indexing**

Large datasets (real estate or infrastructure data) may require indexing to maintain performance.

Log File Maintenance
--------------------

CasaNova may generate log files such as:

- API request logs  
- Error logs  
- Performance metrics  

Perform:

- Weekly rotation  
- Archiving of old logs  
- Optional upload to a monitoring system such as ELK or CloudWatch  

Dataset Updates
----------------

Infrastructure datasets (parks, marts, schools, stations) and
real estate property listings should be updated periodically.

Recommended procedure:

1. Place new CSV files in the `data/` directory  
2. Validate schema consistency  
3. Run preprocessing scripts (if applicable)  
4. Restart backend services  

Dependency Maintenance
----------------------

Updating dependencies ensures security and compatibility.

Backend:

.. code-block:: bash

    pip list --outdated
    pip install --upgrade <package>

Frontend:

.. code-block:: bash

    npm outdated
    npm update

------------------------------------------------------------
Common Issues and Solutions
------------------------------------------------------------

Backend Fails to Start
----------------------

**Cause 1:** Missing or incorrect `.env` values  
**Solution:** Ensure required environment variables are set:

::

    DJANGO_SECRET_KEY, DB_NAME, DB_USER, DB_PASSWORD, DB_HOST

**Cause 2:** Database not running  
**Solution:** Start MySQL server and verify connection:

.. code-block:: bash

    mysql -u root -p -h 127.0.0.1 -P 3306

**Cause 3:** Migration conflicts  
**Solution:**

.. code-block:: bash

    rm -rf migrations/*
    python manage.py makemigrations
    python manage.py migrate

Frontend Cannot Connect to Backend
----------------------------------

**Cause:** Incorrect API base URL in `.env`  
**Solution:** Confirm:

::

    VITE_API_BASE_URL=http://127.0.0.1:8000/api/

Then rebuild frontend:

.. code-block:: bash

    npm run dev

Loan Recommendation Returns Empty Results
-----------------------------------------

Possible causes:

1. User does not meet minimum income or credit requirements  
2. DSR ratio too low  
3. Incorrect loan preference flags  

**Solution:**

- Validate user data  
- Print intermediate values for debugging  
- Adjust DSR ratio if necessary  

Property Recommendation List Is Empty
-------------------------------------

**Cause 1:** No properties fall within the computed budget  
**Solution:** Increase asset value or loan limit for testing

**Cause 2:** Missing dataset columns  
**Solution:** Ensure required columns exist:

::

    ['위도', '경도', '물건금액(만원)', '주소', '건물명']

**Cause 3:** Infrastructure distance functions failed  
**Solution:** Test distance functions independently:

.. code-block:: python

    haversine_vec(lat1, lon1, lat2, lon2)

Performance Issues
------------------

**Symptom:** Slow response during recommendation calculations  
**Cause:** Large dataset size or unoptimized vectorized functions  
**Solutions:**

1. Use NumPy vectorized operations  
2. Pre-cache distance matrices  
3. Apply indexing on frequently queried columns  

------------------------------------------------------------
Service Monitoring Tips
------------------------------------------------------------

- Track API response times  
- Monitor server CPU/memory usage  
- Log frequency of loan and property recommendation requests  
- Validate dataset accuracy after updates  

------------------------------------------------------------
Disaster Recovery
------------------------------------------------------------

In the event of system failure:

1. Restore database from latest dump  
2. Reinstall dependencies using `requirements.txt` and `package.json`  
3. Rebuild frontend assets  
4. Run Django migrations  
5. Test core API endpoints before going live  

------------------------------------------------------------
End of Maintenance & Troubleshooting Guide
------------------------------------------------------------
