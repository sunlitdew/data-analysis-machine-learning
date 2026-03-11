import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from import_data import getDataSet

def make_matrix():
    data = getDataSet()
    data['Gender'] = data['Gender'].map({'Female': 0, 'Male': 1})
    binary_cols = ['Family History', 'High caloric', 'Smoking', 'Monitoring']
    for col in binary_cols:
        data[col] = data[col].map({'no': 0, 'yes': 1})


    frequency_mapping = {'no': 0, 'Sometimes': 1, 'Frequently': 2, 'Always': 3}
    data['Snacks'] = data['Snacks'].map(frequency_mapping)
    data['Alcohol'] = data['Alcohol'].map(frequency_mapping)


    data = pd.get_dummies(data,
                          columns=['Transport'],
                          prefix_sep='',
                          prefix='',
                          drop_first=True)

    data = data.rename(columns={"Public_Transportation": "Public Transit"})

    obesity_order = [
        'Insufficient Weight',
        'Normal Weight',
        'Overweight Level I',
        'Overweight Level II',
        'Obesity Type I',
        'Obesity Type II',
        'Obesity Type III'
    ]

    data['Obesity'] = data['Obesity'].map(
        {category: idx for idx, category in enumerate(obesity_order)}
    )

    corr_matrix = data.corr()

    plt.figure(figsize=(15, 12))
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    heatmap = sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, vmin=-0.5, vmax=0.5,
                          mask=mask)


    heatmap.set_yticklabels([""] + heatmap.get_yticklabels()[1:])
    heatmap.set_xticklabels(heatmap.get_xticklabels()[:-1] + [""])
    plt.title("Correlation Matrix")
    plt.tight_layout(pad=3)


def show_matrix():
    make_matrix()
    plt.show()
    plt.close()

def save_matrix_as(filename):
    make_matrix()
    plt.savefig(filename)
    plt.close()

if __name__ == '__main__':
    show_matrix()