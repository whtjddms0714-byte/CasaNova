# Backend Skeleton for Real Estate Recommendation Project

import pandas as pd

# 1. User Information Structure (Example)
user_info = {
    "income_monthly": None,  # Monthly income (KRW)
    "asset": None,           # Deposited asset (KRW)
    "existing_debt": None,   # Existing debt (KRW)
    "dsr_ratio": 0.4,        # Fixed DSR ratio for mortgage loan
    "weights": [5, 4, 3, 2], # Park / School / Market / Transport weights
}

# 2. Loan Product Structure (Example format)
loan_products = [
    {"name": "", "rate": None, "years": None}
]


# 3. Loan Calculation (PMT)
def calculate_max_loan(user, loan):
    """
    Calculate maximum available loan using the PMT formula.
    
    Expected:
    - Use income, existing debt, and dsr_ratio to find available monthly payment.
    - Calculate PMT to determine max loan based on interest rate and period.
    """
    pass  # TODO: Implement PMT calculation logic


# 4. Loan Recommendation
def recommend_loans(user, loan_list):
    """
    Recommend loan products based on max loan calculation.
    
    Expected:
    - Iterate loan list
    - For each loan, calculate max loan
    - Return list of recommendations
    """
    pass  # TODO: Implement loan recommendation logic


# 5. Infrastructure Scoring
def calculate_infra_score(df, weights):
    """
    Calculate weighted infrastructure score.
    
    Expected:
    - Apply scoring rules based on distance (classify_grade)
    - Calculate weighted total score
    """
    pass  # TODO: Implement infra score logic


# 6. Real Estate Recommendation
def recommend_estate(user, loan_amount, df):
    """
    Recommend properties within available budget.
    
    Expected:
    - Budget = asset + loan
    - Filter properties by budget
    - Sort by infrastructure score
    """
    pass  # TODO: Implement property recommendation logic


# 7. Entry Point (Temporary)
def main():
    """Temporary main function for skeleton verification."""
    print("Backend skeleton loaded. Implementation pending.")


if __name__ == "__main__":
    main()
