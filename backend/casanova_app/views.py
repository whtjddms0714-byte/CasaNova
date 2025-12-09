import json
import pandas as pd
import numpy as np  # NaN -> None 치환용

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .engine.data_loader import load_loan_products, load_estate_and_infra
from .engine.pipeline import recommend_estate
from .engine.finance import recommend_loans
from .engine.infra import calculate_distance, classify_grade


@csrf_exempt
def recommend_loans_view(request):
    """
    대출 추천 API
    URL: /api/recommend-loans/
    메서드: POST
    """
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    try:
        body = json.loads(request.body.decode("utf-8"))
        user_info = body.get("user_info")
        if not user_info:
            return JsonResponse({"error": "user_info required"}, status=400)

        loan_products = load_loan_products()
        loan_results = recommend_loans(user_info, loan_products)

        loans = [
            {
                "name": name,
                "score": score,
                "max_loan": max_loan,
            }
            for (name, score, max_loan) in loan_results
        ]

        return JsonResponse(
            {"loan_recommendations": loans},
            json_dumps_params={"ensure_ascii": False},
        )

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def recommend_properties_view(request):
    """
    부동산 추천 API
    URL: /api/recommend-properties/
    메서드: POST
    """
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    try:
        # 1) 요청 JSON 파싱
        body = json.loads(request.body.decode("utf-8"))
        user_info = body.get("user_info")
        selected_loan_amount = body.get("selected_loan_amount")

        if not user_info:
            return JsonResponse({"error": "user_info required"}, status=400)
        if selected_loan_amount is None:
            return JsonResponse({"error": "selected_loan_amount required"}, status=400)

        # 2) 부동산 + 인프라 데이터 로드
        df_estate, infra_dfs = load_estate_and_infra()
        df = df_estate.copy()

        # 3) 인프라까지 거리(min) 계산
        df = calculate_distance(df, infra_dfs["station"], "Transport (min)")
        df = calculate_distance(df, infra_dfs["park"], "Park (min)")
        df = calculate_distance(df, infra_dfs["mart"], "Mart (min)")
        df = calculate_distance(df, infra_dfs["school"], "School (min)")
                # 🔧 마트/공원 거리 NaN이면 기본값(60분)으로 채우기
        #    → 최소한 UI에서는 숫자가 보이게 하기 위함
        for col in ["Mart (min)"]:
            if col in df.columns:
                df[col] = df[col].fillna(60)

        # 4) 거리 -> 점수 매핑
        df["Transport Score"] = df["Transport (min)"].apply(classify_grade)
        df["Park Score"] = df["Park (min)"].apply(classify_grade)
        df["School Score"] = df["School (min)"].apply(classify_grade)
        df["Mart Score"] = df["Mart (min)"].apply(classify_grade)

        # 5) 추천 로직 실행 (예산/지역/인프라 점수 반영)
        recommended = recommend_estate(user_info, selected_loan_amount, df)

        # NaN -> None (1차)
        recommended = recommended.astype(object).where(
            pd.notnull(recommended),
            None,
        )

        # 결과 없음 처리
        if recommended.empty:
            return JsonResponse(
                {
                    "message": "No suitable properties were found. Please adjust your budget or location."
                },
                json_dumps_params={"ensure_ascii": False},
            )

        # 6) 프론트에서 쓰는 필드 이름으로 거리 컬럼 rename
        recommended = recommended.rename(
            columns={
                "School (min)": "school_distance_min",
                "Mart (min)": "mart_distance_min",
                "Transport (min)": "transport_distance_min",
                "Park (min)": "park_distance_min",
            }
        )

        # 혹시 남아 있을 NaN → None 한 번 더
        recommended = recommended.replace({np.nan: None})

        # 7) 프론트에서 실제로 쓰는 필드만 JSON으로 변환
        properties = recommended[
            [
                "address",
                "building_name",
                "price_10k",
                "Infrastructure Score",
                "school_distance_min",
                "mart_distance_min",
                "transport_distance_min",
                "park_distance_min",
            ]
        ].to_dict(orient="records")

        return JsonResponse(
            {"message": "success", "properties": properties},
            json_dumps_params={"ensure_ascii": False},
        )

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
