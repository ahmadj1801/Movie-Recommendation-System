import tkinter


class HomeForm:
    # Private Class attributes
    __lbl_intro = __btn_movies = __btn_stats = __btn_recommendation = ''

    def __init__(self):
        # Create Window
        window = tkinter.Tk()
        # Window Title
        window.title("Movie System")
        # Window Size
        window.geometry('500x200')
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
        window.columnconfigure([0, 1, 2, 3], minsize=100)
        self.__lbl_intro = tkinter.Label(window, text='Data Visualisation',
                                         font=("Arial Bold", 15)).grid(row=0, column=1)


# ====================================END HomeForm Class================================================

class MoviesForm:

    def __init__(self):
        window = tkinter.Tk()
        window.title("Movies")
        window.geometry('400x400')
        window.rowconfigure([0, 1, 2, 3], minsize=100)
        window.columnconfigure([0, 1, 2, 3], minsize=100)
        self.__lbl_intro = tkinter.Label(window, text='Movies',
                                         font=("Arial Bold", 15)).grid(row=0, column=1)


# ====================================END MoviesForm Class================================================


class MovieRecommendationForm:

    def __init__(self):
        window = tkinter.Tk()
        window.title("Movie Recommendations")
        window.geometry('400x400')
        window.rowconfigure([0, 1, 2, 3], minsize=100)
        window.columnconfigure([0, 1, 2, 3], minsize=100)
        self.__lbl_intro = tkinter.Label(window, text='Movie Recommendation',
                                         font=("Arial Bold", 15)).grid(row=0, column=1)


# ====================================END MovieRecommendationForm Class================================================
