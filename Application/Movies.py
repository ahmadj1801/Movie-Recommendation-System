import pandas as pd
import matplotlib.pyplot as plt
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

    def get_filtered_df(self, movie_name):
        df = self.movies[self.movies.title == movie_name]
        return df

    def get_average_rating(self, movie_name):
        df = self.get_filtered_df(movie_name)
        print(df)
        average_ratings: pd.DataFrame = pd.merge(df, self.ratings, left_on='movieId', right_on='movieId',
                                                 how='left').drop(['userId', 'timestamp'], axis=1).groupby(
            'movieId').mean()
        print(average_ratings)
        return round((average_ratings['rating'].tolist())[0], 2)

    def get_total_number_of_reviews(self, movie_name):
        df = self.get_filtered_df(movie_name)
        df: pd.DataFrame = pd.merge(df, self.ratings, left_on='movieId', right_on='movieId',
                                    how='left').drop(['userId', 'timestamp'], axis=1)
        total_count = df.shape[0]
        return total_count

    def get_number_of_x_ratings(self, movie_name, star_levels):
        df = self.get_filtered_df(movie_name)
        df: pd.DataFrame = pd.merge(df, self.ratings, left_on='movieId', right_on='movieId',
                                    how='left').drop(['userId', 'timestamp'], axis=1)
        print(df)
        df = df.groupby(pd.cut(df.rating, star_levels)).count()
        print(df)
        df = df['rating'].tolist()
        print(df)
        return df

    @staticmethod
    def format_name(movie_name):
        c = 1
        movie = str(movie_name).split(" ")
        new_name = ''
        for m in movie:
            new_name = "{0} {1}".format(new_name, str(m))
            if c % 3 == 0:
                new_name = new_name + "\n"
            c = c + 1
        return new_name

    # ==================================== Data Analytics =====================================

    def top_five_movies(self):
        top_5 = pd.merge(self.movies, self.ratings, left_on='movieId', right_on='movieId')
        top_5 = top_5['title'].value_counts(ascending=False)
        top_5 = top_5.head(5)
        movie_names = top_5.index
        graph = plt.figure(figsize=(20, 10))
        plt.bar(movie_names, top_5, color=['teal', 'springgreen', 'mediumaquamarine'], width=0.5)
        plt.xlabel('Title')
        plt.ylabel('Number of Ratings')
        plt.title('Most Reviewed Movies')
        plt.show()
        pass  # Display movie names and the rating (Store)

    def bottom_five_movies(self):
        bottom_5 = pd.merge(self.movies, self.ratings, left_on='movieId', right_on='movieId')
        bottom_5 = bottom_5['title'].value_counts(ascending=True)
        bottom_5 = bottom_5.head(5)
        movie_names = bottom_5.index
        graph = plt.figure(figsize=(20, 10))
        plt.bar(movie_names, bottom_5, color=['royalblue', 'violet', 'orchid'], width=0.5)
        plt.xlabel('Title')
        plt.ylabel('Number of Ratings')
        plt.title('Least Reviewed Movies')
        plt.show()
        pass  # Display movie names and the rating (Store)

    def movie_analytics(self):
        pass  # Movie name -> pie charge of ratings in each category (Create)

    def movies_per_star_rating(self):
        pass  # For each star rating, how many movies in each category (Create)

    def highest_rated_movies(self):
        highest = pd.merge(self.movies, self.ratings, left_on='movieId', right_on='movieId').drop(['userId',
                                                                                                   'timestamp', 'genres'
                                                                                                      , 'movieId'],
                                                                                                  axis=1)
        highest = (highest.groupby('title').mean('rating')).sort_values('rating', ascending=False)
        print(highest)
        pass

    def lowest_rated_movies(self):
        pass
