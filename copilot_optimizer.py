import pandas as pd
from sklearn.metrics import accuracy_score

def analyze_copilot_productivity(baseline_df, copilot_df):
    score = accuracy_score(baseline_df['completion'], copilot_df['completion'])
    print(f"Copilot alignment score: {score}")
    return score