import tkinter
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
        self.character_button = Button(master, text='Create New Character', font=("Helvetica", 30),
                                       fg='blue', command=self.faction_menu)
        self.quit_button = Button(master, text='Quit', font=("Helvetica", 30),
                                  fg='red', command=self.master.destroy)

        self.character_button.place(relx=0, rely=1, anchor=SW)
        self.quit_button.place(relx=1, rely=1, anchor=SE)

        canvas = Canvas(master, width=500, height=625)
        canvas.pack(side=RIGHT)
        image = ImageTk.PhotoImage(file='wowza.jpg')
        canvas.create_image(265, 200, image=image)
        master.mainloop()

    def faction_menu(self):
        _ = Faction(self.master)

    # def faction_menu(master):
    #     faction_window = Toplevel(master)
    #     faction_window.title("Faction Selector")
    #     faction_window.geometry('1000x700')

    # faction_description_label = Label(master,
    #                                        text='Before you step foot into Azeroth, you must select a faction.'
    #                                             'The factions available to you are:', font=("Helvetica", 30))


class Faction:
    def __init__(self, master):
        self.faction = Toplevel(master)
        self.faction.title("Faction Selector")
        self.faction.geometry('1000x700')

        self.description_frame = Frame(self.faction)
        # self.alliance_frame = Frame(self.faction)
        # self.horde_frame = Frame(self.faction)
        # self.alliance_frame = Frame(self.faction)
        # self.horde_frame = Frame(self.faction)

        self.faction_description_label = Label(self.description_frame,
                                               text='Before you step foot into Azeroth, you must select a faction.''\n'
                                                    'The factions available to you are:', font=("Helvetica", 30))

        self.alliance_label = Label(self.faction, text='The Alliance is one of two major political factions' '\n'
                                    'of the mortal races in Azeroth. Driven by tradition, the' '\n'
                                    'Alliance consists of powerful cultures and groups bound' '\n'
                                    'not by desperation or necessity but by their deep' '\n'
                                    'commitments to abstract concepts like nobility, honor,' '\n'
                                    'faith, justice, and sacrifice.', relief=SUNKEN, bg='white', fg='blue', font=("Helvetica", 16))

        self.alliance_label.place(relx=0.6, rely=0.6)

        canvas = Canvas(self.faction, width=200, height=200)
        canvas.place(relx=0.7, rely=0.2)
        image = ImageTk.PhotoImage(file='alliance.jpg')
        canvas.create_image(200, 500, image=image)
        image.place(relx=0.7, rely=0.2, anchor=NW)

        self.faction_description_label.pack()
        self.description_frame.pack()

        self.alliance_button = Button(self.faction, text='Alliance', command=self.alliance, font=("Helvetica", 30),
                                      fg='blue')
        self.horde_button = Button(self.faction, text='Horde', command=self.horde, font=("Helvetica", 30), fg='red')

        self.alliance_button.place(relx=0.74, rely=0.5)
        self.horde_button.place(relx=0.3, rely=0.5)
        # self.alliance_button.pack()
        # self.horde_button.pack()

        # self.alliance_frame.pack(side=LEFT)
        # self.horde_frame.pack(side=LEFT)
        self.faction.mainloop()
    def alliance(self):
        _ = Alliance(self.faction)

    def horde(self):
        _ = Horde(self.faction)


class Alliance:
    def __init__(self, master):
        self.alliance = Toplevel(master)
        self.alliance.title('Alliance')
        self.alliance.geometry('1000x700')

        self.radio_var = IntVar()
        self.radio_var.set(1)

        self.human = Radiobutton(self.alliance, text='Human', variable=self.radio_var, value=1, font=("Helvetica", 30))
        self.dwarf = Radiobutton(self.alliance, text='Dwarf', variable=self.radio_var, value=2, font=("Helvetica", 30))
        self.night_elf = Radiobutton(self.alliance, text='Night Elf', variable=self.radio_var, value=3,
                                     font=("Helvetica", 30))
        self.gnome = Radiobutton(self.alliance, text='Gnome', variable=self.radio_var, value=4, font=("Helvetica", 30))

        self.human.place(relx=0.3, rely=0.1)
        self.dwarf.place(relx=0.3, rely=0.3)
        self.night_elf.place(relx=0.3, rely=0.5)
        self.gnome.place(relx=0.3, rely=0.7)


class Horde:
    def __init__(self, master):
        self.horde = Toplevel(master)
        self.horde.title('Horde')
        self.horde.geometry('1000x700')


def main():
    root = Tk()
    _ = WoW(root)
    root.mainloop()


main()
