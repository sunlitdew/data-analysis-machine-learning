from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from import_data import getDataSet

def make_plot():
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
    pca = PCA(n_components=2)
    pca_data = StandardScaler().fit_transform(data)
    dataPCA = pd.DataFrame(pca.fit_transform(pca_data), columns=['PC1', 'PC2'])
    dataPCA['Obesity'] = data['Obesity']
    sns.scatterplot(data=dataPCA, x=dataPCA['PC1'], y=dataPCA['PC2'], alpha=0.3, hue='Obesity')
    plt.title('PCA 2 dimensionality reduction')
    plt.tight_layout(pad=3)

def show_plot():
    make_plot()
    plt.show()
    plt.close()


def save_plot_as(filename):
    make_plot()
    plt.savefig(filename)
    plt.close()

if __name__ == '__main__':
    show_plot()