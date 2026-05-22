from __future__ import annotations


FEATURE_COLUMNS = ["spend_per_visit", "account_age_months", "engagement_score"]


def _to_float(row: dict[str, str], column: str) -> float:
    value = row.get(column, "")
    if value == "":
        raise ValueError(f"missing value for {column}")
    return float(value)


def build_feature_row(row: dict[str, str]) -> dict[str, float]:
    total_spend = _to_float(row, "total_spend")
    visits = _to_float(row, "visits")
    days_since_signup = _to_float(row, "days_since_signup")

    spend_per_visit = total_spend / max(visits, 1.0)
    account_age_months = days_since_signup / 30.0
    engagement_score = (visits * 10.0) + min(total_spend / 20.0, 50.0)

    feature_row: dict[str, float] = {
        "spend_per_visit": round(spend_per_visit, 4),
        "account_age_months": round(account_age_months, 4),
        "engagement_score": round(engagement_score, 4),
    }

    if "churned" in row and row["churned"] != "":
        feature_row["churned"] = float(row["churned"])

    return feature_row


def build_feature_table(rows: list[dict[str, str]]) -> list[dict[str, float]]:
    return [build_feature_row(row) for row in rows]
