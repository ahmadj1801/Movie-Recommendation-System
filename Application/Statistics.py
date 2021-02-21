import pandas as pd
import re

from Movies import MoviesData

'''
movies = ratings = None
movie_names = genres = average_ratings = None


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
    return new_movie_names'''
m = MoviesData()
# print(m.movies_per_star_rating())
# print(m.most_reviewed_movies())
# print(m.least_reviewed_movies())
# m.highest_rated_movies()
'''x = re.sub('\([0-9]{4}\)', '', 'Iron man (2014)')
x = (re.findall('\([0-9]{4}\)', 'Iron man (2014)'))[0]
x = re.sub('\(', '', x)
x = re.sub('\)', '', x)
print(x)'''
m.movies_per_year()