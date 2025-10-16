from abc import ABC, abstractmethod

class ApplicantBase(ABC):
    def __init__(self, id: str, income: float, loan_amount: float, credit_score: int, age: int):
        self.id = id
        self.income = income
        self.loan_amount = loan_amount
        self.credit_score = credit_score
        self.age = age

    @abstractmethod
    def calculate_risk_score(self):
        pass

class LoanApplicant(ApplicantBase):
    def calculate_risk_score(self):
        score = (self.loan_amount / self.income) * 100
        if self.credit_score < 600:
            score += 10
        if self.age < 25 or self.age > 60:
            score += 5
        return score

class BusinessApplicant(LoanApplicant):
    def __init__(self, id, income, loan_amount, credit_score, age, revenue: float):
        super().__init__(id, income, loan_amount, credit_score, age)
        self.revenue = revenue

    def calculate_risk_score(self):
        score = (self.loan_amount / (self.income + 0.3 * self.revenue)) * 100
        if self.credit_score < 620:
            score += 8
        return score