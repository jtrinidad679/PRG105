from tkinter import *
from PIL import ImageTk
import pickle


class WoW:
    def __init__(self, master):
        self.master = master
        self.master.title("World of Warcraft")

        master.geometry('1000x700')

        self.character_frame = Frame(self.master).grid(row=0, sticky=W)
        self.create_character_frame = Frame(self.master).grid(row=3, sticky=W)
        self.quit_frame = Frame(self.master).grid(row=4, sticky=W)
        self.image_frame = Frame(self.master).grid(row=5, sticky=W)

        self.character_label = Label(self.character_frame, text='Your Characters', font=("Helvetica", 30)).grid(row=0,
                                                                                                                sticky=W)

        self.character_button = Button(self.create_character_frame, text='Create New Character', font=("Helvetica", 26),
                                       command=self.faction_menu).grid(row=3, sticky=W)
        self.quit_button = Button(self.quit_frame, text='Quit', font=("Helvetica", 26),
                                  command=self.master.destroy).grid(row=4, sticky=W)

    def faction_menu(self):
        faction_window = Tk()
        faction_window.title("Faction Selector")
        faction_window.geometry('1000x700')


def main():
    root = Tk()
    _ = WoW(root)
    root.mainloop()


main()
