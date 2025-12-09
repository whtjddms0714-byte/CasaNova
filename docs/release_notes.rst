<<<<<<< HEAD
# 릴리즈 노트Release Notes
=============

<<<<<<< Updated upstream
버전별 변경사항, 기능 추가, 버그 수정 내역 등.
=======
=======
Release Notes
=============

>>>>>>> 99cfac16b797d7549dabf44f88a13845caa126e3
This document lists version history, new features, improvements, and bug fixes
for the CasaNova project. The project is currently in its early development
phase, and the following notes reflect the initial release milestones.

------------------------------------------------------------
Version 0.1.0 (Initial Release)
------------------------------------------------------------

Release Date: 2025-01-01  
Status: Active Development

Overview
--------

<<<<<<< HEAD
This is the first public release of CasaNova, a financial-based housing
recommendation system designed to support young adults in determining
=======
This is the first public release of CasaNova, a financial-based housing recommendation system that uses real-world loan data rather than mock datasets
 designed to support young adults in determining
>>>>>>> 99cfac16b797d7549dabf44f88a13845caa126e3
realistic housing budgets and making informed property decisions.

Key Features
------------

**1. Financial Simulation Engine**
<<<<<<< HEAD

- Implementation of a PMT-based loan calculation model  
- DSR-based repayment capacity estimation  
- Loan eligibility checks using income, credit score, and preferential conditions  
- Ranking logic for multiple loan products  

**2. Budget Calculation Module**

- Total housing budget computed as:  

  ``asset + selected_loan_amount``  

- Integration with user-defined financial profiles  
- Support for optional budget caps (in units of 10,000 KRW)

**3. Infrastructure Scoring Engine**

- Vectorized Haversine distance computation  
- Scoring for: park, school, mart, transport accessibility  
- Weighted scoring system configurable by the user  

**4. Property Recommendation Engine**

- Budget-based filtering  
- Infrastructure score ranking  
- Support for CSV-based property datasets and vectorized NumPy operations  

**5. Web-Based Workflow**

- Three-step process:

  - user profile input,
  - loan recommendation and selection,
  - property recommendation and display.

- Jekyll-based static pages integrated with Django APIs  

**6. Project Documentation Structure**

- ReadTheDocs documentation setup  
- Pages for technical overview, API reference, configuration, and contribution guidelines  
=======
- Implementation of PMT-based loan calculation model  
- DSR-based repayment capability estimation  
- Loan eligibility checks using income, credit score, and preferential conditions  
- Integration of real financial loan products loaded from verified datasets or public APIs  

**2. Budget Calculation Module**
- Total housing budget computed as:  
  ``asset + max_loan``  
- Integration with user-defined financial profiles  
- Final budget visualization support (Chart.js placeholder)

**3. Infrastructure Scoring Engine**
- Vectorized Haversine distance computation  
- Scoring for: Park, School, Mart, Transport accessibility  
- Weighted scoring system customizable by the user  

**4. Property Recommendation Engine**
- Budget filtering  
- Infrastructure score ranking  
- Supports large datasets through NumPy vectorization  

**5. CLI Interaction Mode**
- Basic `main()` function for local testing  
- Step-by-step loan and property recommendation process  

**6. Project Documentation Structure**
- Complete ReadTheDocs documentation setup  
- Pages include technical overview, API reference, configuration, and contribution guide  
>>>>>>> 99cfac16b797d7549dabf44f88a13845caa126e3

Enhancements
------------

<<<<<<< HEAD
- Clean modular engine structure separating finance, infra, and pipeline logic  
- Separation of concerns between Django views and engine modules  
- Centralized dataset loading through a dedicated data loader  
=======
- Clean modular code structure for simulation, scoring, and recommendation  
- Improved readability with refactored functions  
- Dataset handling separated into well-defined preprocessing steps  
>>>>>>> 99cfac16b797d7549dabf44f88a13845caa126e3

Bug Fixes
---------

<<<<<<< HEAD
- Adjusted rounding behavior in loan calculations  
- Corrected distance normalization for walking-time estimation  
- Resolved data type mismatches in eligibility checks  
=======
- Fixed rounding behavior in loan calculations  
- Corrected distance normalization for infrastructure walking-time simulation  
- Resolved data type mismatch in eligibility checks  
>>>>>>> 99cfac16b797d7549dabf44f88a13845caa126e3

Known Issues
------------

<<<<<<< HEAD
- No persistent user account system implemented  
- No production-grade authentication or authorization  
- Datasets must be manually managed in the ``data/`` directory  
- Frontend is a minimal reference implementation without advanced UI/UX features  

Roadmap (Planned for Future Releases)
-------------------------------------

**Version 0.2.0**

- Full Django REST API structure with serializers and viewsets  
- Additional endpoints for configuration and introspection  
- Extended frontend integration with richer visualizations  

**Version 0.3.0**

- User authentication (e.g. JWT or session-based)  
- Saved searches and preference profiles  
- Improved recommendation result visualization  

**Version 0.4.0**

- Integration with larger and richer real estate datasets  
- Enhanced scoring models and optional machine learning support  

**Version 1.0.0**

- Production-ready release  
- Deployment guides and best practices  
- Performance tuning and horizontal scalability considerations  
=======
- No real API endpoints implemented yet (Django integration planned)  
- Dataset files must be manually placed in `data/` directory  
- Some CLI prompts need validation logic  
- Infrastructure scoring weight adjustment UI not yet implemented in frontend  

------------------------------------------------------------
Roadmap (Planned for Future Releases)
------------------------------------------------------------

**Version 0.2.0**
- Full Django REST API implementation  
- Endpoints for loan simulation, property scoring, and recommendation  
- Basic frontend integration with live API calls  

**Version 0.3.0**
- User authentication (JWT)  
- Saved searches and user preference profiles  
- UI/UX improvements for recommendation visualization  

**Version 0.4.0**
- Real estate dataset integration (actual market property listings)  
- Machine learning–based preference prediction models  

**Version 1.0.0**
- Production-ready release  
- Full deployment documentation  
- Performance tuning and scalable hosting model  
>>>>>>> 99cfac16b797d7549dabf44f88a13845caa126e3

------------------------------------------------------------
End of Release Notes
------------------------------------------------------------
<<<<<<< HEAD
>>>>>>> Stashed changes
=======
>>>>>>> 99cfac16b797d7549dabf44f88a13845caa126e3
