from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Converter:
    def __init__(self):

        # Formatting variables...
        background_color = "#52ACD1"

        # Initialise list to hold calculation history
        self.all_calc_list = []

        # Converter Frame
        self.converter_frame = Frame (bg=background_color, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("arial 20 bold"),
                                          fg="Black", bg=background_color,
                                          padx=50, pady=20)

        self.temp_converter_label.grid(row=0)

        # User instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be \n"
                                                  "converted and then push \n"
                                                  "one of the buttons below.\n",
                                             font="arial 15 italic", wrap=250,bg=background_color,
                                             fg="Black",justify=LEFT)
        self.temp_instructions_label.grid(row=1)

        # temperture entry box (row2)
        self.to_convert_entry = Entry(self.converter_frame,width=30,
                                      font= ("arial 15 bold"))
        self.to_convert_entry.grid(row=2)

        # conversion buttons frame (row 3) ,orchid3 | khakil
        self.converter_buttons_frame = Frame(self.converter_frame)
        self.converter_buttons_frame.grid(row=3, pady=30)

        self.to_c_button = Button(self.converter_buttons_frame,
                                  text = " To Centigrade ",
                                  font = ( " arial 10 bold " ),
                                  bg="#4D8889", fg="#F7FBFD",
                                  padx = 10, pady = 10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.converter_buttons_frame,
                                  text="To Fahreneit", font="Arial 10 bold",
                                  bg="#4D8889", fg="#F7FBFD", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        # Answer label (row 4)

        self.converted_label = Label (self.converter_frame,
                                      text="Answer", font="Arial 10 bold",
                                      bg=background_color, padx=10, pady=10)
        self.converted_label.grid(row=4)

        # history / Help button frame (row 5)
        self.history_buttons_frame = Frame(self.converter_frame)
        self.history_buttons_frame.grid(rows=5, pady=10, padx=10)

        # history button
        self.history_buttons = Button(self.history_buttons_frame,
                                      text="history", font="Arial 10 bold",
                                      command=lambda: self.history(self.all_calc_list),
                                      bg="#4D8889",fg="#F7FBFD", padx=10, pady=10)
        self.history_buttons.grid(row=0, column=0)

        if len(self.all_calc_list) == 0:
            self.history_buttons.config(state=DISABLED)

        # Help Button
        self.help_button = Button(self.history_buttons_frame,
                                  text="help",font="arial 10 bold",bg="#4D8889",
                                  fg="#F7FBFD",padx=10, pady=10, command=self.help)
        self.help_button.grid(row=0, column=1)

    def help(self):
        print("you need help")
        get_help = Help(self)
        get_help.help_text.configure(text="you fix it by getting off my app")

    def temp_convert(self, low):
        print(low)

        error = "#ffafaf" # pale pink when a error

        # Retrieve amount entered into Entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_error = "no"

            # convert to F
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degrees C if {} degree F".format(to_convert, fahrenheit)

            # convert to C
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degrees C if {} degree F".format(to_convert, celsius)

            else:
                # input is invalid
                answer = "Too cold"
                has_error = "yes"

            # Display answer
            if has_error == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)

            # Add Answer to list for history
            if has_error != "yes":
                self.all_calc_list.append(answer)
                self.history_buttons.config(state=NORMAL)

        except ValueError:
            self.converted_label.configure(text="enter a number", fg="red")
            self.to_convert_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)
        return rounded

    def history(self, calc_history):
        History(self, calc_history)


class Help:
    def __init__(self, partner):

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Set up child window (ie: help box)
        self.help_box = Toplevel()

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg="#52ACD1")
        self.help_frame.grid()
        # Set up help heading (row 0)
        self.how_heading = Label(self.help_frame,
                             text="Help / Instruction",
                             font="arial 20 bold", bg="#52ACD1")
        self.how_heading.grid(row=0)
        # Help text (label, row 1)
        self.help_text = Label(self.help_frame,
                           text="i have no idea where this is going to be",
                           justify=LEFT, width=50, bg="#52ACD1", wrap=200)
        self.help_text.grid(column=0, row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="#4D8889",
                              font="arial 10 bold", fg="#F7FBFD",
                              command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


class History:
    def __init__(self, partner, calc_history):

        background = "#52ACD1"

        # disable history button
        partner.history_buttons.config(state=DISABLED)

        # Set up child window (ie: history box)
        self.history_box = Toplevel()

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, width=300, bg="#52ACD1")
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame,
                                 text="Calculation history ",
                                 font="arial 20 bold",bg="#52ACD1")
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame,
                               text="to much to write",
                               justify=LEFT,width=50, bg="#52ACD1",wrap=200)
        self.history_text.grid(column=0,row=1)

        # history output goes here...

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
                self.history_text.config(text="Here is your calculation "
                                         "history. You can use the "
                                         "export button to save this "
                                         "data to a text file if "
                                         "desired.",  font="arial 12 italic")

        # Lable to display calculation history to user
        self.calc_history = Label(self.history_frame, text=history_string,
                                  bg=background, font="arial 12 bold", justify=LEFT)
        self.calc_history.grid(row=2)

        # Export / dismiss Button Frame
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="export",
                                    font="arial 12 bold",bg="#4D8889", fg="#F7FBFD",)
        self.export_button.grid(row=0, column=0)

        # dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                    font="arial 12 bold",bg="#4D8889", fg="#F7FBFD",
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        # Put history button back to normal
        partner.history_buttons.config(state=NORMAL)
        self.history_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("temp con")
    something = Converter()
    root.mainloop()
