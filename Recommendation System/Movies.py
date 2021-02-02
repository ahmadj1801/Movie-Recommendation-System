import pandas as pd
import matplotlib as pt
import re

# Read CSV Files
def read_data():
    global movies, ratings
    ratings = pd.read_csv("../Data/ratings.csv")
    movies = pd.read_csv("../Data/movies.csv")
    print(movies)
    print(ratings)

# Data Statistics
    # Movie ID, Movie Name, Total Rating, Average Rating, Number of votes
def stats():
    global movie_names, genres, average_ratings
    movie_names = movies['title'].unique()
    movie_names = clean_titles(movie_names)
    average_ratings = pd.merge(movies, ratings, left_on='movieId', right_on='movieId',
                    how='left').drop(['userId', 'timestamp'], axis=1).groupby('movieId').mean()
    print(average_ratings)

def clean_titles(titles):
    new_movie_names = []
    for t in titles:
        new_title = re.sub('\([0-9]{4}\)', '', t)
        new_movie_names.append(new_title.strip())
    return new_movie_names

# Data Visualisation
    # Pie Chart -> Number of movies in each genre
    # Pie Chart -> Select Movie -> show rating %

read_data()
stats()

# import pyodbc

# cnxn = pyodbc.connect('DRIVER={CData ODBC Driver for Access};DataSource = ..\Database\Movies.accdb;')
# cursor = cnxn.cursor()
# cursor.execute("SELECT OrderName, Freight FROM Orders WHERE ShipCity = 'New York'")
# rows = cursor.fetchall()
# for row in rows:
    #print(row.OrderName, row.Freight)