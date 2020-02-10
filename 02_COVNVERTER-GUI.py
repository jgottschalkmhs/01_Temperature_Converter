from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Converter:
    def __init__(self):

        # Formatting variables...
        background_color = "light blue"

        # Converter Frame
        self.converter_frame = Frame (width=600 , bg=background_color, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("arial 20 bold"),
                                          fg="red",bg=background_color,
                                          padx=50, pady=80)

        self.temp_converter_label.grid(row=0)

        # User instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="this is not placeholder \n"
                                                  "this might be a placeholder\n"
                                                  "this is a placeholder\n",
                                             font="arial 20 italic", wrap=350,
                                             justify=LEFT)
        self.temp_instructions_label.grid(row=1)

        # temperture entry box (row2)
        self.to_convert_entry = Entry(self.converter_frame,width=50,
                                      font=("arial 20 bold"))
        self.to_convert_entry.grid(row=2)

        # conversion buttons frame (row 3) ,orchid3 | khakil
        self.converter_buttons_frame = Frame(self.converter_frame)
        self.converter_buttons_frame.grid(rows=3, pady=30)

        self.to_c_button = Button(self.converter_buttons_frame,
                                  text = "To Centigrade",
                                  font = ("arial 20 bold"),
                                  fg = "red", bg = "khaki",
                                  padx = 10, pady = 10)
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.converter_buttons_frame,
                                  text="To Fahreneit", font="Arial 20 bold",
                                  bg="orchid", padx=10, pady=10)
        self.to_f_button.grid(row=0, column=1)

        # Answer label (row 4)
        self.Answer_buttons_frame = Frame(self.converter_frame)
        self.Answer_buttons_frame.grid(rows=3, pady=50, padx=60)

        self.Answer_buttons = Button (self.converter_frame,
                                      text="Answer", font="Arial 20 bold",
                                      bg="pink", padx=10, pady=10)
        self.Answer_buttons.grid(row=6)

        # History / Help button frame (row 5)
        self.History_buttons_frame = Frame(self.converter_frame)
        self.History_buttons_frame.grid(rows=3, pady=10, padx=10)

        self.History_buttons = Button(self.converter_frame,
                                     text="History", font="Arial 20 bold",
                                     bg="purple", padx=10, pady=10)
        self.History_buttons.grid(row=6)



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("temp con")
    something = Converter()
    root.mainloop()