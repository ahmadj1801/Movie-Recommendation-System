import tkinter


class StatisticsForm:
    __lbl_intro = ''

    def __init__(self):
        window = tkinter.Tk()
        window.title("Data Visualization")
        window.geometry('400x400')
        window.rowconfigure([0, 1, 2, 3], minsize=100)
        window.columnconfigure([0, 1, 2, 3], minsize=100)
        self.__lbl_intro = tkinter.Label(window, text='Data Visualisation',
                                         font=("Arial Bold", 15)).grid(row=0, column=1)
