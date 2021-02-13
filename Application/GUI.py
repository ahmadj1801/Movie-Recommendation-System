import tkinter
from tkinter import ttk

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
        self.window = tkinter.Tk()
        self.window.title("Movies")
        self.window.geometry('400x400')
        self.window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], minsize=50)
        self.window.columnconfigure([0, 1, 2], minsize=100)
        movie_data = MoviesData()
        self.__drp_movie = ttk.Combobox(self.window, values=movie_data.get_movie_names()).grid(row=0, column=1)
        self.__btn_submit = tkinter.Button(self.window, text="Submit", width=10,
                                           command=self.btn_submit_click).grid(row=0, column=2)

    def btn_submit_click(self):
        # Get Text from Combo box
        # Look for Picture Online
        # Look for Ratings
        # Set Name in the Label
        pass

    def populate_combobox(self):
        pass


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
