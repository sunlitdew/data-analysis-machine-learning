import pandas as pd

from import_data import getDataSet
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def make_plot():
    data = getDataSet()
    fig, ax = plt.subplots(figsize=(10, 6))

    for gender in data['Gender'].unique():
        gender_data = data[data['Gender'] == gender].copy()

        height_bins = np.linspace(gender_data['Height'].min(),
                                  gender_data['Height'].max(), 10)
        gender_data.loc[:, 'Height_bin'] = pd.cut(gender_data['Height'], bins=height_bins)

        stats = gender_data.groupby('Height_bin', observed=True).agg(
            mean_height=('Height', 'mean'),
            mean_weight=('Weight', 'mean'),
            std_weight=('Weight', 'std')
        ).reset_index()

        sns.regplot(
            x='Height',
            y='Weight',
            data=gender_data,
            scatter=False,
            ax=ax,
            label=gender
        )

        ax.errorbar(
            x=stats['mean_height'],
            y=stats['mean_weight'],
            yerr=stats['std_weight'],
            fmt='o',
            markersize=3,
            capsize=3,
            label=f'{gender} ±1 SD',
            alpha=0.7
        )

    plt.title('Height vs Weight by Gender with Standard Deviation Error Bars')
    plt.xlabel('Height')
    plt.ylabel('Weight')
    plt.legend()
    plt.tight_layout(pad=3)
    return fig


def show_plot():
    make_plot()
    plt.show()
    plt.close()


def save_plot_as(filename):
    fig = make_plot()
    fig.savefig(filename)
    plt.close()


if __name__ == '__main__':
    show_plot()