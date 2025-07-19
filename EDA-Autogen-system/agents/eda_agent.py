import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io, base64

class EDAAgent:
    def __init__(self, df):
        self.df = df

    def run_eda(self):
        stats = self.df.describe(include='all').to_dict()
        # Basic histogram example
        plot_img = io.BytesIO()
        sns.histplot(self.df.select_dtypes(include='number').iloc[:,0])
        plt.savefig(plot_img, format='png')
        plot_img.seek(0)
        plot_b64 = base64.b64encode(plot_img.getvalue()).decode()
        return stats, plot_b64
