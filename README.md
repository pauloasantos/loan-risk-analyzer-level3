# Loan Portfolio Risk Analyzer

This project is a Streamlit dashboard for evaluating the risk of loan applicants (individuals and businesses) in a banking context. It uses Python, pandas, and Streamlit, and is fully modular.

## Features

- Upload applicant data via CSV
- Add applicants manually via sidebar form
- Automatic risk score calculation and categorization
- Portfolio-level statistics and summary
- Interactive filtering and charts

## Setup

1. **Clone or download the repository.**

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Theme configuration:**
   The dark theme is set in `.streamlit/config.toml`:
   ```
   [theme]
   base="dark"
   ```

## Usage

1. **Start the app:**
   ```
   streamlit run app.py
   ```

2. **Open the dashboard:**
   The app will open automatically in your browser, or visit [http://localhost:8501](http://localhost:8501).

3. **Upload Data:**
   - Use the sidebar to upload a CSV file with columns: `id`, `income`, `loan_amount`, `credit_score`, `age`, and optionally `revenue`.
   - Or use the sidebar form to add applicants manually.

4. **Explore Tabs:**
   - **Data Overview:** See all input data.
   - **Risk Analysis:** Filter applicants by risk category and view charts.
   - **Summary:** View portfolio statistics and metrics.

## File Structure

```
loan_risk_analyzer/
├── app.py
├── client.py
├── portfolio_analyzer.py
├── risk_tools.py
├── requirements.txt
└── .streamlit/
    └── config.toml
```

## Requirements

- Python 3.8+
- Streamlit
- pandas

## License

MIT License