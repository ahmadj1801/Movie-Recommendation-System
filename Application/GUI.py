import tkinter
import os
import pandas as pd
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np

from Movies import MoviesData


def calculate_centre(window):
    position_right = position_down = 0
    win_width = window.winfo_reqwidth()
    win_height = window.winfo_reqheight()
    position_right = int(window.winfo_screenwidth() / 2 - win_width / 2)
    position_down = int(window.winfo_screenheight() / 2 - win_height / 2)
    return position_right, position_down


class HomeForm:
    # Private Class attributes
    __lbl_intro = __btn_movies = __btn_stats = __btn_recommendation = ''

    def __init__(self):
        # Create Window
        window = tkinter.Tk()
        # Window Title
        window.title("Movie System")
        pos_right, pos_down = calculate_centre(window)
        # Window Size
        window.geometry("+{}+{}".format(pos_right, pos_down))
        # Set Row sizes
        window.rowconfigure([0, 1, 2, 3], minsize=50)
        # Set Column Sizes
        window.columnconfigure([0, 1, 2], minsize=100)
        # Heading
        self.__lbl_intro = tkinter.Label(window, text='Welcome to the Movie Recommendation System!',
                                         font=("Arial Bold", 10)).grid(row=0, column=1)
        # Click to View Movies in the Data Set
        self.__btn_movies = tkinter.Button(window, text="View Movies", width=20,
                                           command=self.btn_movies_click).grid(row=1, column=1)
        # Click to View Data Analytics
        self.__btn_stats = tkinter.Button(window, text="View Data Analytics", width=20,
                                          command=self.btn_stats_click).grid(row=2, column=1)
        # Click to perform Machine Learning
        self.__btn_recommendation = tkinter.Button(window, text="Movie Recommendations", width=20,
                                                   command=self.btn_recommendation_click).grid(row=3, column=1)
        # Window Stays Open until closed
        window.mainloop()

    @staticmethod
    def btn_movies_click():
        # Open Movies Page
        movie_form = MoviesForm()
        pass

    @staticmethod
    def btn_stats_click():
        # Open Stats Page
        stats_form = StatisticsForm()
        pass

    @staticmethod
    def btn_recommendation_click():
        # Open Movie Recommendation Page
        recommendation_form = MovieRecommendationForm()
        pass


# ====================================END HomeForm Class================================================


class StatisticsForm:
    __lbl_intro = ''

    def __init__(self):
        window = tkinter.Tk()
        window.title("Data Visualization")
        window.geometry('400x400')
        window.rowconfigure([0, 1, 2, 3], minsize=50)
        window.columnconfigure([0, 1, 2], minsize=100)
        self.__lbl_intro = tkinter.Label(window, text='Data Visualisation',
                                         font=("Arial Bold", 15)).grid(row=0, column=1)


# ====================================END HomeForm Class================================================

class MoviesForm:

    def __init__(self):
        # Main Window
        self.window = tkinter.Toplevel()
        self.window.title("Movies")
        self.window.geometry('500x400')
        self.window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], minsize=20)
        self.window.columnconfigure([0, 1, 2], minsize=200)
        # Movie Data Frames
        self.movie_data = MoviesData()
        # Set Up Drop Down Component
        self.variable = tkinter.StringVar(self.window)
        self.variable.set("--Select--")
        self.variable.trace('w', self.option_callback)
        self.__drp_movie = ttk.Combobox(self.window, values=self.movie_data.get_movie_names(),
                                        textvariable=self.variable).grid(row=0, column=0)
        # Set Up Button
        self.__btn_submit = tkinter.Button(self.window, text="Submit", width=10,
                                           command=self.btn_submit_click).grid(row=0, column=1,
                                                                               sticky=tkinter.W, pady=10)
        # Set Up Movie Logo
        self.__image_path = self.__image_path = self.__image = self.__lbl_logo = ''
        self.display_logo_picture("../Images/placeholder.png")
        # Set Up Review label
        self.__lbl_review = tkinter.Label(self.window, text="Reviews", font=("Arial Bold", 10)
                                          ).grid(row=3, column=0)
        # Set up star Images
        self.__lbl_5stars = ''
        self.display_stars("../Images/5stars.png", self.__lbl_5stars, 4, 0)
        self.__lbl_4stars = ''
        self.display_stars("../Images/4stars.png", self.__lbl_4stars, 5, 0)
        self.__lbl_3stars = ''
        self.display_stars("../Images/3stars.png", self.__lbl_3stars, 6, 0)
        self.__lbl_2stars = ''
        self.display_stars("../Images/2stars.png", self.__lbl_2stars, 7, 0)
        self.__lbl_1stars = ''
        self.display_stars("../Images/1stars.png", self.__lbl_1stars, 8, 0)
        # Name Label
        self.text = tkinter.StringVar()
        self.text.set("")
        self.__lbl_name = tkinter.Label(self.window, textvariable=self.text,
                                        font=("Arial Bold", 15)).grid(row=1, column=1)
        # Rating Label
        self.__rating = tkinter.Label(self.window, text="Average Rating", font=("Arial Bold", 10)).grid(row=4, column=1)
        # Star Image
        self.__lbl_rating_stars = ''
        self.display_stars("../Images/3stars.png", self.__lbl_rating_stars, 5, 1)
        # Rating Value
        self.__avg_rating = tkinter.StringVar()
        self.__avg_rating.set("None")
        self.__lbl_avg_rating = tkinter.Label(self.window, textvariable=self.__avg_rating, font=("Arial Bold", 8)).grid(
            row=6, column=1)
        # Individual star ratings
        self.__star5 = tkinter.StringVar()
        self.__star5.set("(0)")
        self.__lbl_1star_rating = tkinter.Label(self.window, textvariable=self.__star5, font=("Arial Bold", 8)).grid(
            row=4, column=0, sticky=tkinter.E, padx=30)

        self.__star4 = tkinter.StringVar()
        self.__star4.set("(0)")
        self.__lbl_1star_rating = tkinter.Label(self.window, textvariable=self.__star4, font=("Arial Bold", 8)).grid(
            row=5, column=0, sticky=tkinter.E, padx=30)

        self.__star3 = tkinter.StringVar()
        self.__star3.set("(0)")
        self.__lbl_1star_rating = tkinter.Label(self.window, textvariable=self.__star3, font=("Arial Bold", 8)).grid(
            row=6, column=0, sticky=tkinter.E, padx=30)

        self.__star2 = tkinter.StringVar()
        self.__star2.set("(0)")
        self.__lbl_1star_rating = tkinter.Label(self.window, textvariable=self.__star2, font=("Arial Bold", 8)).grid(
            row=7, column=0, sticky=tkinter.E, padx=30)

        self.__star1 = tkinter.StringVar()
        self.__star1.set("(0)")
        self.__lbl_1star_rating = tkinter.Label(self.window, textvariable=self.__star1, font=("Arial Bold", 8)).grid(
            row=8, column=0, sticky=tkinter.E, padx=30)

        # Window Stays Open until closed
        self.window.mainloop()

    def option_callback(self, *args):
        print(self.variable.get())

    def btn_submit_click(self):
        # Get Text from Combo box
        movie_name = str(self.variable.get())
        # Look for Picture Online - look locally
        file_path = "../Images/" + movie_name
        if not os.path.exists(file_path):
            file_path = "../Images/error.png"
        self.display_logo_picture(file_path)
        # Look for Ratings
        avg_rating = self.movie_data.get_average_rating(movie_name)
        # Total number of ratings
        total_reviews = self.movie_data.get_total_number_of_reviews(movie_name)
        self.__avg_rating.set(str(avg_rating) + " ( " + str(total_reviews) + " )")
        # Update Stars
        print(self.load_stars(avg_rating))
        self.display_stars(self.load_stars(avg_rating), self.__lbl_avg_rating, 5, 1)
        # Set Name in the Label
        self.text.set(self.movie_data.format_name(movie_name))
        ratings = self.movie_data.get_number_of_x_ratings(movie_name, [0, 1, 2, 3, 4, 5])
        self.display_ratings(ratings)

    def load_stars(self, rating):
        path = '../Images/'
        switch = {0: '1stars.png', 1: '1stars.png', 2: '2stars.png', 3: '3stars.png', 4: '4stars.png', 5: '5stars.png'}
        path = path + switch.get(np.floor(rating))
        return path

    def display_logo_picture(self, string_path):
        self.__image_path = Image.open(string_path)
        self.__image_path = self.__image_path.resize((125, 150), Image.NONE)
        self.__image = ImageTk.PhotoImage(self.__image_path)
        self.__lbl_logo = tkinter.Label(self.window, image=self.__image)
        self.__lbl_logo.image = self.__image
        self.__lbl_logo.grid(row=1, column=0)

    def display_stars(self, string_path, label, r, c):
        path = Image.open(string_path)
        path = path.resize((100, 20), Image.NORMAL)
        img = ImageTk.PhotoImage(path)
        label = tkinter.Label(self.window, image=img)
        label.image = img
        label.grid(row=r, column=c)

    def display_ratings(self, ratings):
        self.__star5.set("(" + str(ratings[4]) + ")")
        self.__star4.set("(" + str(ratings[3]) + ")")
        self.__star3.set("(" + str(ratings[2]) + ")")
        self.__star2.set("(" + str(ratings[1]) + ")")
        self.__star1.set("(" + str(ratings[0]) + ")")


# ====================================END MoviesForm Class================================================


class MovieRecommendationForm:

    def __init__(self):
        window = tkinter.Tk()
        window.title("Movie Recommendations")
        window.geometry('400x400')
        window.rowconfigure([0, 1, 2, 3], minsize=50)
        window.columnconfigure([0, 1, 2], minsize=100)
        self.__lbl_intro = tkinter.Label(window, text='Movie Recommendation',
                                         font=("Arial Bold", 15)).grid(row=0, column=1)

# ====================================END MovieRecommendationForm Class================================================
