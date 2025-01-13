import pandas as pd
from variables import DATA_FILE

def load_data():
    """Loads data from the CSV file."""
    df = pd.read_csv(DATA_FILE)
    return df

def preprocess_data(df):
    """Preprocesses the data (combines 'Jaar' and 'Kwartaal')."""
    df['JaarKwartaal'] = df['Jaar'].astype(str) + " " + df['Kwartaal']
    return df