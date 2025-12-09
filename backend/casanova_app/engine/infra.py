# backend/casanova_app/engine/infra.py

from typing import List
import numpy as np
import pandas as pd


def classify_grade(value: float) -> int:
    """
    도보 시간(분)에 따른 점수 매핑.
    """
    if value <= 5:
        return 100
    elif value <= 10:
        return 90
    elif value <= 15:
        return 80
    elif value <= 20:
        return 70
    elif value <= 25:
        return 60
    elif value <= 30:
        return 50
    elif value <= 35:
        return 40
    else:
        return 30


def calculate_infra_score(df: pd.DataFrame, weights: List[int]) -> pd.DataFrame:
    """
    인프라 점수를 가중합으로 계산.
    weights = [Park, School, Mart, Transport]
    """
    w_park, w_school, w_mart, w_transport = weights

    df["Infrastructure Score"] = (
        df["Park Score"] * w_park
        + df["School Score"] * w_school
        + df["Mart Score"] * w_mart
        + df["Transport Score"] * w_transport
    ) / sum(weights)

    return df


def haversine_vec(lat1, lon1, lat2, lon2):
    """
    벡터화된 Haversine 거리 계산 (km 단위).
    lat1, lon1: (n, 1)
    lat2, lon2: (1, m)
    """
    R = 6371  # km
    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)
    a = (
        np.sin(dlat / 2) ** 2
        + np.cos(np.radians(lat1))
        * np.cos(np.radians(lat2))
        * np.sin(dlon / 2) ** 2
    )
    return R * 2 * np.arcsin(np.sqrt(a))


def nearest_infra_vectorized(houses_df: pd.DataFrame, infra_df: pd.DataFrame):
    """
    each house → nearest infra까지 도보 시간(분) 계산.
    전제: houses_df, infra_df 둘 다 'latitude', 'longitude' 컬럼 사용.
    """
    lat1 = houses_df["latitude"].values[:, np.newaxis]
    lon1 = houses_df["longitude"].values[:, np.newaxis]
    lat2 = infra_df["latitude"].values[np.newaxis, :]
    lon2 = infra_df["longitude"].values[np.newaxis, :]

    distances = haversine_vec(lat1, lon1, lat2, lon2)
    min_distances = distances.min(axis=1)

    return np.round(min_distances / 4 * 60, 1)  # 4km/h 보행 기준, 분 단위


def calculate_distance(
    df_estate: pd.DataFrame, infra_df: pd.DataFrame, col_name: str
) -> pd.DataFrame:
    """
    estate df에 인프라까지의 도보 시간(분) 컬럼 추가.
    """
    df_estate[col_name] = nearest_infra_vectorized(df_estate, infra_df)
    return df_estate
