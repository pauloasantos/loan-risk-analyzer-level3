def categorize_risk(score: float):
    if score < 20:
        return "Low"
    elif score <= 40:
        return "Medium"
    else:
        return "High"