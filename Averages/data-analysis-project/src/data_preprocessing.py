import pandas as pd

def load_data(file_path):
    """Load the dataset from a CSV file."""
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    """Clean the dataset by handling missing values and converting data types."""
    # Drop rows with missing values
    data = data.dropna()
    
    # Convert data types if necessary
    data['Points Per Game'] = data['Points Per Game'].astype(float)
    data['Assists Per Game'] = data['Assists Per Game'].astype(float)
    data['Rebounds Per Game'] = data['Rebounds Per Game'].astype(float)
    data['Steals Per Game'] = data['Steals Per Game'].astype(float)
    data['Blocks Per Game'] = data['Blocks Per Game'].astype(float)
    
    return data

def preprocess_data(file_path):
    """Load and clean the dataset."""
    data = load_data(file_path)
    cleaned_data = clean_data(data)
    return cleaned_data