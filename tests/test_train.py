from kalyan_mlops.train import evaluate, predict, train_centroid_classifier


def test_centroid_classifier_predicts_nearest_class():
    rows = [
        {"spend_per_visit": 10, "account_age_months": 1, "engagement_score": 15, "churned": 1},
        {"spend_per_visit": 12, "account_age_months": 2, "engagement_score": 18, "churned": 1},
        {"spend_per_visit": 90, "account_age_months": 12, "engagement_score": 120, "churned": 0},
        {"spend_per_visit": 95, "account_age_months": 13, "engagement_score": 130, "churned": 0},
    ]

    model = train_centroid_classifier(rows)

    assert predict(model, {"spend_per_visit": 11, "account_age_months": 1.5, "engagement_score": 16}) == 1
    assert predict(model, {"spend_per_visit": 92, "account_age_months": 12, "engagement_score": 125}) == 0


def test_evaluate_returns_accuracy():
    rows = [
        {"spend_per_visit": 10, "account_age_months": 1, "engagement_score": 15, "churned": 1},
        {"spend_per_visit": 90, "account_age_months": 12, "engagement_score": 120, "churned": 0},
    ]
    model = {"0": {"spend_per_visit": 90, "account_age_months": 12, "engagement_score": 120}, "1": {"spend_per_visit": 10, "account_age_months": 1, "engagement_score": 15}}

    metrics = evaluate(model, rows)

    assert metrics["accuracy"] == 1
    assert metrics["examples"] == 2
