# Import Required Libraries
import pandas as pd

# Load the CSV file
file_path = "../data/player_stats.csv"  # Adjust the path if necessary
data = pd.read_csv(file_path)

# Data Cleaning
# Drop rows with missing values
cleaned_data = data.dropna()

# Convert numeric columns to appropriate data types
numeric_columns = ['Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%',
                   'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
for col in numeric_columns:
    if col in cleaned_data.columns:
        cleaned_data[col] = pd.to_numeric(cleaned_data[col], errors='coerce')

# Drop rows with invalid numeric data
cleaned_data = cleaned_data.dropna(subset=numeric_columns)

# Analysis
# Top 10 players by points per game
top_scorers = cleaned_data.nlargest(15, 'PTS')[['Player', 'PTS']]
print("Top 15 Players by Points Per Game:")
print(top_scorers)

# Average statistics by position
average_stats_by_position = cleaned_data.groupby('Pos')[numeric_columns].mean()
print("\nAverage Statistics by Position:")
print(average_stats_by_position)

# Distribution of players by team
players_by_team = cleaned_data['Team'].value_counts()
print("\nNumber of Players by Team:")
print(players_by_team)

# Save cleaned data to a new CSV file (optional)
cleaned_data.to_csv("../data/cleaned_player_stats.csv", index=False)
print("\nCleaned data saved to 'cleaned_player_stats.csv'")