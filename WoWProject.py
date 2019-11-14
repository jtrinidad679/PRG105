import tkinter
import tkinter.messagebox


class MainScreen:
    def __init__(self, master):
        self.master = master
        self.master.title('World of Warcraft')

        master.geometry("2000x2000")

        self.character_frame = tkinter.Frame(self.master)
        self.create_character_frame = tkinter.Frame(self.master)
        self.quit_frame = tkinter.Frame(self.master)

        self.value = tkinter.IntVar()
        self.value.set(1)

        self.character_button = tkinter.Button(self.create_character_frame, text='Create New Character', variable=self.value, value=1, command=self.faction_menu)
        self.quit_button = tkinter.Button(self.quit_frame, text='Quit', bg='black', fg='red', command=self.master.destroy)

        self.character_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.character_frame.pack()
        self.create_character_frame.pack()
        self.quit_frame.pack()

    def faction_menu(self):
        if self.value.get() == 1:
            _ = Faction()


class Faction:
    def _init__(self, master):
        self.faction = tkinter.Toplevel(master)
        self.faction.title('Faction Selector')

        self.faction_description_frame = tkinter.Frame(self.faction)
        self.horde_frame = tkinter.Frame(self.faction)
        self.alliance_frame = tkinter.Frame(self.faction)

        self.description_label = tkinter.Label(self.faction_description_frame, text='Before you step foot into Azeroth, you need to select a faction. \n'
                                                                                    'The factions available to you are: Alliance or Horde.')
        self.description_label.pack(side='left')

        self.alliance_button = tkinter.Button(self.alliance_frame, text='Alliance', command=self.alliance)
        self.horde_button = tkinter.Button(self.horde_frame, text='Horde', command=self.horde)

        self.faction_description_frame.pack()
        self.horde_frame.pack()
        self.alliance_frame.pack()


def main():
    root = tkinter.Tk()
    _ = MainScreen(root)
    root.mainloop()


main()

# https://stackoverflow.com/questions/36575890/how-to-set-a-tkinter-window-to-a-constant-size
