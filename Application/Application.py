import tkinter

# Create Window
window = tkinter.Tk()

# Window Title
window.title("Movie System")

# Window Size
window.geometry('500x200')
window.rowconfigure([0, 1, 2, 3], minsize=50)
window.columnconfigure([0, 1, 2], minsize=100)

# Place holder
placeholder = tkinter.Label(window, text=" ").grid(row=0, column=0)

# Heading
lbl_intro = tkinter.Label(window, text='Welcome to the Movie Recommendation System!',
                          font=("Arial Bold", 10)).grid(row=0, column=1)

# Click to View Movies in the Data Set
btn_movies = tkinter.Button(window, text="View Movies", width=20).grid(row=1, column=1)

# Click to View Data Analytics
btn_stats = tkinter.Button(window, text="View Data Analytics", width=20).grid(row=2, column=1)

# Click to perform Machine Learning
btn_recommendation = tkinter.Button(window, text="Movie Recommendations", width=20).grid(row=3, column=1)

# Window Stays Open until closed
window.mainloop()
