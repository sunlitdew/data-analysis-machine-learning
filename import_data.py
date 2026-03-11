from ucimlrepo import fetch_ucirepo
import pandas as pd

# fetch dataset
datatable = fetch_ucirepo(id=544)
#datatable = pd.read_csv("name.csv")

dataset = pd.concat([datatable.data.features, datatable.data.targets], axis=1)

variable_name_dict = dict([
    ('Gender', 'Gender'),
    ('Age', 'Age'),
    ('Height', 'Height'),
    ('Weight', 'Weight'),
    ('family_history_with_overweight', 'Family History'),
    ('FAVC', 'High caloric'),
    ('FCVC', 'Vegetables'),
    ('NCP', 'Meals'),
    ('CAEC', 'Snacks'),
    ('SMOKE', 'Smoking'),
    ('CH2O', 'Water'),
    ('SCC', 'Monitoring'),
    ('FAF', 'Activity'),
    ('TUE', 'Devices'),
    ('CALC', 'Alcohol'),
    ('MTRANS', 'Transport'),
    ('NObeyesdad', 'Obesity')
])

numeric = ['Age', 'Height', 'Weight', 'Vegetables', 'Meals', 'Water', 'Activity', 'Devices']
non_numeric = ['Gender', 'Family History', 'High caloric', 'Snacks', 'Smoking', 'Monitoring', 'Activity', 'Alcohol', 'Transport', 'Obesity']

dataset = dataset.rename(columns=variable_name_dict)
dataset['Transport'] = dataset['Transport'].map(lambda x: "Public Transit" if x == "Public_Transportation" else x)

obesity_order = [
    'Insufficient_Weight',
    'Normal_Weight',
    'Overweight_Level_I',
    'Overweight_Level_II',
    'Obesity_Type_I',
    'Obesity_Type_II',
    'Obesity_Type_III'
]

obesity_dict = {
    'Insufficient_Weight' : 'Insufficient Weight',
    'Normal_Weight' : 'Normal Weight',
    'Overweight_Level_I' : 'Overweight Level I',
    'Overweight_Level_II' : 'Overweight Level II',
    'Obesity_Type_I' : 'Obesity Type I',
    'Obesity_Type_II' : 'Obesity Type II',
    'Obesity_Type_III' : 'Obesity Type III'
}

dataset['Obesity'] = pd.Categorical(
    dataset['Obesity'],
    categories=obesity_order,
    ordered=True
)

dataset['Obesity'] = dataset['Obesity'].map(obesity_dict)


def getDataSet():
    return dataset.copy()