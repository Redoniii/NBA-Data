# NBA Stats Analysis

This project focuses on analyzing NBA player statistics to uncover trends, patterns, and insights into player and team performance. It includes data cleaning, statistical analysis, and visualizations.

## Project Structure

- **data/**: Contains raw and cleaned datasets.
  - `player_stats.csv`: Raw dataset with player statistics.
  - `cleaned_player_stats.csv`: Cleaned dataset ready for analysis.

- **notebooks/**: Contains Jupyter Notebooks for interactive data analysis.
  - `analysis1.ipynb`: Notebook for exploring and visualizing player statistics.

- **environment/**: Contains environment setup files.
  - `requirements.txt`: Lists the required Python packages for the project, including pandas, numpy, matplotlib, and seaborn.

- **images/**: Contains visualizations generated during the analysis.
  - `average-stats-by-pos.png`: Average statistics by player position.
  - `distribution-APG.png`: Distribution of assists per game.
  - `distribution-by-team.png`: Distribution of statistics by team.
  - `distribution-PPG.png`: Distribution of points per game.
  - `Top12.png`: Top 12 players based on performance metrics.

- **src/**: Contains source code for data processing and visualization.
  - `data_analysis.py`: Functions for statistical analysis of player data.
  - `data_visualization.py`: Functions for creating visualizations of player performance metrics.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Nba-Stats