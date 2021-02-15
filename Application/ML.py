import pandas as pd
import sklearn

from Movies import MoviesData


# User Collaborative filtering
class Recommended:

    def __init__(self):
        pass

    def __init__(self, watched: dict):
        self.__user_watched = watched
        self.movie_data = MoviesData()
        self.user_data = self.create_user_data_frame()
        pass

    def create_user_data_frame(self):
        return ''

    def get_recommendations(self):
        pass
