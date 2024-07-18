<h1>Tennis Matches Dataset Analysis</h1>


This project involves cleaning, filtering, and analyzing a dataset of ATP tennis matches from 1970(ish) to 2024. 
The main objectives are to prepare the dataset for analysis and create functions to extract meaningful insights about players' performances.

<h3>Dataset Cleaning and Preparation</h3>
-  Reading the Data
-  Load datasets for matches from 2000 to 2024 (Feb)
-  Concatenate these datasets into a single DataFrame.
-  Dropping Unnecessary Columns for the analysis 
-  Remove columns that are not required for the analysis.

<h3>Date Formatting</h3>
-  Convert the tourney_date column to a datetime format.
-  Filter the data to include only matches from the year 2000 onwards.
-  Focusing on Winner Statistics
-  Drop columns related to the losers to focus on the winner statistics.
-  Column Renaming
-  Rename columns to remove prefixes like "winner" or "w_".
-  Replace certain column names for better clarity (e.g., 'ht' to 'height', 'ioc' to 'country', 'df' to 'double_faults').
-  Standardizing Player Names
-  Convert all player names to lowercase for consistency.
-  Saving the Cleaned Dataset
-  Save the cleaned and filtered dataset to a CSV file (matches.csv).


<h3>Analysis Functions</h3>
-  Multiple functions are created to analyze the cleaned dataset and extract specific insights about players' performances:

Career High Ranking
-  career_high(df): Returns the highest ranking achieved by a player and the year it was reached.
Max Rank Points
-  max_rank_points(df): Returns the highest ranking points achieved by a player and the year it was reached.
Tournaments Won
-  num_tour_won(df, nombre): Returns the number of tournaments won by a player and the distribution of these wins by tournament.
Service Points Won by Surface
-  mean_svpt_surf(df): Returns the average percentage of service points won by surface type.
Aces Analysis
-  aces(df): Returns the total and average number of aces made by a player, grouped by surface type.
Comprehensive Player Analysis
-  analysis(df, nombre): Combines the above functions to provide a comprehensive analysis of a player's performance based on their name (provided in lowercase).



<h2>Example Usage:</h2>
-  print(analysis(matches, "novak djokovic"))


<br>The player name should be in lower case.
The filter of player after the year 2000 could be removed. I mainly used it to focus on certain players. 
</br>

