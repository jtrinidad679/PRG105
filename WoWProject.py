from tkinter import *
from PIL import ImageTk


class WoW:
    def __init__(self, master):
        # Creating the first window with a title and setting it to my desired window size.
        self.master = master
        self.master.title("World of Warcraft")
        master.geometry('1000x700')

        # Here we are trying to open the text file that holds the character information.
        # Then, it will display the information we gathered from the save function in the main window.
        # If the file cannot be found it will print the except statement.
        try:
            characters_file = open('characters.txt', 'r')
            file_contents = characters_file.read()
            characters_file.close()
            self.file_contents = Label(master, text=file_contents, font=("Helvetica", 28))
            self.file_contents.place(relx=0, rely=0.1)
        except FileNotFoundError:
            print("You don't have any characters yet. Try making one!")

        # Creating labels and buttons and placing them in my desired locations.
        self.character_label = Label(master, text='Your Characters', fg='blue', font=("Helvetica", 30))
        self.character_label.place(anchor=NW)
        self.character_button = Button(master, text='Create New Character', font=("Helvetica", 30),
                                       fg='blue', command=self.faction_menu)
        self.quit_button = Button(master, text='Quit', font=("Helvetica", 30),
                                  fg='red', command=self.master.destroy)

        self.character_button.place(relx=0, rely=1, anchor=SW)
        self.quit_button.place(relx=1, rely=1, anchor=SE)

        # Using the canvas widget to insert an image of Ragnaros on the main screen.
        canvas = Canvas(master, width=500, height=600)
        canvas.pack(side=RIGHT)
        image = ImageTk.PhotoImage(file='wowza.jpg')
        canvas.create_image(265, 325, image=image)
        master.mainloop()

        # The character_button once clicked will open up a new window titled: Faction Selector.
    def faction_menu(self):
        _ = Faction(self.master)


class Faction:
    def __init__(self, master):
        self.faction = Toplevel(master)
        self.faction.title("Faction Selector")
        self.faction.geometry('1000x700')

        self.description_frame = Frame(self.faction)

        # Creating labels that give the user information about the factions they will be creating characters for.
        self.faction_description_label = Label(self.description_frame,
                                               text='Before you step foot into Azeroth, you must select a faction.''\n'
                                                    'The factions available to you are:', font=("Helvetica", 30))

        self.alliance_label = Label(self.faction, text='Driven by tradition, the Alliance consists of powerful' '\n'
                                                       'cultures and groups bound by their deep commitments' '\n'
                                                       'to abstract concepts like nobility, honor, faith, justice,' '\n'
                                                       'and sacrifice. Striving to represent these high ideals, its' '\n'
                                                       'many different peoples all contribute their technical,' '\n'
                                                       'arcane, and spiritual wisdom towards their shared goal' '\n'
                                                       'of preserving order on Azeroth and creating a' '\n'
                                                       'peaceful and just world.', relief=SUNKEN, bg='white', fg='blue', font=("Helvetica", 16))

        self.horde_label = Label(self.faction, text='A faction led by off-worlders and composed of' '\n'
                                                    'outsiders, the Horde has survived the obstacles of Azeroth by' '\n'
                                                    'bonding together and fighting as family, comrades, or even' '\n'
                                                    'uneasy allies. Driven by unity, the Horde consists of a coalition' '\n'
                                                    'of disparate races and cultures loosely joined in an alliance' '\n'
                                                    'of convenience against a hostile world that would' '\n'
                                                    'see them destroyed.', relief=SUNKEN, bg='white', fg='red',
                                 font=("Helvetica", 16))

        # Placing the labels.
        self.alliance_label.place(relx=0.6, rely=0.7)
        self.horde_label.place(relx=0.02, rely=0.7)

        # Using canvas again to insert 2 separate pictures that display the Horde and Alliance logos.
        canvas = Canvas(self.faction, width=300, height=300)
        canvas.place(relx=0.63, rely=0.13)
        image = ImageTk.PhotoImage(file='alliance.jpg')
        canvas.create_image(165, 160, image=image)
        image.place(relx=0.63, rely=0.13, anchor=NW)

        canvas2 = Canvas(self.faction, width=300, height=300)
        canvas2.place(relx=0.06, rely=0.13)
        image2 = ImageTk.PhotoImage(file='horde.jpg')
        canvas2.create_image(158, 150, image=image2)
        image2.place(relx=0.06, rely=0.13, anchor=NW)

        # Packing the label and frame.
        self.faction_description_label.pack()
        self.description_frame.pack()

        # Creating the buttons and placing them.
        self.alliance_button = Button(self.faction, text='Alliance', command=self.alliance, font=("Helvetica", 30),
                                      fg='blue')
        self.horde_button = Button(self.faction, text='Horde', command=self.horde, font=("Helvetica", 30), fg='red')

        self.alliance_button.place(relx=0.74, rely=0.6)
        self.horde_button.place(relx=0.17, rely=0.6)

        self.faction.mainloop()

    # Each button once clicked will open a new window for the faction you select.
    def alliance(self):
        _ = Alliance(self.faction)

    def horde(self):
        _ = Horde(self.faction)


class Alliance:
    def __init__(self, master):
        self.alliance = Toplevel(master)
        self.alliance.title('Alliance')
        self.alliance.geometry('1000x700')

        self.alliance_label = Label(self.alliance, text='Alliance Races', fg='blue', font=("Helvetica", 30))
        self.alliance_class_label = Label(self.alliance, text='Classes', fg='blue', font=("Helvetica", 30))
        self.alliance_label.place(relx=0.06, rely=0)
        self.alliance_class_label.place(relx=0.6, rely=0)

        # Creating radio buttons.
        # One set of radio buttons follows the radio variable, and the other set follows the class variable.
        # We have two separate radio buttons with different functions. One that selects your desired race,
        # and one that selects your desired class.
        self.radio_var = IntVar()
        self.radio_var.set(1)

        self.human = Radiobutton(self.alliance, text='Human', variable=self.radio_var, value=1, font=("Helvetica", 30))
        self.dwarf = Radiobutton(self.alliance, text='Dwarf', variable=self.radio_var, value=2, font=("Helvetica", 30))
        self.night_elf = Radiobutton(self.alliance, text='Night Elf', variable=self.radio_var, value=3,
                                     font=("Helvetica", 30))
        self.gnome = Radiobutton(self.alliance, text='Gnome', variable=self.radio_var, value=4, font=("Helvetica", 30))

        self.class_var = IntVar()
        self.class_var.set(1)

        self.warrior = Radiobutton(self.alliance, text='Warrior', variable=self.class_var, value=1,
                                   font=("Helvetica", 30))
        self.hunter = Radiobutton(self.alliance, text='Hunter', variable=self.class_var, value=2,
                                  font=("Helvetica", 30))
        self.rogue = Radiobutton(self.alliance, text='Rogue', variable=self.class_var, value=3, font=("Helvetica", 30))
        self.priest = Radiobutton(self.alliance, text='Priest', variable=self.class_var, value=4,
                                  font=("Helvetica", 30))
        self.mage = Radiobutton(self.alliance, text='Mage', variable=self.class_var, value=5, font=("Helvetica", 30))
        self.warlock = Radiobutton(self.alliance, text='Warlock', variable=self.class_var, value=6,
                                   font=("Helvetica", 30))
        self.druid = Radiobutton(self.alliance, text='Druid', variable=self.class_var, value=7, font=("Helvetica", 30))

        # Lots of placing stuff.
        self.human.place(relx=0.1, rely=0.1)
        self.dwarf.place(relx=0.1, rely=0.2)
        self.night_elf.place(relx=0.1, rely=0.3)
        self.gnome.place(relx=0.1, rely=0.4)

        self.warrior.place(relx=0.6, rely=0.1)
        self.hunter.place(relx=0.6, rely=0.2)
        self.rogue.place(relx=0.6, rely=0.3)
        self.priest.place(relx=0.6, rely=0.4)
        self.mage.place(relx=0.6, rely=0.5)
        self.warlock.place(relx=0.6, rely=0.6)
        self.druid.place(relx=0.6, rely=0.7)

        # Creating a label that prompts the user to enter their desired character name in the entry box.
        self.name_label = Label(self.alliance, text='Enter Name: ', font=("Helvetica", 30))
        self.name_entry = Entry(self.alliance, width=20)

        self.name_label.place(relx=0.1, rely=0.89)
        self.name_entry.place(relx=0.3, rely=0.9)

        # Creating the Enter World button.
        self.world_button = Button(self.alliance, text='Enter World', command=self.save, font=("Helvetica", 30))

        self.world_button.place(relx=0.8, rely=0.89)

    def save(self):
        # The Enter World button when clicked will open the text file, gather the information the user has
        # entered or selected and then close the file again.
        characters_file = open('characters.txt', 'w')
        character_name = self.name_entry.get()
        characters_file.write(character_name + " - ")

        if self.radio_var.get() == 1:
            characters_file.write("Human")
        elif self.radio_var.get() == 2:
            characters_file.write("Dwarf")
        elif self.radio_var.get() == 3:
            characters_file.write("Night Elf")
        elif self.radio_var.get() == 4:
            characters_file.write("Gnome")

        if self.class_var.get() == 1:
            characters_file.write(" Warrior")
        elif self.class_var.get() == 2:
            characters_file.write(" Hunter")
        elif self.class_var.get() == 3:
            characters_file.write(" Rogue")
        elif self.class_var.get() == 4:
            characters_file.write(" Priest")
        elif self.class_var.get() == 5:
            characters_file.write(" Mage")
        elif self.class_var.get() == 6:
            characters_file.write(" Warlock")
        elif self.class_var.get() == 7:
            characters_file.write(" Druid")

        characters_file.close()


class Horde:
    def __init__(self, master):
        self.horde = Toplevel(master)
        self.horde.title('Horde')
        self.horde.geometry('1000x700')

        self.horde_label = Label(self.horde, text='Races', fg='red', font=("Helvetica", 30))
        self.horde_class_label = Label(self.horde, text='Classes', fg='red', font=("Helvetica", 30))

        self.horde_label.place(relx=0.1, rely=0)
        self.horde_class_label.place(relx=0.6, rely=0)

        # Creating radio buttons.
        # One set of radio buttons follows the radio variable, and the other set follows the class variable.
        # We have two separate radio buttons with different functions. One that selects your desired race,
        # and one that selects your desired class.
        self.radio_var = IntVar()
        self.radio_var.set(1)

        self.orc = Radiobutton(self.horde, text='Orc', variable=self.radio_var, value=1, font=("Helvetica", 30))
        self.undead = Radiobutton(self.horde, text='Undead', variable=self.radio_var, value=2, font=("Helvetica", 30))
        self.tauren = Radiobutton(self.horde, text='Tauren', variable=self.radio_var, value=3,
                                  font=("Helvetica", 30))
        self.troll = Radiobutton(self.horde, text='Troll', variable=self.radio_var, value=4, font=("Helvetica", 30))

        self.class_var = IntVar()
        self.class_var.set(1)

        self.warrior = Radiobutton(self.horde, text='Warrior', variable=self.class_var, value=1, font=("Helvetica", 30))
        self.hunter = Radiobutton(self.horde, text='Hunter', variable=self.class_var, value=2, font=("Helvetica", 30))
        self.rogue = Radiobutton(self.horde, text='Rogue', variable=self.class_var, value=3, font=("Helvetica", 30))
        self.priest = Radiobutton(self.horde, text='Priest', variable=self.class_var, value=4, font=("Helvetica", 30))
        self.shaman = Radiobutton(self.horde, text='Shaman', variable=self.class_var, value=5, font=("Helvetica", 30))
        self.mage = Radiobutton(self.horde, text='Mage', variable=self.class_var, value=6, font=("Helvetica", 30))
        self.druid = Radiobutton(self.horde, text='Druid', variable=self.class_var, value=7, font=("Helvetica", 30))
        self.warlock = Radiobutton(self.horde, text='Warlock', variable=self.class_var, value=8, font=("Helvetica", 30))

        # Lots of placing stuff.
        self.orc.place(relx=0.1, rely=0.1)
        self.undead.place(relx=0.1, rely=0.2)
        self.tauren.place(relx=0.1, rely=0.3)
        self.troll.place(relx=0.1, rely=0.4)

        self.warrior.place(relx=0.6, rely=0.1)
        self.hunter.place(relx=0.6, rely=0.2)
        self.rogue.place(relx=0.6, rely=0.3)
        self.priest.place(relx=0.6, rely=0.4)
        self.mage.place(relx=0.6, rely=0.5)
        self.warlock.place(relx=0.6, rely=0.6)
        self.shaman.place(relx=0.6, rely=0.7)
        self.druid.place(relx=0.6, rely=0.8)

        # Creating a label that prompts the user to enter their desired character name in the entry box.
        self.name_label = Label(self.horde, text='Enter Name: ', font=("Helvetica", 30))
        self.name_entry = Entry(self.horde, width=20)

        self.name_label.place(relx=0.1, rely=0.89)
        self.name_entry.place(relx=0.3, rely=0.9)

        # Creating the Enter World button.
        self.world_button = Button(self.horde, text='Enter World', command=self.save, font=("Helvetica", 30))

        self.world_button.place(relx=0.8, rely=0.89)

    def save(self):
        # The Enter World button when clicked will open the text file, gather the information the user has
        # entered or selected and then close the file again.
        characters_file = open('characters.txt', 'w')
        character_name = self.name_entry.get()
        characters_file.write(character_name + " - ")

        if self.radio_var.get() == 1:
            characters_file.write("Orc")
        elif self.radio_var.get() == 2:
            characters_file.write("Undead")
        elif self.radio_var.get() == 3:
            characters_file.write("Tauren")
        elif self.radio_var.get() == 4:
            characters_file.write("Troll")

        if self.class_var.get() == 1:
            characters_file.write(" Warrior")
        elif self.class_var.get() == 2:
            characters_file.write(" Hunter")
        elif self.class_var.get() == 3:
            characters_file.write(" Rogue")
        elif self.class_var.get() == 4:
            characters_file.write(" Priest")
        elif self.class_var.get() == 5:
            characters_file.write(" Shaman")
        elif self.class_var.get() == 6:
            characters_file.write(" Mage")
        elif self.class_var.get() == 7:
            characters_file.write(" Druid")
        elif self.class_var.get() == 8:
            characters_file.write(" Warlock")

        characters_file.close()


def main():
    root = Tk()
    _ = WoW(root)
    root.mainloop()


main()
