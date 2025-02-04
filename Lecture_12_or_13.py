import pandas as pd
import os

# Fix the file path using one of the three solutions
HOUSING_PATH = r"C:\Users\Asus\Desktop\python\ml\machine_learning\datasets\housing"

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")  # Joins path safely
    return pd.read_csv(csv_path)

housing = load_housing_data()
print(housing.head())  # Print first few rows
