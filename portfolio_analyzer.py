import pandas as pd
from client import LoanApplicant, BusinessApplicant
from risk_tools import categorize_risk

class PortfolioAnalyzer:
    def __init__(self, applicants):
        self.applicants = applicants

    @staticmethod
    def make_applicant(row):
        revenue = row.get("revenue", None)
        if revenue not in [None, ""] and not pd.isna(revenue):
            return BusinessApplicant(
                id=row["id"],
                income=row["income"],
                loan_amount=row["loan_amount"],
                credit_score=row["credit_score"],
                age=row["age"],
                revenue=row["revenue"]
            )
        else:
            return LoanApplicant(
                id=row["id"],
                income=row["income"],
                loan_amount=row["loan_amount"],
                credit_score=row["credit_score"],
                age=row["age"]
            )

    @classmethod
    def from_dicts(cls, rows):
        applicants = [cls.make_applicant(row) for row in rows]
        return cls(applicants)

    def summarize(self):
        scores = [a.calculate_risk_score() for a in self.applicants]
        categories = [categorize_risk(s) for s in scores]
        total = len(self.applicants)
        high_risk = sum(1 for c in categories if c == "High")
        average_score = round(sum(scores) / total, 2) if total else 0
        if scores:
            max_score = max(scores)
            idx = scores.index(max_score)
            highest = {
                "id": self.applicants[idx].id,
                "score": round(max_score, 2),
                "category": categories[idx]
            }
        else:
            highest = None

        dist = {"Low": categories.count("Low"), "Medium": categories.count("Medium"), "High": categories.count("High")}
        return {
            "total": total,
            "high_risk": high_risk,
            "average_score": average_score,
            "highest_risk": highest,
            "distribution": dist
        }

    def to_dataframe(self):
        data = []
        for a in self.applicants:
            score = a.calculate_risk_score()
            category = categorize_risk(score)
            row = a.__dict__.copy()
            row["risk_score"] = round(score, 2)
            row["risk_category"] = category
            data.append(row)
        return pd.DataFrame(data)

    def filter_by_category(self, category):
        df = self.to_dataframe()
        if category == "All":
            return df
        return df[df["risk_category"] == category]