# Data Analysis Project

This project aims to analyze player statistics from the NBA, focusing on various performance metrics such as points per game, assists, rebounds, steals, and blocks. The analysis will provide insights into player performance and team contributions.

## Project Structure

- **data/**: Contains the dataset with player statistics.
  - `players_stats.csv`: The dataset with columns for Player Name, Team, Points Per Game, Assists Per Game, Rebounds Per Game, Steals Per Game, and Blocks Per Game.
  
- **notebooks/**: Contains Jupyter Notebooks for data analysis.
  - `analysis.ipynb`: A notebook for loading the dataset, preprocessing the data, conducting exploratory data analysis, and visualizing the results.
  
- **environment/**: Contains environment setup files.
  - `requirements.txt`: Lists the required Python packages for the project, including pandas, numpy, matplotlib, seaborn, and jupyter.
  
- **src/**: Contains source code for data processing and analysis.
  - `data_preprocessing.py`: Functions for loading, cleaning, and preparing the dataset for analysis.
  - `data_visualization.py`: Functions for creating visualizations of player performance metrics.
  - `statistical_analysis.py`: Functions for performing statistical analysis on the dataset.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd data-analysis-project
   ```

2. **Set up the environment**:
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```
   pip install -r environment/requirements.txt
   ```

4. **Run the analysis**:
   Open the Jupyter Notebook located in the `notebooks/` directory and run the cells to perform the analysis.

## Interpreting Results

The analysis will provide insights into player performance metrics, allowing for comparisons between players and teams. Visualizations will help in understanding trends and patterns in the data.

## License

This project is licensed under the MIT License.