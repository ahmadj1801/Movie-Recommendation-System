import tkinter
import os
from tkinter.filedialog import askopenfilename

import numpy as np

from ML import Recommended
from Movies import MoviesData
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


# Window Position
def calculate_centre(window):
    position_right = position_down = 0
    win_width = window.winfo_reqwidth()
    win_height = window.winfo_reqheight()
    position_right = int(window.winfo_screenwidth() / 2 - win_width / 2)
    position_down = int(window.winfo_screenheight() / 2 - win_height / 2)
    return position_right, position_down


# Class For the Main Screen
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
        self.__btn_stats = tkinter.Button(window, text="Data Visualisation", width=20,
                                          command=self.btn_stats_click).grid(row=2, column=1)
        # Click to perform Machine Learning
        self.__btn_recommendation = tkinter.Button(window, text="Movie Recommendations", width=20,
                                                   command=self.btn_recommendation_click).grid(row=3, column=1)
        # Window Stays Open until closed
        window.mainloop()

    '''Callback Methods'''

    @staticmethod
    def btn_movies_click():
        # Open Movies Page
        movie_form = MoviesForm()

    @staticmethod
    def btn_stats_click():
        # Open Stats Page
        stats_form = StatisticsForm()

    @staticmethod
    def btn_recommendation_click():
        # Open Movie Recommendation Page
        recommendation_form = MovieRecommendationForm()


# ====================================END HomeForm Class================================================

# Class That Displays Graphs
class StatisticsForm:

    def __init__(self):
        # All Available Queries
        self.queries = ['View Highest Rated Movies', 'View Most Reviewed Movies',
                        'View Least Reviewed Movies', 'View Movies Released Per Year', 'View Movies Per Star Rating']
        # Top Level -> Displays on top
        self.window = tkinter.Toplevel()
        # Title
        self.window.title("Data Visualization")
        # Dimensions
        self.window.geometry('900x600')
        # Create a Data Object as part of the class
        self.movie_data = MoviesData()
        # Main Label
        self.__lbl_intro = tkinter.Label(self.window, text='Data Visualisation',
                                         font=("Arial Bold", 15)).place(x=375, y=10)
        # Combo Box Setup
        self.__drp_query = self.variable = tkinter.StringVar(self.window)
        self.variable.set("--Select--")
        self.variable.trace('w', self.option_callback)
        self.__drp_movie = ttk.Combobox(self.window, values=self.queries,
                                        textvariable=self.variable, width=30).place(x=350, y=60)
        self.__lbl_visual = self.img = self.image_path = ''
        # Default Image to be displayed -> On Creation
        self.display_image('../Images/data_vis.gif')
        # Run
        self.window.mainloop()

    # Call back Method on Combo Box
    def option_callback(self, *args):
        # Text of Option Chosen
        option = self.variable.get()
        # Index of Option Chosen
        option_number = self.queries.index(option)  # 0 to 4
        # Display Get Path to Graph
        if option_number == 0:
            path = self.movie_data.highest_rated_movies()
        elif option_number == 1:
            path = self.movie_data.most_reviewed_movies()
        elif option_number == 2:
            path = self.movie_data.least_reviewed_movies()
        elif option_number == 3:
            path = self.movie_data.movies_per_year()
        else:
            path = self.movie_data.movies_per_star_rating()
        # Display Graph
        self.display_image(path)

    # Display Appropriate Graph
    def display_image(self, string_path):
        self.image_path = Image.open(string_path)
        self.image_path = self.image_path.resize((700, 400), Image.NORMAL)
        self.img = ImageTk.PhotoImage(self.image_path)
        self.__lbl_visual = tkinter.Label(self.window, image=self.img)
        self.__lbl_visual.image = self.img
        self.__lbl_visual.place(x=100, y=100)


# ====================================END StatisticsForm Class================================================

# Class to Handle Viewing of Movies
class MoviesForm:

    def __init__(self):
        # Main Window
        self.window = tkinter.Toplevel()
        self.window.title("Movies")
        self.window.geometry('500x420')
        self.window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], minsize=20)
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
        self.upload_image = tkinter.Button(self.window, text='Upload', width=10, command=self.upload_image).grid(row=2, column=0)
        # Set Up Review label
        self.__lbl_review = tkinter.Label(self.window, text="Reviews", font=("Arial Bold", 10)
                                          ).grid(row=4, column=0)
        # Set up star Images
        self.__lbl_5stars = ''
        self.display_stars("../Images/5stars.png", self.__lbl_5stars, 5, 0)
        self.__lbl_4stars = ''
        self.display_stars("../Images/4stars.png", self.__lbl_4stars, 6, 0)
        self.__lbl_3stars = ''
        self.display_stars("../Images/3stars.png", self.__lbl_3stars, 7, 0)
        self.__lbl_2stars = ''
        self.display_stars("../Images/2stars.png", self.__lbl_2stars, 8, 0)
        self.__lbl_1stars = ''
        self.display_stars("../Images/1stars.png", self.__lbl_1stars, 9, 0)
        # Name Label
        self.text = tkinter.StringVar()
        self.text.set("")
        self.__lbl_name = tkinter.Label(self.window, textvariable=self.text,
                                        font=("Arial Bold", 15)).grid(row=1, column=1)
        # Rating Label
        self.__rating = tkinter.Label(self.window, text="Average Rating", font=("Arial Bold", 10)).grid(row=5, column=1)
        # Star Image
        self.__lbl_rating_stars = ''
        self.display_stars("../Images/3stars.png", self.__lbl_rating_stars, 6, 1)
        # Rating Value
        self.__avg_rating = tkinter.StringVar()
        self.__avg_rating.set("None")
        self.__lbl_avg_rating = tkinter.Label(self.window, textvariable=self.__avg_rating, font=("Arial Bold", 8)).grid(
            row=7, column=1)
        # Individual star ratings
        self.__star5 = tkinter.StringVar()
        self.__star5.set("(0)")
        self.__lbl_1star_rating = tkinter.Label(self.window, textvariable=self.__star5, font=("Arial Bold", 8)).grid(
            row=5, column=0, sticky=tkinter.E, padx=30)

        self.__star4 = tkinter.StringVar()
        self.__star4.set("(0)")
        self.__lbl_1star_rating = tkinter.Label(self.window, textvariable=self.__star4, font=("Arial Bold", 8)).grid(
            row=6, column=0, sticky=tkinter.E, padx=30)

        self.__star3 = tkinter.StringVar()
        self.__star3.set("(0)")
        self.__lbl_1star_rating = tkinter.Label(self.window, textvariable=self.__star3, font=("Arial Bold", 8)).grid(
            row=7, column=0, sticky=tkinter.E, padx=30)

        self.__star2 = tkinter.StringVar()
        self.__star2.set("(0)")
        self.__lbl_1star_rating = tkinter.Label(self.window, textvariable=self.__star2, font=("Arial Bold", 8)).grid(
            row=8, column=0, sticky=tkinter.E, padx=30)

        self.__star1 = tkinter.StringVar()
        self.__star1.set("(0)")
        self.__lbl_1star_rating = tkinter.Label(self.window, textvariable=self.__star1, font=("Arial Bold", 8)).grid(
            row=9, column=0, sticky=tkinter.E, padx=30)

        # Window Stays Open until closed
        self.window.mainloop()

    def upload_image(self):
        title = str(self.variable.get())
        title = self.movie_data.save_file_name(self.movie_data, title)
        print(title)
        tkinter.Tk().withdraw()
        file = askopenfilename(filetypes=[('image types', ('.png', '.jpg'))])
        print(file)

    # CallBack on Combo Box
    def option_callback(self, *args):
        self.variable.get()

    # Callback Method. Called When Button Clicked
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
        self.display_stars(self.load_stars(avg_rating), self.__lbl_avg_rating, 5, 1)
        # Set Name in the Label
        self.text.set(self.movie_data.format_name(movie_name))
        ratings = self.movie_data.get_number_of_x_ratings(movie_name, [0, 1.9, 2.9, 3.9, 4.9, 5])
        self.display_ratings(ratings)

    # Display the Average Rating Star Picture
    def load_stars(self, rating):
        path = '../Images/'
        switch = {0: '1stars.png', 1: '1stars.png', 2: '2stars.png', 3: '3stars.png', 4: '4stars.png', 5: '5stars.png'}
        # Choose Lower -> 3.6 displays 3 Stars
        path = path + switch.get(np.floor(rating))
        return path

    # Display Movie Logo
    def display_logo_picture(self, string_path):
        self.__image_path = Image.open(string_path)
        self.__image_path = self.__image_path.resize((125, 150), Image.NONE)
        self.__image = ImageTk.PhotoImage(self.__image_path)
        self.__lbl_logo = tkinter.Label(self.window, image=self.__image)
        self.__lbl_logo.image = self.__image
        self.__lbl_logo.grid(row=1, column=0)

    # Display Stars
    def display_stars(self, string_path, label, r, c):
        path = Image.open(string_path)
        path = path.resize((100, 20), Image.NORMAL)
        img = ImageTk.PhotoImage(path)
        label = tkinter.Label(self.window, image=img)
        label.image = img
        label.grid(row=r, column=c)

    # Display Textual Ratings - Per Star Level
    def display_ratings(self, ratings):
        self.__star5.set("(" + str(ratings[4]) + ")")
        self.__star4.set("(" + str(ratings[3]) + ")")
        self.__star3.set("(" + str(ratings[2]) + ")")
        self.__star2.set("(" + str(ratings[1]) + ")")
        self.__star1.set("(" + str(ratings[0]) + ")")


# ====================================END MoviesForm Class================================================

# A Class to Handle The Graphical Aspect of the Recommendation Form
class MovieRecommendationForm:

    def __init__(self):
        # Display on Top
        self.window = tkinter.Toplevel()
        # Title
        self.window.title("Movie Recommendations")
        self.window.geometry('650x550')
        # Movie Data Frames
        self.movie_data = MoviesData()
        # Main Heading
        self.__lbl_intro = tkinter.Label(self.window, text='Movie Recommendation',
                                         font=("Arial Bold", 15)).place(x=240, y=20)
        # Secondary Heading
        self.__lbl_my_recommendation = tkinter.Label(self.window, text='My Recommendations',
                                                     font=("Arial Bold", 15)).place(x=240, y=320)
        # Label Prompt
        self.__lbl_drp = tkinter.Label(self.window, text="Select a Movie:").place(x=10, y=70)
        # Label Prompt
        self.__lbl_sld = tkinter.Label(self.window, text="Enter a Rating:").place(x=10, y=130)
        # Confirm Button
        self.__btn_submit = tkinter.Button(self.window, text="Confirm Rating",
                                           command=self.btn_submit_click).place(x=145, y=180)
        # Recommend Button
        self.__btn_recommend = tkinter.Button(self.window, text="Recommend Me Movies",
                                              command=self.btn_recommend_click).place(x=122, y=220)
        # Set Up Drop Down Component
        self.variable = tkinter.StringVar(self.window)
        self.variable.set("--Select--")
        self.variable.trace('w', self.option_callback)
        self.__drp_movie = ttk.Combobox(self.window, values=self.movie_data.get_movie_names(),
                                        textvariable=self.variable, state='readonly')
        self.__drp_movie.place(x=120, y=70)
        self.__drp_movie.current(0)
        # Set Up Slider
        self.var = tkinter.DoubleVar()
        self.__slider = tkinter.Scale(self.window, from_=1, to=5, orient=tkinter.HORIZONTAL,
                                      tickinterval=1, length=140, variable=self.var).place(x=120, y=110)
        # Set up Watched List Box
        self.__lst_watched = tkinter.Listbox(self.window, width=50, height=12)
        self.__lst_watched.place(x=300, y=70)
        # Set Up Recommended List Box
        self.__lst_recommended = tkinter.Listbox(self.window, width=80, height=10)
        self.__lst_recommended.place(x=80, y=350)
        # Dictionary of Movies Watched and the Users Respective Ratings on Them
        self.watched = dict()

    # CallBack Method -> Submit Button
    def btn_submit_click(self):
        # Get the movie from the Combo Box
        movie_name = self.variable.get()
        # Get the Rating
        rating = self.var.get()
        # Add/Override if exists
        self.watched[movie_name] = rating
        full_string = movie_name + " " + str(rating)
        # Add to List
        self.__lst_watched.insert(tkinter.END, full_string)
        pass

    # Callback on Recommend Button
    def btn_recommend_click(self):
        # Check User has Rated Movies
        if self.__lst_watched.size() != 0:
            # Recommendation object
            ml = Recommended(self.watched)
            # recommend method on ml -> return array
            suggestions: [] = ml.get_recommendations
            # update recommend list box
            self.update_recommendations(suggestions)
        else:
            # Insufficient Ratings on inputted movies Error
            messagebox.showerror('Error', "Please Rate At Least ONE Movie!")

    # CallBack on Combo Box
    def option_callback(self, *args):
        self.variable.get()

    # Update List box
    def update_recommendations(self, suggestions):
        # Remove Existing Recommendations
        self.__lst_recommended.delete(0, tkinter.END)
        # Add to List Box
        for suggestion in suggestions:
            self.__lst_recommended.insert(tkinter.END, suggestion)

# ====================================END MovieRecommendationForm Class================================================
