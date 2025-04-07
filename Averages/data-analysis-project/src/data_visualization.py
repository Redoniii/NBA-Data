import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_points_per_game(data):
    # Sort the data by 'Points Per Game' in descending order
    sorted_data = data.sort_values(by='Points Per Game', ascending=False)
    
    # Plot the sorted data
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Player Name', y='Points Per Game', data=sorted_data, palette='viridis')
    plt.xticks(rotation=45)
    plt.title('Points Per Game by Player')
    plt.xlabel('Player Name')
    plt.ylabel('Points Per Game')
    plt.tight_layout()
    plt.show()

def plot_assists_per_game(data):
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Player Name', y='Assists Per Game', data=data, palette='magma')
    plt.xticks(rotation=45)
    plt.title('Assists Per Game by Player')
    plt.xlabel('Player Name')
    plt.ylabel('Assists Per Game')
    plt.tight_layout()
    plt.show()

def plot_rebounds_per_game(data):
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Player Name', y='Rebounds Per Game', data=data, palette='plasma')
    plt.xticks(rotation=45)
    plt.title('Rebounds Per Game by Player')
    plt.xlabel('Player Name')
    plt.ylabel('Rebounds Per Game')
    plt.tight_layout()
    plt.show()

def plot_scatter_points_assists(data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Points Per Game', y='Assists Per Game', data=data, hue='Team', style='Team', s=100)
    plt.title('Points Per Game vs Assists Per Game')
    plt.xlabel('Points Per Game')
    plt.ylabel('Assists Per Game')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()