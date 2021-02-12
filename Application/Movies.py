import pandas as pd
import re


class MoviesData:

    movies = ratings = " "

    def __init__(self):
        self.read_data()

    # Read CSV Files
    def read_data(self):
        self.ratings = pd.read_csv("../Data/ratings.csv")
        self.movies = pd.read_csv("../Data/movies.csv")

    def get_movie_names(self):
        movie_names = list(self.movies['title'])
        movie_names.sort()
        return movie_names
