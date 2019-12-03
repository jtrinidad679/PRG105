from tkinter import *
from PIL import ImageTk
import pickle


class WoW:
    def __init__(self, master):
        self.master = master
        self.master.title("World of Warcraft")
        master.geometry('1000x700')

        self.character_label = Label(master, text='Your Characters', font=("Helvetica", 30))
        self.character_label.place(anchor=NW)
        self.character_button = Button(master, text='Create New Character', font=("Helvetica", 26),
                                       fg='blue', command=self.faction_menu)
        self.quit_button = Button(master, text='Quit', font=("Helvetica", 26),
                                  fg='red', command=self.master.destroy)

        self.character_button.place(relx=0, rely=1, anchor=SW)
        self.quit_button.place(relx=1, rely=1, anchor=SE)

        canvas = Canvas(master, width=500, height=625)
        canvas.pack(side=RIGHT)
        image = ImageTk.PhotoImage(file='wowza.jpg')
        canvas.create_image(265, 200, image=image)
        master.mainloop()

    def faction_menu(master):
        faction_window = Tk.Toplevel(master)
        faction_window.title("Faction Selector")
        faction_window.geometry('1000x700')

        faction_description_label = Label(master,
                                               text='Before you step foot into Azeroth, you must select a faction.'
                                                    'The factions available to you are:', font=("Helvetica", 30))


def main():
    root = Tk()
    _ = WoW(root)
    root.mainloop()


main()
