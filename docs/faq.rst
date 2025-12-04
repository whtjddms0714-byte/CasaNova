.. _faq:

Frequently Asked Questions (FAQ)
================================

Q: Are the DSR/Loan Simulation results guaranteed to be accurate by real banks?
---------------------------------------------------------------------------------

A: **No, they are not guaranteed to be exact.** CasaNova uses a **mock dataset** of loan products and applies the standard **Present Value (PMT)** formula to estimate the maximum loan amount. While the simulation results are designed to be **highly similar** to typical banking results, they are for **pre-budget determination and planning purposes only.** You should always consult with a financial institution for final, legally binding loan quotes.

Q: Where does the property and infrastructure data come from?
------------------------------------------------------

A: All data currently used by the CasaNova application is sourced from open public APIs for demonstration and educational purposes. The data sources are as follows:

- [cite_start]**Property Listings (Price & Coordinates):** Sourced from the **Seoul Real Estate API** [cite: 1] (Data Source: Seoul Open Data Plaza).
- [cite_start]**School Data:** Derived from the **National Elementary and Secondary School Data (Seoul Extraction)** [cite: 2] (Data Source: Data.go.kr).
- [cite_start]**Park Data:** Sourced from the **Seoul Public Park Information** [cite: 3] (Data Source: Seoul Open Data Plaza).
- [cite_start]**Mart Data:** Sourced from the **Seoul Large Mart Store Information** [cite: 4] (Data Source: Seoul Open Data Plaza).
- [cite_start]**Public Transport (Subway):** Sourced from the **Seoul Subway Station Information** [cite: 5] (Data Source: Seoul Open Data Plaza).
- **Loan Products:** Currently using a **Mock Data Set** based on generalized market interest rates for simulation.

Q: Can I change the importance of parks, schools, or public transport?
--------------------------------------------------------------------------

A: **Yes.** CasaNova's **Lifestyle Matching Engine** is designed to be highly customizable. During the second step of the process, you can **manually set the priority/weight** for each key infrastructure element (Park, School, Mart, Public Transport). This personalization ensures the final property recommendations accurately reflect your unique lifestyle needs.
