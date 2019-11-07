import tkinter

# creating the class name


class MilesPerGallonConverter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # creating the main window and frames

        self.top_frame = tkinter.Frame()
        self.middle_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        self.last_frame = tkinter.Frame()

        # creating the gallons label and entry, then packing. then, creating the miles label
        # and entry and packing that as well

        self.gallons_label = tkinter.Label(self.top_frame, text='Enter how many gallons your car holds:')
        self.gallons_entry = tkinter.Entry(self.top_frame, width=10)

        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')

        self.miles_label = tkinter.Label(self.middle_frame, text='Enter how many miles have you traveled:')
        self.miles_entry = tkinter.Entry(self.middle_frame, width=10)

        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        self.description_label = tkinter.Label(self.bottom_frame, text='Converted to miles per gallons: ')

        self.value = tkinter.StringVar()
        self.converted_miles_label = tkinter.Label(self.bottom_frame, textvariable=self.value)

        self.description_label.pack(side='left')
        self.converted_miles_label.pack(side='left')

        # creating the buttons that will be used to convert the miles per gallon OR quit the program

        self.calc_button = tkinter.Button(self.last_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.last_frame, text='Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        self.last_frame.pack()

        tkinter.mainloop()

    # the function that will be used to convert the miles per gallon
    def convert(self):
        gallons = int(self.gallons_entry.get())
        miles = int(self.miles_entry.get())

        miles_per_gallon = miles / gallons
        self.value.set(format(miles_per_gallon, '.2f'))

# creating an instance of the class


miles_per_gallon_converter = MilesPerGallonConverter()
