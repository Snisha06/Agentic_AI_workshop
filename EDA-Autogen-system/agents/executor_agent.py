class ExecutorAgent:
    def validate(self, df, report):
        # Basic validation; in real case, re-run EDA steps
        if df.empty:
            return "Validation failed: dataframe is empty."
        return "Validation okay."
