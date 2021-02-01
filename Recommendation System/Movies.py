import pandas as pd

def read_data():
    global movies, ratings
    ratings = pd.read_csv("../Data/ratings.csv")
    movies = pd.read_csv("../Data/movies.csv")

read_data()
