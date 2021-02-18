from tkinter import messagebox

import pandas as pd
import sklearn

from Movies import MoviesData


# User Collaborative filtering => People with similar characteristics, will have similar taste
class Recommended:

    def __init__(self, watched: dict):
        # Movies that the user watched
        self.__user_watched = watched
        # Movies Data Object => Contains the project data
        self.movie_data = MoviesData()
        # Data Frame Containing Similarities
        self.sim: pd.DataFrame = pd.DataFrame()
        pass

    @property
    def get_recommendations(self):
        movie_rating: pd.DataFrame = pd.merge(self.movie_data.get_movie_data_frame(),
                                              self.movie_data.get_ratings_data_frame()).drop(['timestamp'], axis=1)
        # Get Data Frame in Desired Format
        movie_rating = movie_rating.pivot_table(index=['userId'], columns=['title'],
                                                values='rating')
        # Drop movies that have less than 5 Ratings
        movie_rating = movie_rating.dropna(thresh=5, axis=1)
        # fill NaN wil 0
        movie_rating = movie_rating.fillna(0)
        # Similarity Values
        user_similarity = movie_rating.corr(method='pearson')
        col = user_similarity.columns
        for movie in self.__user_watched:  #
            if movie in col:
                self.sim = self.sim.append(self.get_recommended_movies(user_similarity, movie,
                                                                       self.__user_watched.get(movie)),
                                           ignore_index=True)
        print(self.sim.head())
        sorted_recommendations = self.sim.sum().sort_values(ascending=False)
        if len(sorted_recommendations) == 0:
            messagebox.showinfo('Insufficient Ratings', 'There are insufficient ratings to recommend you a movie')
        print(sorted_recommendations.index)
        names = sorted_recommendations.index
        final_recommendations = [i for i in names if i not in self.__user_watched]
        print(final_recommendations)
        return final_recommendations[0:10]

    def get_recommended_movies(self, sim_df, movie_name, user_rating):
        score = sim_df[movie_name] * (float(user_rating) - 2.5)
        score.sort_values(ascending=False)
        return score
