import numpy as np 
import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle

def train_model(training_data_path):
    training_data = pd.read_csv(training_data_path)

    features = training_data.drop(columns=['Appliances'])
    target = training_data['Appliances']

    train_X, test_X, train_y, test_y = train_test_split(features, target, test_size=0.25, random_state=40)

    cols_to_drop = ['lights', 'rv1', 'rv2', 'Visibility', 'T6', 'T9', 'date']

    train_X = train_X.drop(cols_to_drop, axis=1)
    test_X = test_X.drop(cols_to_drop, axis=1)

    scaler = StandardScaler()
    train_X_scaled = scaler.fit_transform(train_X)
    test_X_scaled = scaler.transform(test_X)

    model = RandomForestRegressor(random_state=78)
    model.fit(train_X_scaled, train_y)

    pickle.dump(model, open('model.pkl','wb'))

def predict_energy_consumption(input_data):
    model = pickle.load(open('model.pkl','rb'))

    scaler = StandardScaler()
    input_data_scaled = scaler.transform(input_data)

    predictions = model.predict(input_data_scaled)

    return predictions

train_data_path = r'C:\Users\User\Documents\Agile Data Science\energyconsumption\energyconsumption\KAG_energydata_complete.csv'
train_model(train_data_path)