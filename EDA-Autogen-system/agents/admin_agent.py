class AdminAgent:
    def orchestrate(self, df):
        from agents.data_preparation_agent import DataPreparationAgent
        from agents.eda_agent import EDAAgent
        from agents.report_generator_agent import ReportGeneratorAgent
        from agents.critic_agent import CriticAgent
        from agents.executor_agent import ExecutorAgent

        prep = DataPreparationAgent(df)
        clean_df = prep.clean_and_preprocess()

        eda = EDAAgent(clean_df)
        stats, plot_b64 = eda.run_eda()

        reporter = ReportGeneratorAgent()
        report = reporter.create_report(stats, plot_b64)

        critic = CriticAgent()
        feedback = critic.review(report)

        if "look" not in feedback.lower():
            # revise report
            report += "\n\n## Improvements\n" + feedback

        executor = ExecutorAgent()
        validation = executor.validate(clean_df, report)

        return report, feedback, validation
