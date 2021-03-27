from sklearn.pipeline import Pipeline
from sklearn.preprocessing import (MinMaxScaler, StandardScaler, RobustScaler)
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import numpy as np

def preprocess_X_minmax(X_train, obj):
    X_train_without_year = X_train.drop("Year", axis=1)
    obj_without_year = obj.drop("Year", axis=1)
    num_attribs = ["Kilometers_Driven", "Mileage", "Engine", "Power"]
    cat_attribs = ["Location", "Fuel_Type", "Transmission", "Owner_Type",
                    "Seats", "Brand"]

    
    full_pipeline = ColumnTransformer([
        ("num", MinMaxScaler(), num_attribs),
        ("cat", OneHotEncoder(), cat_attribs),
    ])

    
    full_pipeline.fit(X_train_without_year)
    result = np.append(full_pipeline.transform(obj_without_year).toarray(),
                       np.array(obj['Year']).reshape(-1,1), axis=1)
    
    return result


def preprocess_X_standard(X_train, obj):
    X_train_without_year = X_train.drop("Year", axis=1)
    obj_without_year = obj.drop("Year", axis=1)
    num_attribs = ["Kilometers_Driven", "Mileage", "Engine", "Power"]
    cat_attribs = ["Location", "Fuel_Type", "Transmission", "Owner_Type",
                    "Seats", "Brand"]

    
    full_pipeline = ColumnTransformer([
        ("num", StandardScaler(), num_attribs),
        ("cat", OneHotEncoder(), cat_attribs),
    ])

    
    full_pipeline.fit(X_train_without_year)
    result = np.append(full_pipeline.transform(obj_without_year).toarray(),
                       np.array(obj['Year']).reshape(-1,1), axis=1)
    
    return result


def preprocess_X_robust(X_train, obj):
    X_train_without_year = X_train.drop("Year", axis=1)
    obj_without_year = obj.drop("Year", axis=1)
    num_attribs = ["Kilometers_Driven", "Mileage", "Engine", "Power"]
    cat_attribs = ["Location", "Fuel_Type", "Transmission", "Owner_Type",
                    "Seats", "Brand"]

    
    full_pipeline = ColumnTransformer([
        ("num", RobustScaler(), num_attribs),
        ("cat", OneHotEncoder(), cat_attribs),
    ])

    
    full_pipeline.fit(X_train_without_year)
    result = np.append(full_pipeline.transform(obj_without_year).toarray(),
                       np.array(obj['Year']).reshape(-1,1), axis=1)
    
    return result