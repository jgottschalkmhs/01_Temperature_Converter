from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Converter:
    def __init__(self):

        # Formatting variables...
        background_color = "green"

        # Converter MAin Screen GUT...
        self.converter_frame = Frame (width=600 , height=500, bg=background_color)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("arial 20 bold"),
                                          fg="red",bg=background_color,
                                          padx=50, pady=80)

        self.temp_converter_label.grid(row=0)

        # Help Button (row 1)
        self.help_button = Button(self.converter_frame,
                                  text="help",font="arial 20 bold",fg="blue",
                                  bg="black",padx=12, pady=12,command=self.help,)
        self.help_button.grid(row=1, pady=50)

    def help(self):
        print("you need help")
        get_help = Help(self)
        get_help.help_text.configure(text="you fix it by getting of my app")

class Help:
    def __init__(self, partner):
        background = "pink"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Set up child window (ie: help box)
        self.help_box = Toplevel(1)

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg="yellow")
        self.help_frame.grid()
        # Set up help heading (row 0)
        self.how_heading = Label(self.help_frame,
                                 text="help / instruction",
                                 font="arial 20 bold",bg="dark green")
        self.how_heading.grid(row=0)
        # Help text (label, row 1)
        self.help_text = Label(self.help_frame,
                               text="i have no idea where this is going to be",
                               justify=LEFT,width=50, bg="orange",wrap=200)
        self.help_text.grid(column=0,row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame,text="Dismiss",width=10,bg="red",
                                  font="arial 20 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("temp con")
    something = Converter()
    root.mainloop()
