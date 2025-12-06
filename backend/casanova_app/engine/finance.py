# backend/casanova_app/engine/finance.py

from decimal import Decimal, getcontext
from typing import List, Dict, Tuple

getcontext().prec = 28


def check_preferential(user: Dict, loan: Dict) -> bool:
    """
    Determine whether the user is eligible for any preferential benefit
    defined in loan['benefit_condition'].

    Expected patterns in benefit_condition:
      - "Newlywed"
      - "Young adult"
      - "Low-income"
      - "Multi-child"
      - "Long-term employee"
    """
    cond = (loan.get("benefit_condition") or "").lower()
    income = user.get("income_monthly", 0)

    # Newlywed: married
    if "newlywed" in cond and user.get("married"):
        return True

    # Young adult: we don't have age, so we treat "first_job" as proxy
    if "young adult" in cond and user.get("first_job"):
        return True

    # Low-income: monthly income < 3,000,000
    if "low-income" in cond and income < 3_000_000:
        return True

    # Multi-child: not implemented yet (no children info in user)
    # Long-term employee: also no field yet

    return False



def check_eligibility(user: Dict, loan: Dict) -> bool:
    min_income = loan.get("min_income", 0)
    min_credit = loan.get("min_credit", 0)

    return not (
        user.get("income_monthly", 0) < min_income
        or user.get("credit_score", 0) < min_credit
    )



def calculate_max_loan(user, loan):
    """
    DSR 기준으로 사용자가 감당 가능한 최대 대출금 계산.
    - 기존 월 상환액(existing_debt_monthly_payment) 반영
    - 기존 부채 원금(existing_debt)을 기준으로 추정 월 상환액도 반영
    """

    # 1) 기본 입력값
    income_monthly = Decimal(str(user.get("income_monthly", 0)))
    dsr_ratio = Decimal(str(user.get("dsr_ratio", 0.4)))

    # 사용자가 직접 넣은 기존 월 상환액
    existing_payment_direct = Decimal(str(user.get("existing_debt_monthly_payment", 0)))

    # 기존 부채 원금
    existing_debt = Decimal(str(user.get("existing_debt", 0)))

    # 2) 기존 부채 원금 → 추정 월 상환액으로 환산 (기본: 연 4%, 10년 상환 가정)
    existing_payment_estimated = Decimal("0")
    if existing_debt > 0:
        r_prev = Decimal("0.04") / 12      # 연 4% 금리
        n_prev = Decimal("10") * 12        # 10년(120개월) 가정

        if r_prev == 0:
            existing_payment_estimated = existing_debt / n_prev
        else:
            existing_payment_estimated = (
                existing_debt * r_prev / (1 - (1 + r_prev) ** (-n_prev))
            )

    # 3) 최종 기존 월 상환액: 직접 입력값이 있으면 그걸 우선 사용
    existing_payment = existing_payment_direct if existing_payment_direct > 0 else existing_payment_estimated

    # 4) DSR을 적용한 신규 대출 월 상환 한도
    available_monthly = income_monthly * dsr_ratio - existing_payment
    if available_monthly <= 0:
        return 0

    # 5) 신규 대출 한도 계산 (PMT 역산)
    rate = Decimal(str(loan.get("rate", 0)))
    years = Decimal(str(loan.get("years", 30)))
    r = rate / 12
    n = years * 12

    if r == 0:
        max_loan = available_monthly * n
    else:
        max_loan = available_monthly * (1 - (1 + r) ** (-n)) / r

    return int(max_loan)



def recommend_loans(user: Dict, loan_products: List[Dict]) -> List[Tuple[str, float, int]]:
    """
    반환 형식: [(name, score, max_loan), ...]  ← 반드시 3개짜리 튜플
    """
    recommendations = []

    for loan in loan_products:
        if not check_eligibility(user, loan):
            continue

        max_loan = calculate_max_loan(user, loan)
        if max_loan <= 0:
            continue

        rate = float(loan.get("rate", 0.05))
        score = max_loan / 1e6 + (0.05 - rate) * 100

        if check_preferential(user, loan):
            score += 5

        recommendations.append((loan["name"], float(score), int(max_loan)))

    return sorted(recommendations, key=lambda x: x[1], reverse=True)
