#importing packages for the fix of datetime tourney_date
import pandas as pd
import datetime 


#reading the csv created in 'cleaning.ipynb' which is a focused on data cleaning and filtering for the purpose of the analysis
matches = pd.read_csv('matches.csv', delimiter=',')


#Changing the type of tourney_date 
matches['tourney_date'] = pd.to_datetime(matches['tourney_date'], format='%Y-%m-%d')



"""
Creating multiple functions and adding them all to the function "analysis".
The dataset is updated until february of 2024, so some tournaments will not be showed and rankings are not updated after that


"""
def career_high(df):
    max_rank = df.loc[df['rank'] == df['rank'].min()]
    year = max_rank['tourney_date'].dt.year.iloc[0]
    
    return f'Career High Ranking:\nReached career high ranking number {max_rank["rank"].iloc[0]} in the year {year}.'

def max_rank_points(df):
    max_points = df.loc[df['rank_points'] == df['rank_points'].max()]
    year = max_points['tourney_date'].dt.year.iloc[0]

    return f'Max Rank Points:\nReached career high ranking points of {max_points["rank_points"].iloc[0]} in the year {year}.'


def num_tour_won(df, nombre):
    ganados = df[df['round'] == 'F'].loc[df['name'] == nombre, 'tourney_name']
    conteo_por_torneo = ganados.value_counts()
    total_torneos_ganados = sum(conteo_por_torneo)

    return f'Tournaments Won:\nWon {total_torneos_ganados} tournaments, corresponding to:\n{conteo_por_torneo.to_string()}.' 


def mean_svpt_surf(df):
    porcentaje = round(df.groupby('surface')['svpt'].mean(),2)

    return f'Percentage of won serves in different surfaces are:\n{porcentaje.to_string(header = False)}'


def aces(df):
    sum_aces = df.groupby('surface')['ace'].sum()
    mean_aces = round(df.groupby('surface')['ace'].mean(),2)

    return f'Aces Analysis:\nThe sum of aces in different surfaces are:\n{sum_aces.to_string(header = False)}\n\nThe mean of aces in different surfaces are:\n{mean_aces.to_string(header = False)}'


def analysis(df, nombre):
    df = df[df['name'].str.contains(nombre)]
    
    high = career_high(df)
    rank = max_rank_points(df)
    tourn = num_tour_won(df, nombre)
    svpt = mean_svpt_surf(df)
    ace = aces(df)

    return f'{high}\n\n{rank}\n\n{tourn}\n\n{svpt}\n\n{ace}'
    



#Using the last function to display the analysis of a player, which should be provided in lower case. 
print(analysis(matches, "novak Djokovic"))
