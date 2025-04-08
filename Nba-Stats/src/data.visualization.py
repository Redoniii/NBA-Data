import matplotlib.pyplot as plt
import seaborn as sns

# Bar plot for top 12 players by points per game
plt.figure(figsize=(10, 6))
sns.barplot(x='PTS', y='Player', data=top_scorers, palette='viridis')
plt.title('Top 12 Players by Points Per Game', fontsize=16)
plt.xlabel('Points Per Game', fontsize=12)
plt.ylabel('Player', fontsize=12)
plt.show()


# Bar plot for average statistics by position
plt.figure(figsize=(12, 8))
sns.heatmap(average_stats_by_position[numeric_columns], annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Average Statistics by Position', fontsize=16)
plt.xlabel('Statistics', fontsize=12)
plt.ylabel('Position', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Pie chart for distribution of players by team
plt.figure(figsize=(8, 8))
players_by_team.plot(kind='pie', autopct='%1.1f%%', startangle=140, legend=False)
plt.title('Distribution of Players by Team', fontsize=16)
plt.ylabel('')  # Remove y-axis label
plt.show()


# Histogram for points per game distribution
plt.figure(figsize=(10, 6))
sns.histplot(cleaned_data['PTS'], bins=20, kde=True, color='blue')
plt.title('Distribution of Points Per Game', fontsize=16)
plt.xlabel('Points Per Game', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()



# Histogram for asist per game distribution
plt.figure(figsize=(10, 6))
sns.histplot(cleaned_data['AST'], bins=20, kde=True, color='blue')
plt.title('Distribution of Asist Per Game', fontsize=16)
plt.xlabel('Asist Per Game', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()