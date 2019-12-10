from tkinter import *
from PIL import ImageTk
import pickle


class WoW:
    def __init__(self, master):
        self.master = master
        self.master.title("World of Warcraft")
        master.geometry('1000x700')

        try:
            characters_file = open('characters.txt' 'r')
            file_contents = characters_file.read()
            characters_file.close()
            print(file_contents)
        except FileNotFoundError:
            print("You don't have any characters yet. Try making one!")

        self.character_label = Label(master, text='Your Characters', font=("Helvetica", 30))
        self.character_label.place(anchor=NW)
        self.character_button = Button(master, text='Create New Character', font=("Helvetica", 30),
                                       fg='blue', command=self.faction_menu)
        self.quit_button = Button(master, text='Quit', font=("Helvetica", 30),
                                  fg='red', command=self.master.destroy)

        self.character_button.place(relx=0, rely=1, anchor=SW)
        self.quit_button.place(relx=1, rely=1, anchor=SE)

        canvas = Canvas(master, width=500, height=600)
        canvas.pack(side=RIGHT)
        image = ImageTk.PhotoImage(file='wowza.jpg')
        canvas.create_image(265, 325, image=image)
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

        self.alliance_label = Label(self.faction, text='Driven by tradition, the Alliance consists of powerful' '\n'
                                    'cultures and groups bound by their deep commitments' '\n'
                                    'to abstract concepts like nobility, honor, faith, justice,' '\n'
                                    'and sacrifice. Striving to represent these high ideals, its' '\n'
                                    'many different peoples all contribute their technical,' '\n'
                                    'arcane, and spiritual wisdom towards their shared goal' '\n'
                                    'of preserving order on Azeroth and creating a' '\n'
                                    'peaceful and just world.'
                                    , relief=SUNKEN, bg='white', fg='blue', font=("Helvetica", 16))

        self.horde_label = Label(self.faction, text='A faction led by off-worlders and composed of' '\n'
                                 'outsiders, the Horde has survived the obstacles of Azeroth by' '\n'
                                 'bonding together and fighting as family, comrades, or even' '\n'
                                 'uneasy allies. Driven by unity, the Horde consists of a coalition' '\n'
                                 'of disparate races and cultures loosely joined in an alliance' '\n' 
                                 'of convenience against a hostile world that would' '\n'
                                 'see them destroyed.',relief=SUNKEN, bg='white', fg='red', font=("Helvetica", 16))

        self.alliance_label.place(relx=0.6, rely=0.7)
        self.horde_label.place(relx=0.02, rely=0.7)

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

        self.faction_description_label.pack()
        self.description_frame.pack()

        self.alliance_button = Button(self.faction, text='Alliance', command=self.alliance, font=("Helvetica", 30),
                                      fg='blue')
        self.horde_button = Button(self.faction, text='Horde', command=self.horde, font=("Helvetica", 30), fg='red')

        self.alliance_button.place(relx=0.74, rely=0.6)
        self.horde_button.place(relx=0.17, rely=0.6)
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

        self.alliance_label = Label(self.alliance, text='Alliance Races', fg='blue', font=("Helvetica", 30))
        self.alliance_class_label = Label(self.alliance, text='Classes', fg='blue', font=("Helvetica", 30))
        self.alliance_label.place(relx=0.06, rely=0)
        self.alliance_class_label.place(relx=0.6, rely=0)

        self.radio_var = IntVar()
        self.radio_var.set(1)

        self.human = Radiobutton(self.alliance, text='Human', variable=self.radio_var, value=1, font=("Helvetica", 30))
        self.dwarf = Radiobutton(self.alliance, text='Dwarf', variable=self.radio_var, value=2, font=("Helvetica", 30))
        self.night_elf = Radiobutton(self.alliance, text='Night Elf', variable=self.radio_var, value=3,
                                     font=("Helvetica", 30))
        self.gnome = Radiobutton(self.alliance, text='Gnome', variable=self.radio_var, value=4, font=("Helvetica", 30))

        self.class_var = IntVar()
        self.class_var.set(1)

        self.warrior = Radiobutton(self.alliance, text='Warrior', variable=self.class_var, value=1, font=("Helvetica", 30))
        self.hunter = Radiobutton(self.alliance, text='Hunter', variable=self.class_var, value=2, font=("Helvetica", 30))
        self.rogue = Radiobutton(self.alliance, text='Rogue', variable=self.class_var,value=3, font=("Helvetica", 30))
        self.priest = Radiobutton(self.alliance, text='Priest', variable=self.class_var, value=4, font=("Helvetica", 30))
        self.mage = Radiobutton(self.alliance, text='Mage', variable=self.class_var, value=5, font=("Helvetica", 30))
        self.warlock = Radiobutton(self.alliance, text='Warlock', variable=self.class_var, value=6, font=("Helvetica", 30))
        self.druid = Radiobutton(self.alliance, text='Druid', variable=self.class_var, value=6, font=("Helvetica", 30))

        self.human.place(relx=0.1, rely=0.15)
        self.dwarf.place(relx=0.1, rely=0.35)
        self.night_elf.place(relx=0.1, rely=0.55)
        self.gnome.place(relx=0.1, rely=0.75)

        self.warrior.place(relx=0.6, rely=0.1)
        self.hunter.place(relx=0.6, rely=0.2)
        self.rogue.place(relx=0.6, rely=0.3)
        self.priest.place(relx=0.6, rely=0.4)
        self.mage.place(relx=0.6, rely=0.5)
        self.warlock.place(relx=0.6, rely=0.6)
        self.druid.place(relx=0.6, rely=0.7)


class Horde:
    def __init__(self, master):
        self.horde = Toplevel(master)
        self.horde.title('Horde')
        self.horde.geometry('1000x700')

        self.horde_label = Label(self.horde, text='Races', fg='red', font=("Helvetica", 30))
        self.horde_class_label = Label(self.horde, text='Classes', fg='red', font=("Helvetica", 30))

        self.horde_label.place(relx=0.1, rely=0)
        self.horde_class_label.place(relx=0.6, rely=0)

        self.radio_var = IntVar()
        self.radio_var.set(1)

        self.class_var = IntVar()
        self.class_var.set(1)

        self.orc = Radiobutton(self.horde, text='Orc', variable=self.radio_var, value=1, font=("Helvetica", 30))
        self.undead = Radiobutton(self.horde, text='Undead', variable=self.radio_var, value=2, font=("Helvetica", 30))
        self.tauren = Radiobutton(self.horde, text='Tauren', variable=self.radio_var, value=3,
                                     font=("Helvetica", 30))
        self.troll = Radiobutton(self.horde, text='Troll', variable=self.radio_var, value=4, font=("Helvetica", 30))

        self.orc.place(relx=0.1, rely=0.1)
        self.undead.place(relx=0.1, rely=0.2)
        self.tauren.place(relx=0.1, rely=0.3)
        self.troll.place(relx=0.1, rely=0.4)

        self.warrior = Radiobutton(self.horde, text='Warrior', variable=self.class_var, value=1, font=("Helvetica", 30))
        self.hunter = Radiobutton(self.horde, text='Hunter', variable=self.class_var, value=2, font=("Helvetica", 30))
        self.rogue = Radiobutton(self.horde, text='Rogue', variable=self.class_var,value=3, font=("Helvetica", 30))
        self.priest = Radiobutton(self.horde, text='Priest', variable=self.class_var, value=4, font=("Helvetica", 30))
        self.shaman = Radiobutton(self.horde, text='Shaman', variable=self.class_var, value=5, font=("Helvetica", 30))
        self.mage = Radiobutton(self.horde, text='Mage', variable=self.class_var, value=6, font=("Helvetica", 30))

        self.warrior.place(relx=0.6, rely=0.1)
        self.hunter.place(relx=0.6, rely=0.2)
        self.rogue.place(relx=0.6, rely=0.3)
        self.priest.place(relx=0.6, rely=0.4)
        self.shaman.place(relx=0.6, rely=0.5)
        self.mage.place(relx=0.6, rely=0.6)

        self.name_label = Label(self.horde, text='Enter Name: ', font=("Helvetica", 30))
        self.name_entry = Entry(self.horde, width=20)

        self.name_label.place(relx=0.3, rely=0.89)
        self.name_entry.place(relx=0.5, rely=0.9)

        self.world_button = Button(self.horde, text='Enter World', command=self.save, font=("Helvetica", 30))

        self.world_button.place(relx=0.8, rely=0.89)

    def save(self):
        print(self.radio_var.get())
        characters_file = open('characters.txt', 'w')
        if self.radio_var.get() == 1:
            character = characters_file.write("Orc")
        elif self.radio_var.get() == 2:
            character = characters_file.write("Undead")
        elif self.radio_var.get() == 3:
            character = characters_file.write("Tauren")
        elif self.radio_var.get() == 4:
            character = characters_file.write("Troll")
        characters_file.close()


def main():
    root = Tk()
    _ = WoW(root)
    root.mainloop()


main()
