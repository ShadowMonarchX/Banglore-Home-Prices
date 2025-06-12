import json
import numpy as np
import os
import joblib  # Use joblib instead of pickle

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("Loading saved artifacts...")

    global __data_columns
    global __locations
    global __model

    base_path = os.path.dirname(__file__)
    columns_path = os.path.join(base_path, "artifacts/columns.json")
    model_path = os.path.join(base_path, "artifacts/model.joblib")  # updated filename

    with open(columns_path, "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # assuming sqft, bath, bhk come first

    if __model is None:
        __model = joblib.load(model_path)

    print("Artifacts loaded successfully.")


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))
