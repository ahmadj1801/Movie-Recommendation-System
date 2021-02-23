import pandas as pd
import matplotlib.pyplot as plt
import os
import re


class MoviesData:

    def __init__(self):
        self.movies = self.ratings = ''
        self.read_data()

    # Read CSV Files
    def read_data(self):
        # Read Data
        self.ratings = pd.read_csv("../Data/ratings.csv")
        self.movies = pd.read_csv("../Data/movies.csv")
        # Set Mat-plot-Lib up
        plt.rcParams['font.size'] = 15
        plt.rc('axes', labelsize=20)
        plt.style.use('fivethirtyeight')

    # List of Movie Titles
    def get_movie_names(self):
        # Convert to List
        movie_names = list(self.movies['title'])
        # Sort
        movie_names.sort()
        return movie_names

    # Return movie Data Frame
    def get_movie_data_frame(self):
        return self.movies

    # Return Ratings Data Frame
    def get_ratings_data_frame(self):
        return self.ratings

    # Filtered Data Frame on a Specific Movie Title
    def get_filtered_df(self, movie_name):
        df = self.movies[self.movies.title == movie_name]
        return df

    # Average Ratings
    def get_average_rating(self, movie_name):
        df = self.get_filtered_df(movie_name)
        # Drop Unnecessary Columns - Use Mean
        average_ratings: pd.DataFrame = pd.merge(df, self.ratings, left_on='movieId', right_on='movieId',
                                                 how='left').drop(['userId', 'timestamp'], axis=1).groupby(
            'movieId').mean()
        # Return Average Ratings - 2 Decimal Places
        return round((average_ratings['rating'].tolist())[0], 2)

    # Total Reviews on a Specific Movie
    def get_total_number_of_reviews(self, movie_name):
        df = self.get_filtered_df(movie_name)
        # Merging Based on ID
        df: pd.DataFrame = pd.merge(df, self.ratings, left_on='movieId', right_on='movieId',
                                    how='left').drop(['userId', 'timestamp'], axis=1)
        # Shape will give size
        total_count = df.shape[0]
        return total_count

    # Number of Ratings per Star Level
    def get_number_of_x_ratings(self, movie_name, star_levels):
        df = self.get_filtered_df(movie_name)
        # Columns - movieId, rating, genres
        df: pd.DataFrame = pd.merge(df, self.ratings, left_on='movieId', right_on='movieId',
                                    how='left').drop(['userId', 'timestamp'], axis=1)
        df = df.groupby(pd.cut(df.rating, star_levels)).count()
        df = df['rating'].tolist()
        return df

    # Method to Format the Movie Title
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

    # Return Release Year - IF Irregular Format, return 0
    def get_year(self, movie_name):
        year = 0
        # Regular Expressions to find the Year
        year = re.findall('\([0-9]{4}\)', movie_name)
        if year != []:
            year = year[0]
            year = re.sub('\(', '', year)
            year = re.sub('\)', '', year)
        else:
            year = 0
        return int(year)

    # ==================================== Data Analytics =====================================

    # Graph Most Reviewed Movies
    def most_reviewed_movies(self):
        path = '../Images/most_reviewed_movies.png'
        if not os.path.exists(path):
            top_5 = pd.merge(self.movies, self.ratings, left_on='movieId', right_on='movieId')
            top_5 = top_5['title'].value_counts(ascending=False)
            top_5 = top_5.head(5)
            movie_names = top_5.index
            graph = plt.figure(figsize=(20, 10))
            plt.bar(movie_names, top_5, color=['teal', 'yellowgreen', 'crimson'], width=0.5)
            plt.xlabel('Title')
            plt.ylabel('Number of Ratings')
            plt.title('Most Reviewed Movies')
            plt.savefig(path)
        return path  # Display movie names and the rating (Store)

    # Graph Least Reviewed Movies
    def least_reviewed_movies(self):
        path = '../Images/least_reviewed_movies.png'
        if not os.path.exists(path):
            bottom_5 = pd.merge(self.movies, self.ratings, left_on='movieId', right_on='movieId')
            bottom_5 = bottom_5['title'].value_counts(ascending=True)
            bottom_5 = bottom_5.head(5)
            movie_names = bottom_5.index
            graph = plt.figure(figsize=(20, 10))
            plt.bar(movie_names, bottom_5, color=['goldenrod', 'steelblue', 'coral'], width=0.5)
            plt.xlabel('Title')
            plt.ylabel('Number of Ratings')
            plt.title('Least Reviewed Movies')
            plt.savefig(path)
        return path  # Display movie names and the rating

    # Pie Chart
    def movies_per_star_rating(self):
        path = '../Images/movies_per_star.png'
        if not os.path.exists(path):
            star = pd.merge(self.movies, self.ratings, left_on='movieId', right_on='movieId',
                            how='left').drop(['userId', 'timestamp'], axis=1).groupby(
                'movieId').mean()
            star = star.groupby(pd.cut(star.rating, [0, 1, 2, 3, 4, 5])).count()
            pie = plt.figure()
            axis = pie.add_axes([0, 0, 1, 1])
            axis.axis('equal')
            headings = ['0 - 1 Star', '1  - 2 Star', '2 - 3 Star', '3 - 4 Star', '4 - 5 Star']
            ratings = [x[0] for x in star.values]
            axis.pie(ratings, labels=headings, autopct='%1.2f%%', colors=['goldenrod', 'crimson', 'blueviolet',
                                                                          'teal', 'yellowgreen'])
            plt.savefig(path)
        return path  # For each star rating, how many movies in each category

    # Graph Highest Rated Movies
    def highest_rated_movies(self):
        path = '../Images/highest_rated_movies.png'
        if not os.path.exists(path):
            highest = pd.merge(self.movies, self.ratings, left_on='movieId', right_on='movieId').drop(['userId',
                                                                                                       'timestamp',
                                                                                                       'genres'
                                                                                                          , 'movieId'],
                                                                                                      axis=1)
            highest = (highest.groupby('title').mean('rating')).sort_values('rating', ascending=False)
            most_reviewed = pd.merge(self.movies, self.ratings, left_on='movieId', right_on='movieId')
            most_reviewed = most_reviewed['title'].value_counts(ascending=False)
            d = {'title': most_reviewed.index, 'reviews': most_reviewed.values}
            most_reviewed = pd.DataFrame(d)
            highest = pd.merge(most_reviewed, highest, left_on='title', right_on='title')
            highest = highest[highest['reviews'] >= 5]
            highest = highest.sort_values('rating', ascending=False)
            highest = highest.head(5).drop(['reviews'], axis=1)
            graph = plt.figure(figsize=(20, 10))
            plt.bar(highest['title'], highest['rating'], color=['palevioletred', 'plum', 'powderblue'], width=0.5)
            plt.xlabel('Title')
            plt.ylabel('Average rating', )
            plt.title('Highest Rated Movies')
            plt.savefig(path)
        return path

    # Line Graph of Movies Per Year
    def movies_per_year(self):
        path = '../Images/movies_per_year.png'
        if not os.path.exists(path):
            titles = self.movies['title']
            per_year = dict()
            release_years = []
            frequencies = []
            c = 0
            for title in titles:
                year = str(self.get_year(title))
                if year not in per_year.keys():
                    per_year[year] = 1
                else:
                    per_year[year] = per_year.get(year) + 1
            for i in sorted(per_year):
                release_years.append(i)
                frequencies.append(int(per_year[i]))
            plt.figure(figsize=(20, 10))
            plt.plot(release_years, frequencies, color='darkviolet', linewidth=5)
            plt.title('Number of Movie Releases Per Year')
            plt.xlabel('Year')
            plt.ylabel('Number of Movie Releases')
            plt.xticks(release_years[::10])
            plt.savefig(path)
        return path
