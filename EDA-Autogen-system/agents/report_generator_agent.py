class ReportGeneratorAgent:
    def __init__(self):
        self.report = ""

    def create_report(self, stats, plot_b64):
        self.report += "# 🗂️ EDA Report\n\n"
        self.report += "## Summary Statistics\n"
        for col, col_stats in stats.items():
            self.report += f"### {col}\n"
            for k, v in col_stats.items():
                self.report += f"- {k}: {v}\n"
            self.report += "\n"
        self.report += f"## Visualization\n\n![Hist](data:image/png;base64,{plot_b64})\n"
        return self.report
