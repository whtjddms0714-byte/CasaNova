Release Notes
=============

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

This is the first public release of CasaNova, a financial-based housing recommendation system that uses real-world loan data rather than mock datasets
 designed to support young adults in determining
realistic housing budgets and making informed property decisions.

Key Features
------------

**1. Financial Simulation Engine**
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

Enhancements
------------

- Clean modular code structure for simulation, scoring, and recommendation  
- Improved readability with refactored functions  
- Dataset handling separated into well-defined preprocessing steps  

Bug Fixes
---------

- Fixed rounding behavior in loan calculations  
- Corrected distance normalization for infrastructure walking-time simulation  
- Resolved data type mismatch in eligibility checks  

Known Issues
------------

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

------------------------------------------------------------
End of Release Notes
------------------------------------------------------------
