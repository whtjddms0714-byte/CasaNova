# 릴리즈 노트Release Notes
=============

<<<<<<< Updated upstream
버전별 변경사항, 기능 추가, 버그 수정 내역 등.
=======
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

This is the first public release of CasaNova, a financial-based housing
recommendation system designed to support young adults in determining
realistic housing budgets and making informed property decisions.

Key Features
------------

**1. Financial Simulation Engine**

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

Enhancements
------------

- Clean modular engine structure separating finance, infra, and pipeline logic  
- Separation of concerns between Django views and engine modules  
- Centralized dataset loading through a dedicated data loader  

Bug Fixes
---------

- Adjusted rounding behavior in loan calculations  
- Corrected distance normalization for walking-time estimation  
- Resolved data type mismatches in eligibility checks  

Known Issues
------------

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

------------------------------------------------------------
End of Release Notes
------------------------------------------------------------
>>>>>>> Stashed changes
