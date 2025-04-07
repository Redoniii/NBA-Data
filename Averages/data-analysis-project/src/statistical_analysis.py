import pandas as pd
from scipy import stats

def load_data(file_path):
    return pd.read_csv(file_path)

def calculate_averages(df):
    averages = {
        'Points Per Game': df['Points Per Game'].mean(),
        'Assists Per Game': df['Assists Per Game'].mean(),
        'Rebounds Per Game': df['Rebounds Per Game'].mean(),
        'Steals Per Game': df['Steals Per Game'].mean(),
        'Blocks Per Game': df['Blocks Per Game'].mean()
    }
    return averages

def calculate_correlations(df):
    correlation_matrix = df.corr()
    return correlation_matrix

def perform_t_tests(df, column1, column2):
    t_stat, p_value = stats.ttest_ind(df[column1], df[column2])
    return t_stat, p_value

def main():
    file_path = '../data/players_stats.csv'
    df = load_data(file_path)
    
    averages = calculate_averages(df)
    print("Averages:", averages)
    
    correlations = calculate_correlations(df)
    print("Correlation Matrix:\n", correlations)
    
    t_stat, p_value = perform_t_tests(df, 'Points Per Game', 'Assists Per Game')
    print(f"T-test between Points Per Game and Assists Per Game: t-statistic = {t_stat}, p-value = {p_value}")

if __name__ == "__main__":
    main()