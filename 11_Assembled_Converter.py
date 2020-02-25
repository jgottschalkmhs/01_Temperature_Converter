from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Converter:
    def __init__(self):

        # Formatting variables...
        background_color = "green"

        # In actual program this is blank and is populated with user calculations
        self.all_calc_list = ['0 degree C is -17.8 degree F',
                              '1 degree C is -1 degree F',
                              '4 degree C is -0.8 degree F',
                              '47 degree C is -5478 degree F',
                              '47 degree C is -5478 degree F',
                              '47 degree C is -5478 degree F',
                              '64 degree C is -674 degree F',]

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

        # history Button (row 1)
        self.history_button = Button(self.converter_frame, text="History",
                                     font="arial 10 ",fg="blue",
                                     bg="black",padx=12, pady=12,
                                     command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1, pady=50)

    def history(self, calc_history):
        History(self, calc_history)

class History:
    def __init__(self, partner, calc_history):

        background = "green"

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Set up child window (ie: history box)
        self.history_box = Toplevel()

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, width=300, bg="yellow")
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame,
                                 text="Calculation History ",
                                 font="arial 20 bold",bg="dark green")
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame,
                               text="to much to write",
                               justify=LEFT,width=50, bg="orange",wrap=200)
        self.history_text.grid(column=0,row=1)

        # History output goes here...

        # Generate string from list of calculation...
        history_string = ""

        if len(calc_history) >= 7:
            for item in range(0,7):
                history_string += calc_history[len(calc_history)
                                                - item - 1]+"\n"


        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history)-
                                               calc_history.index(item)-1] + "\n"
                self.history_text.config(text="here is your calculation "
                                         "history. You can use the "
                                         "export buttom to save this"
                                         "data to a text file if "
                                         "desired.")

        # Lable to display calculation history to user
        self.calc_history = Label(self.history_frame, text=history_string,
                                  bg=background, font="arial 12", justify=LEFT)
        self.calc_history.grid(row=2)

        # Export / dismiss Button Frame
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="export",
                                    font="arial 12 bold")
        self.export_button.grid(row=0, column=0)

        # dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="export",
                                    font="arial 12 bold")
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        # Put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("temp con")
    something = Converter()
    root.mainloop()
