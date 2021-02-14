import pandas as pd
import re


class MoviesData:

    def __init__(self):
        self.movies = self.ratings = ''
        self.read_data()

    # Read CSV Files
    def read_data(self):
        self.ratings = pd.read_csv("../Data/ratings.csv")
        self.movies = pd.read_csv("../Data/movies.csv")

    def get_movie_names(self):
        movie_names = list(self.movies['title'])
        movie_names.sort()
        return movie_names

    def get_movie_data_frame(self):
        return self.movies

    def get_ratings_data_frame(self):
        return self.ratings