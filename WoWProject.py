from tkinter import *
from PIL import ImageTk
import cv2


class MainScreen:
    def __init__(self, master):
        self.master = master
        self.master.title('World of Warcraft')

        master.iconbitmap(r'wow_icon.png')

        # image = cv2.imread('worldofwarcraft2.jpg')
        #
        # b, g, r = cv2.split(image)
        # img = cv2.merge((r, g, b))
        #
        # # master = Tk()
        #
        # im = Image.fromarray(img)
        # imgtk = ImageTk.PhotoImage(image=im)
        # #
        # Label(master, image=imgtk).pack()
        canvas = Canvas(width=1250, height=700)
        canvas.pack(expand=YES, fill=BOTH)
        image = ImageTk.PhotoImage(file='worldofwarcraft2.jpg')
        canvas.create_image(10, 10, image=image, anchor=NW)
        master.mainloop()

        # master.geometry("2000x2000")

        self.character_frame = Frame(self.master)
        self.create_character_frame = Frame(self.master)
        self.quit_frame = Frame(self.master)

        self.value = IntVar()
        self.value.set(1)

        self.character_button = Button(self.create_character_frame, text='Create New Character', command=self.faction_menu)
        self.quit_button = Button(self.quit_frame, text='Quit', bg='black', fg='red', command=self.master.destroy)

        self.character_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.character_frame.pack()
        self.create_character_frame.pack()
        self.quit_frame.pack()

    def faction_menu(self):
        if self.value.get() == 1:
            _ = Faction()


def main():
    root = Tk()
    _ = MainScreen(root)
    root.mainloop()


main()

#
# class Faction:
#     def _init__(self, master):
#         self.faction = Tk.Toplevel(master)
#         self.faction.title('Faction Selector')
#
#         self.faction_description_frame = Tk.Frame(self.faction)
#         self.horde_frame = Tk.Frame(self.faction)
#         self.alliance_frame = Tk.Frame(self.faction)
#
#         self.description_label = Tk.Label(self.faction_description_frame, text='Before you step foot into Azeroth, you need to select a faction. \n'
#                                                                                     'The factions available to you are: Alliance or Horde.')
#         self.description_label.pack(side='left')
#
#         self.alliance_button = Tk.Button(self.alliance_frame, text='Alliance', command=self.alliance)
#         self.horde_button = Tk.Button(self.horde_frame, text='Horde', command=self.horde)
#
#         self.faction_description_frame.pack()
#         self.horde_frame.pack()
#         self.alliance_frame.pack()
#
#
# def main():
#     root = Tk()
#     _ = MainScreen(root)
#     root.mainloop()
#
#
# main()

# https://stackoverflow.com/questions/36575890/how-to-set-a-tkinter-window-to-a-constant-size


