import tkinter

# Create Window
window = tkinter.Tk()
# Window Title
window.title("Movie System")
# Window Size
window.geometry('350x350')
lbl_intro = tkinter.Label(window, text='Welcome '
                                       'to the Movie Recommendation System!',
                          font=("Arial Bold", 10)).grid(column=1, row=1)
window.mainloop()
