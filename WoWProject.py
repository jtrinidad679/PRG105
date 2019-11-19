from tkinter import *
from PIL import Image, ImageTk
import cv2


class MainScreen:
    def __init__(self, master):
        self.master = master
        self.master.title('World of Warcraft')

        # master.iconbitmap(r'wow_icon.png')

        # image = cv2.imread('worldofwarcraft.jpg')
        #
        # b, g, r = cv2.split(image)
        # img = cv2.merge((r, g, b))
        #
        # # master = Tk()
        #
        # im = Image.fromarray(img)
        # imgtk = ImageTk.PhotoImage(image=im)
        #
        # Label(master, image=imgtk).pack()


def main():
    root = Tk()
    _ = MainScreen(root)
    root.mainloop()
#
#         # canvas = Tk.Canvas(master, width=2000, height=2000)
#         # wow_image = Tk.PhotoImage(file="worldofwarcraft.jpg")
#         # canvas.create_image(0,0,anchor=NW, image = wow_image)
#         # canvas.pack()
#         #
#         # master.geometry("2000x2000")
#         #
#         # self.character_frame = tk.Frame(self.master)
#         # self.create_character_frame = tk.Frame(self.master)
#         # self.quit_frame = tk.Frame(self.master)
#         #
#         # self.value = tk.IntVar()
#         # self.value.set(1)
#         #
#         # self.character_button = tk.Button(self.create_character_frame, text='Create New Character', command=self.faction_menu)
#         # self.quit_button = tk.Button(self.quit_frame, text='Quit', bg='black', fg='red', command=self.master.destroy)
#         #
#         # self.character_button.pack(side='left')
#         # self.quit_button.pack(side='left')
#         #
#         # self.character_frame.pack()
#         # self.create_character_frame.pack()
#         # self.quit_frame.pack()
#
#     # def faction_menu(self):
#     #     if self.value.get() == 1:
#     #         _ = Faction()
#
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


