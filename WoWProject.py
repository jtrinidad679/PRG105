from tkinter import *
from PIL import ImageTk
import pickle


class MainScreen:
    def __init__(self, master):
        self.master = master
        self.master.title('World of Warcraft')

        master.iconbitmap(r'wow_icon.png')

        master.geometry("2000x2000")

        canvas = Canvas(master, borderwidth=5)
        canvas.pack(side='right', fill=X)
        image = ImageTk.PhotoImage(file='wowpic.jpg')
        canvas.create_image(10, 10, image=image, anchor=NW)
        master.mainloop()

        self.character_frame = Frame(self.master)
        self.create_character_frame = Frame(self.master)
        self.quit_frame = Frame(self.master)

        self.value = IntVar()
        self.value.set(1)

        self.character_button = Button(canvas, self.create_character_frame, text='Create New Character', command=self.faction_menu)
        self.quit_button = Button(canvas, self.quit_frame, text='Quit', bg='black', fg='red', command=self.master.destroy)

        self.character_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.character_frame.pack()
        self.create_character_frame.pack()
        self.quit_frame.pack()

    def faction_menu(self):
        faction_window = Tk()
        faction_window.title("Faction Selector")


class Faction:
    def _init__(self, master):
        try:
            input_file = open("characters_file.dat", 'rb')
            self.characters = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.characters = []
        self.faction = Toplevel(master)
        self.faction.title('Faction Selector')

        self.faction_description_frame = Frame(self.faction)
        self.horde_frame = Frame(self.faction)
        self.alliance_frame = Frame(self.faction)

        self.description_label = Label(self.faction_description_frame, text='Before you step foot into Azeroth, you need to select a faction. \n'
                                                                                    'The factions available to you are: Alliance or Horde.')
        self.description_label.pack(side='left')

        self.alliance_button = Button(self.alliance_frame, text='Alliance', command=self.alliance)
        self.horde_button = Button(self.horde_frame, text='Horde', command=self.horde)

        self.faction_description_frame.pack()
        self.horde_frame.pack()
        self.alliance_frame.pack()


def main():
    root = Tk()
    _ = MainScreen(root)
    root.mainloop()


main()

# https://stackoverflow.com/questions/36575890/how-to-set-a-tkinter-window-to-a-constant-size


