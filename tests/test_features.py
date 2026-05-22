from kalyan_mlops.features import build_feature_row, build_feature_table


def test_build_feature_row_creates_expected_columns():
    row = {
        "customer_id": "C100",
        "total_spend": "300",
        "visits": "6",
        "days_since_signup": "90",
        "churned": "0",
    }

    features = build_feature_row(row)

    assert features["spend_per_visit"] == 50
    assert features["account_age_months"] == 3
    assert features["engagement_score"] == 75
    assert features["churned"] == 0


def test_build_feature_table_keeps_row_count():
    rows = [
        {"total_spend": "100", "visits": "2", "days_since_signup": "30", "churned": "1"},
        {"total_spend": "500", "visits": "10", "days_since_signup": "300", "churned": "0"},
    ]

    assert len(build_feature_table(rows)) == 2
