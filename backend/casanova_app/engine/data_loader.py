# backend/casanova_app/engine/data_loader.py

from pathlib import Path
from typing import Tuple, Dict, List
import pandas as pd


# 프로젝트 기준 경로 (backend/ 기준으로 조정 필요하면 여기만 수정)
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"


def load_loan_products() -> List[dict]:

    loan_products = [
        {
            "name": f"Dream Home {i}",
            "rate": round(0.045 + 0.0001 * i, 3),  # 금리 시작값 4.5%
            "years": 20,                            # 상환기간 20년
            # 상환기간(년)

            # 우대조건 (영어 설명)
            "benefit_condition":
                "Newlywed rate discount +0.1%" if i % 5 == 0 else \
                "Young adult benefit"          if i % 5 == 1 else \
                "Low-income benefit"           if i % 5 == 2 else \
                "Multi-child family benefit"   if i % 5 == 3 else \
                "Long-term employee benefit",

            # 자격조건 (월소득 / 신용점수)
            "min_income": 1_500_000 + (i % 10) * 100_000,  # required monthly income (원)
            "min_credit": 650 + (i % 20),                  # minimum credit score
        }
        for i in range(1, 151)
    ]

    return loan_products


def load_estate_and_infra() -> Tuple[pd.DataFrame, Dict[str, pd.DataFrame]]:

    houses = pd.read_csv(DATA_DIR / "estate.csv")
    station = pd.read_csv(DATA_DIR / "station.csv")
    park = pd.read_csv(DATA_DIR / "park.csv")
    mart = pd.read_csv(DATA_DIR / "mart.csv")
    school = pd.read_csv(DATA_DIR / "school.csv")

    infra_dfs = {
        "station": station,
        "park": park,
        "mart": mart,
        "school": school,
    }
    return houses, infra_dfs
