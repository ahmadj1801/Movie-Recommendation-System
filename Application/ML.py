from tkinter import messagebox
import pandas as pd
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
        for movie in self.__user_watched:
            # Check The movie the user rated has not been dropped due to < 5 overall ratings
            if movie in col:
                self.sim = self.sim.append(self.get_recommended_movies(user_similarity, movie,
                                                                       self.__user_watched.get(movie)),
                                           ignore_index=True)
        # Movies Sorted -> highest to Lowest Rating
        sorted_recommendations = self.sim.sum().sort_values(ascending=False)
        # List of Recommendation Titles
        names = []
        # If No Recommendations
        if len(sorted_recommendations) == 0:
            messagebox.showinfo('Insufficient Ratings', 'The movie(s) that you have provided\n'
                                                        'have insufficient ratings to produce\n'
                                                        'meaningful results. Please try rating\n'
                                                        'more movies.')
            return names
        else:
            # Get Titles
            names = sorted_recommendations.index
            # Remove The Movies That the User Has Watched
            final_recommendations = [i for i in names if i not in self.__user_watched]
            # Return Top 10
            return final_recommendations[0:10]

    def get_recommended_movies(self, sim_df, movie_name, user_rating):
        # A Users Rating will be considered Good if > 2.5
        score = sim_df[movie_name] * (float(user_rating) - 2.5)
        score.sort_values(ascending=False)
        return score
