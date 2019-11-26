import tkinter
# A system that allows you to buy a book from a genre of
# your choice and then receive a random book from that genre


class Book:
    def __init__(self):
        self.main_window = tkinter.Tk()
        # Creating all of the wonderful book-ish frames
        self.book_frame = tkinter.Frame(self.main_window)
        self.type_frame = tkinter.Frame(self.main_window)
        self.extras_frame = tkinter.Frame(self.main_window)
        self.order_frame = tkinter.Frame(self.main_window)
        self.charges_frame = tkinter.Frame(self.main_window)

        self.book_var = tkinter.IntVar()
        self.type_var = tkinter.IntVar()

        self.book_var.set(1)
        self.type_var.set(1)

        # Creating the book label and the different genres available
        # I would've chose more but these are my top 3 favorite genres so :)
        self.book_label = tkinter.Label(self.book_frame, text="Books")
        self.book1 = tkinter.Radiobutton(self.book_frame, text="Young Adult", variable=self.book_var, value=1)
        self.book2 = tkinter.Radiobutton(self.book_frame, text="Fantasy", variable=self.book_var, value=2)
        self.book3 = tkinter.Radiobutton(self.book_frame, text="Historical Fiction", variable=self.book_var, value=3)

        # Packing everything 
        self.book_label.pack()
        self.book1.pack(side='left')
        self.book2.pack(side='left')
        self.book3.pack(side='left')

        # Creating the type label and the different types of books, because there's a lot!
        self.type_label = tkinter.Label(self.type_frame, text="Type of Book")
        self.type1 = tkinter.Radiobutton(self.type_frame, text="E-Book - $5.00", variable=self.type_var, value=1)
        self.type2 = tkinter.Radiobutton(self.type_frame, text="Audio-Book - $8.00", variable=self.type_var, value=2)
        self.type3 = tkinter.Radiobutton(self.type_frame, text="Paperback - $10.00", variable=self.type_var, value=3)
        self.type4 = tkinter.Radiobutton(self.type_frame, text="Hardcover - $15.00", variable=self.type_var, value=4)

        # Packing everything
        self.type_label.pack()
        self.type1.pack(side='left')
        self.type2.pack(side='left')
        self.type3.pack(side='left')
        self.type4.pack(side='left')

        self.autograph_var = tkinter.IntVar()
        self.bookmark_var = tkinter.IntVar()
        self.character_map_var = tkinter.IntVar()

        self.autograph_var.set(0)
        self.bookmark_var.set(0)
        self.character_map_var.set(0)

        # Creating the extras label and the extra goodies you can receive with you purchase
        # Too bad this isn't a real thing with most companies
        self.extras_label = tkinter.Label(self.extras_frame, text="Extra Book Goodies")
        self.autograph = tkinter.Checkbutton(self.extras_frame, text="Autograph", variable=self.autograph_var)
        self.bookmark = tkinter.Checkbutton(self.extras_frame, text="Bookmark", variable=self.bookmark_var)
        self.character_map = tkinter.Checkbutton(self.extras_frame, text="Character Map", variable=self.character_map_var)

        # More packing
        self.extras_label.pack()
        self.autograph.pack(side='left')
        self.bookmark.pack(side='left')
        self.character_map.pack(side='left')

        # Creating buttons that do things!
        self.order_button = tkinter.Button(self.order_frame, text="Order", command=self.display)
        self.quit_button = tkinter.Button(self.order_frame, text="Quit", command=self.main_window.destroy)

        # Packing buttons
        self.order_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Packing all the wonderful book-ish frames
        self.book_frame.pack()
        self.type_frame.pack()
        self.extras_frame.pack()
        self.order_frame.pack()
        self.charges_frame.pack()

        self.order_info = tkinter.StringVar()
        self.order_output = tkinter.Label(self.charges_frame, textvariable=self.order_info)
        self.order_output.pack()

        # Gotta do this otherwise it wont work
        tkinter.mainloop()

    def display(self):
        # Ordering information station
        output = "You ordered "
        if self.type_var.get() == 1:
            output += "an e-book"
        elif self.type_var.get() == 2:
            output += "an audio-book"
        elif self.type_var.get() == 3:
            output += "a paperback"
        elif self.type_var.get() == 4:
            output += "a hardcover"

        if self.book_var.get() == 1:
            output += " Young Adult novel"
        elif self.book_var.get() == 2:
            output += " Fantasy novel"
        elif self.book_var.get() == 3:
            output += " Historical Fiction novel"

        if self.type_var.get() == 1:
            output += " for $5.00"
        elif self.type_var.get() == 2:
            output += " for $8.00"
        elif self.type_var.get() == 3:
            output += " for $10.00"
        elif self.type_var.get() == 4:
            output += " for $15.00"

        if self.autograph_var.get() == 1:
            output += "\nwith an autograph!"
        if self.bookmark_var.get() == 1:
            output += "\nwith a bookmark!"
        if self.character_map_var.get() == 1:
            output += "\nwith a character map!"

        self.order_info.set(output)

# Calling the instance


book_order = Book()
