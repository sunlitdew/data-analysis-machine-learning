import os

import pandas as pd

from import_data import dataset

data = dataset.copy()
numeric_dataset = data.select_dtypes('number')
categorical_dataset = data.select_dtypes('object')

numeric_desc = numeric_dataset.describe([0.05, 0.95])
numeric_desc.drop('count', axis=0, inplace=True)
numeric_desc.drop('50%', axis=0, inplace=True)
numeric_desc.loc['nulls'] = numeric_dataset.isnull().sum()

categorical_desc = categorical_dataset.describe()
categorical_desc.drop('count', axis=0, inplace=True)
categorical_desc.drop('top', axis=0, inplace=True)
categorical_desc.drop('freq', axis=0, inplace=True)
categorical_desc.loc['nulls'] = categorical_dataset.isnull().sum()

value_counts = {}
for column in categorical_dataset.columns:
    value_counts[column] = {key: f"{value*100:.2f}%"
                           for key, value in categorical_dataset[column].value_counts(normalize=True).to_dict().items()}

def save_csvs():
    os.makedirs('csvs', exist_ok=True)
    numeric_desc.to_csv('csvs/numeric_description.csv')
    categorical_desc.transpose().to_csv('csvs/categorical_description.csv')

    value_counts_df = pd.DataFrame.from_dict({(i, j): value_counts[i][j]
                                              for i in value_counts.keys()
                                              for j in value_counts[i].keys()},
                                             orient='index')
    value_counts_df.to_csv('csvs/categorical_value_counts.csv')

if __name__ == '__main__':
    save_csvs()