import os
import sys
import pytest
import pandas as pd
import joblib

sys.path.append(r"C:\UnityProjects\FYP\GameWebAPI")

from app.ml.Analytics.preprocessing.Preprocess_TurnSnapshots import (
    preprocess_turn_snapshot_regression,
    preprocess_turn_snapshot_cluster,
)

CSV_PATH = r"C:\UnityProjects\FYP\GameWebAPI\app\ml\Analytics\Data\TurnSnapShots\turn_snapshots_20260406_192845.csv"

REGRESSION_MODEL_DIR = r"C:\UnityProjects\FYP\GameWebAPI\app\ml\TrainedModels\Regression"
CLUSTERING_MODEL_DIR = r"C:\UnityProjects\FYP\GameWebAPI\app\ml\TrainedModels\Clustering"


def test_ml_pipeline_regression_and_clustering():
    # ===== LOAD CSV =====
    df = pd.read_csv(CSV_PATH)

    # ===== FILTER TURNS ≤ 16 =====
    turn_col = "Turn" if "Turn" in df.columns else "turn"
    df = df[df[turn_col] <= 16].copy()

       # ===== AVG FINAL POPULATION =====
    PREPROCESSED_PATH = (
        r"C:\UnityProjects\FYP\GameWebAPI\app\ml\Analytics\Preprocessed\session_features.csv"
    )

    preprocessed_df = pd.read_csv(PREPROCESSED_PATH)

    avg_final_population = float(
        preprocessed_df["final_population"].mean()
    )

    print("\nAverage Final Population:", avg_final_population)

    assert avg_final_population == pytest.approx(2977, rel=1e-3)

    # ===== REGRESSION PIPELINE =====
    lr_model = joblib.load(os.path.join(REGRESSION_MODEL_DIR, "lr_model.pkl"))
    lr_scaler = joblib.load(os.path.join(REGRESSION_MODEL_DIR, "lr_scaler.pkl"))
    lr_feature_cols = joblib.load(os.path.join(REGRESSION_MODEL_DIR, "lr_feature_cols.pkl"))

    regression_features = preprocess_turn_snapshot_regression(df)

    assert regression_features is not None, "Regression preprocessing returned None"

    X_reg = pd.DataFrame([regression_features])[lr_feature_cols]
    X_reg_scaled = lr_scaler.transform(X_reg)

    predicted_population = float(
        lr_model.predict(X_reg_scaled)[0]
    )

    print("\nPredicted Final Population:", predicted_population)

    assert predicted_population == pytest.approx(
        2767.605216,
        rel=1e-5
    )

    # ===== CLUSTERING PIPELINE =====
    kmeans_model = joblib.load(os.path.join(CLUSTERING_MODEL_DIR, "kmeans_model.pkl"))
    kmeans_scaler = joblib.load(os.path.join(CLUSTERING_MODEL_DIR, "scaler.pkl"))
    kmeans_feature_cols = joblib.load(os.path.join(CLUSTERING_MODEL_DIR, "feature_cols.pkl"))

    cluster_features = preprocess_turn_snapshot_cluster(df)

    assert cluster_features is not None, "Cluster preprocessing returned None"

    X_cluster = pd.DataFrame([cluster_features])[kmeans_feature_cols]
    X_cluster_scaled = kmeans_scaler.transform(X_cluster)
    cluster_id = int(kmeans_model.predict(X_cluster_scaled)[0])

    print("\nPredicted Cluster ID:", cluster_id)

    assert cluster_id == 0