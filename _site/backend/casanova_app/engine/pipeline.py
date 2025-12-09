# backend/casanova_app/engine/pipeline.py

from typing import Dict, Any, List
import pandas as pd

from .finance import recommend_loans
from .infra import (
    calculate_distance,
    classify_grade,
    calculate_infra_score,
)


def recommend_estate(user, loan_amount, df):
    """
    대출 한도 + 자산 + 예산 상한 + 지역 필터에 따라 부동산 추천.
    address 문자열 안에서 '강남구', '송파구' 등 구 이름을 직접 검색하여 필터링.
    """

    # -----------------------------------
    # 1) 총 예산 계산
    # -----------------------------------
    total_budget_won = user.get("asset", 0) + loan_amount
    total_budget_10k = total_budget_won / 10_000  # price_10k 기준

    # 예산 상한(budget_limit) 적용
    budget_limit = user.get("budget_limit")
    if budget_limit and budget_limit > 0:
        total_budget_10k = min(total_budget_10k, budget_limit)

    # -----------------------------------
    # 2) 희망 지역 필터링
    # -----------------------------------
    target_gu = (user.get("target_gu") or "").strip()

    if target_gu and "address" in df.columns:
        # address 안에 타겟 구 이름이 포함된 매물만 남김
        df = df[df["address"].astype(str).str.contains(target_gu, na=False)]

    # -----------------------------------
    # 3) 인프라 점수 계산
    # -----------------------------------
    df = calculate_infra_score(df, user.get("weights", [5,4,3,2]))

    # -----------------------------------
    # 4) 예산(만원 단위) 이하의 매물만 필터링
    # -----------------------------------
    df_filtered = df[df["price_10k"] <= total_budget_10k]

    # -----------------------------------
    # 5) 점수 높은 순 정렬하여 반환
    # -----------------------------------
    return df_filtered.sort_values(by="Infrastructure Score", ascending=False)

