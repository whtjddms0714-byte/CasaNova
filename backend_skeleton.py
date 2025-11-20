import pandas as pd
import math

# -------------------------------
# User Information
# -------------------------------
user_info = {
    "income_monthly": 2500000,   # Monthly income
    "asset": 30000000,           # Savings / capital
    "existing_debt": 0,          # Existing debt
    "dsr_ratio": 0.4,            # DSR (Debt Service Ratio)
    "weights": [5, 4, 3, 2],     # Park / School / Mart / Transport weights
}

# -------------------------------
# Loan Product Data
# -------------------------------
loan_products = [
    {"name": "Dream Home", "rate": 0.034, "years": 30},
    {"name": "Future Plan", "rate": 0.028, "years": 20},
    {"name": "Zero Start", "rate": 0.030, "years": 25},
]

# -------------------------------
# Loan Calculation
# -------------------------------
def calculate_max_loan(user, loan):
    available_monthly = user["income_monthly"] * user["dsr_ratio"] - user.get("existing_debt", 0) / 12
    if available_monthly <= 0:
        return 0
    r = loan["rate"] / 12
    n = loan["years"] * 12
    return int(available_monthly * (1 - (1 + r) ** (-n)) / r)

def recommend_loans(user, loan_list):
    return [{"name": loan["name"], "max_loan": calculate_max_loan(user, loan)} for loan in loan_list]

# -------------------------------
# Infrastructure Score Calculation
# -------------------------------
def classify_grade(value):
    if value <= 5: return 100
    elif value <= 7: return 90
    elif value <= 10: return 80
    elif value <= 12: return 70
    elif value <= 15: return 60
    elif value <= 20: return 50
    else: return 30

def calculate_infra_score(df, weights):
    df['Transport Score'] = df['Transport (min)'].apply(classify_grade)
    df['Park Score'] = df['Park (min)'].apply(classify_grade)
    df['Mart Score'] = df['Mart (min)'].apply(classify_grade)
    df['School Score'] = df['School (min)'].apply(classify_grade)

    df['Infrastructure Score'] = (
        df['Park Score'] * weights[0] +
        df['School Score'] * weights[1] +
        df['Mart Score'] * weights[2] +
        df['Transport Score'] * weights[3]
    ) / sum(weights)

    return df

# -------------------------------
# Distance Calculation (Haversine + Walking Time)
# -------------------------------
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = math.sin(d_lat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(d_lon/2)**2
    return R * (2 * math.asin(math.sqrt(a)))

def walking_minutes(distance_km):
    return round((distance_km / 4) * 60, 1)

def calculate_distance(df_estate, infra_df, col_name):
    distances = []
    for _, house in df_estate.iterrows():
        h_lat, h_lon = house['Latitude'], house['Longitude']
        min_dist = float('inf')
        for _, infra in infra_df.iterrows():
            dist = haversine(h_lat, h_lon, infra['Latitude'], infra['Longitude'])
            if dist < min_dist:
                min_dist = dist
        distances.append(walking_minutes(min_dist))
    df_estate[col_name] = distances
    return df_estate

# -------------------------------
# Final Recommendation
# -------------------------------
def recommend_estate(user, loan_amount, df):
    total_budget = user["asset"] + loan_amount
    df = calculate_infra_score(df, user["weights"])
    return df[df['Price'] <= total_budget].sort_values(by='Infrastructure Score', ascending=False)

# -------------------------------
# Main Execution
# -------------------------------
def main():
    loan_pref = input("Do you want a loan? (yes/no): ")
    if loan_pref.lower() == "yes":
        loans = recommend_loans(user_info, loan_products)
        print("\nRecommended Loan Products:")
        for i, loan in enumerate(loans, 1):
            print(f"{i}. {loan['name']} | Max Loan Amount: {loan['max_loan']:,} KRW")
        selected_loan = loans[int(input("Select loan product number: ")) - 1]['max_loan']
    else:
        selected_loan = 0

    df_estate = pd.DataFrame([
        ['Gangnam-gu, Seoul', 'Raemian', 18000 * 10000, 37.4979, 127.0276],
        ['Seocho-gu, Seoul', 'Xi', 25000 * 10000, 37.4836, 127.0324],
        ['Songpa-gu, Seoul', 'Hillstate', 15000 * 10000, 37.5145, 127.1059]
    ], columns=['Address', 'Building', 'Price', 'Latitude', 'Longitude'])

    df_park = pd.DataFrame([
        ['Gangnam Park', 37.4988, 127.0300],
        ['Yeoksam Culture Park', 37.5005, 127.0362],
        ['Dogok Park', 37.4908, 127.0435],
        ['Seolleung Park', 37.5054, 127.0490]
    ], columns=['Name', 'Latitude', 'Longitude'])

    df_school = pd.DataFrame([
        ['Gangnam Elementary School', 37.4995, 127.0280],
        ['Onju Middle School', 37.5109, 127.0332],
        ['Yeoksam High School', 37.5053, 127.0460],
        ['Gaepo High School', 37.4869, 127.0698]
    ], columns=['Name', 'Latitude', 'Longitude'])

    df_mart = pd.DataFrame([
        ['E-Mart Yeoksam', 37.4965, 127.0258],
        ['Lotte Mart Dogok', 37.4910, 127.0514],
        ['Homeplus Gangnam', 37.5055, 127.0240],
        ['GS Supermarket Gangnam', 37.5011, 127.0350]
    ], columns=['Name', 'Latitude', 'Longitude'])

    df_station = pd.DataFrame([
        ['Gangnam Station', 37.4972, 127.0279],
        ['Yeoksam Station', 37.5006, 127.0365],
        ['Seolleung Station', 37.5045, 127.0486],
        ['Samseong Station', 37.5080, 127.0631]
    ], columns=['Name', 'Latitude', 'Longitude'])

    df_estate = calculate_distance(df_estate, df_station, "Transport (min)")
    df_estate = calculate_distance(df_estate, df_park, "Park (min)")
    df_estate = calculate_distance(df_estate, df_mart, "Mart (min)")
    df_estate = calculate_distance(df_estate, df_school, "School (min)")

    recommended = recommend_estate(user_info, selected_loan, df_estate)
    print("\nRecommended Properties Within Budget:")
    print(recommended[['Address', 'Building', 'Price', 'Infrastructure Score']].to_string(index=False) if not recommended.empty else "No properties found within your budget.")

if __name__ == "__main__":
    main()
