import json
import pandas as pd

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # ← 이 줄이 반드시 있어야 함!

from .engine.data_loader import load_loan_products, load_estate_and_infra
from .engine.pipeline import recommend_estate
from .engine.finance import recommend_loans
from .engine.infra import calculate_distance, classify_grade

@csrf_exempt
def recommend_loans_view(request):
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
                "max_loan": max_loan
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
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    try:
        body = json.loads(request.body.decode("utf-8"))
        user_info = body.get("user_info")
        selected_loan_amount = body.get("selected_loan_amount")

        if not user_info:
            return JsonResponse({"error": "user_info required"}, status=400)
        if selected_loan_amount is None:
            return JsonResponse({"error": "selected_loan_amount required"}, status=400)

        df_estate, infra_dfs = load_estate_and_infra()

        # -----------------------------
        # 1) Distance calculation
        # -----------------------------
        df = df_estate.copy()
        df = calculate_distance(df, infra_dfs["station"], "Transport (min)")
        df = calculate_distance(df, infra_dfs["park"], "Park (min)")
        df = calculate_distance(df, infra_dfs["mart"], "Mart (min)")
        df = calculate_distance(df, infra_dfs["school"], "School (min)")

        # -----------------------------
        # 2) Score mapping
        # -----------------------------
        df["Transport Score"] = df["Transport (min)"].apply(classify_grade)
        df["Park Score"] = df["Park (min)"].apply(classify_grade)
        df["School Score"] = df["School (min)"].apply(classify_grade)
        df["Mart Score"] = df["Mart (min)"].apply(classify_grade)

        # -----------------------------
        # 3) Recommend properties
        # -----------------------------
        recommended = recommend_estate(user_info, selected_loan_amount, df)
        recommended = recommended.where(pd.notnull(recommended), None)

        # -----------------------------
        # 🔥 4) No result → return message
        # -----------------------------
        if recommended.empty:
            return JsonResponse(
                {
                    "message": "No suitable properties were found. Please adjust your budget or location."
                },
                json_dumps_params={"ensure_ascii": False},
            )

        # -----------------------------
        # 5) Normal result
        # -----------------------------
        properties = recommended[
            ["address", "building_name", "price_10k", "Infrastructure Score"]
        ].to_dict(orient="records")

        return JsonResponse(
            {
                "message": "success",
                "properties": properties
            },
            json_dumps_params={"ensure_ascii": False},
        )

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
