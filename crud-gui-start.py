import tkinter
import tkinter.messagebox
import pickle


# main (root) GUI menu
class CrudGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Welcome Menu')

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # create the radio buttons
        self.look = tkinter.Radiobutton(self.top_frame, text='Look up customer',
                                        variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text='Add Customer',
                                       variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text='Change customer email',
                                          variable=self.radio_var, value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text='Delete customer',
                                          variable=self.radio_var, value=4)

        # pack the radio buttons
        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)

        # create ok and quit buttons
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy)

        # pack the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        if self.radio_var.get() == 1:
            _ = LookGUI(self.master)
        elif self.radio_var.get() == 2:
            _ = AddGUI(self.master)
        elif self.radio_var.get() == 3:
            _ = ChangeGUI(self.master)
        elif self.radio_var.get() == 4:
            _ = DeleteGUI(self.master)


class LookGUI:
    def __init__(self, master):

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.look = tkinter.Toplevel(master)
        self.look.title('Search for customer')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame - label and entry box for name
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        # middle frame - label for results
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        # pack Middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def search(self):
        name = self.search_entry.get()
        result = self.customers.get(name, 'Not Found')
        self.value.set(result)

    def back(self):
        self.look.destroy()


class AddGUI:
    def __init__(self, master):

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.add = tkinter.Toplevel(master)
        self.add.title('Add a customer')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.add)
        self.middle_frame = tkinter.Frame(self.add)
        self.bottom_frame = tkinter.Frame(self.add)
        self.last_frame = tkinter.Frame(self.add)

        # widgets for top frame - label and entry box for name
        self.add_label = tkinter.Label(self.top_frame, text='Enter customer name to add: ')
        self.add_entry = tkinter.Entry(self.top_frame, width=15)
        self.email_label = tkinter.Label(self.middle_frame, text='Enter customer email address to add: ')
        self.email_entry = tkinter.Entry(self.middle_frame, width=15)

        # pack top frame
        self.add_label.pack(side='left')
        self.add_entry.pack(side='left')
        self.email_label.pack(side='left')
        self.email_entry.pack(side='left')

        # middle frame - label for results
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.bottom_frame, text='Results: ')
        self.result_label = tkinter.Label(self.bottom_frame, textvariable=self.value)

        # pack Middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # buttons for bottom frame
        self.add_button = tkinter.Button(self.last_frame, text='Add', command=self.add_person)
        self.back_button = tkinter.Button(self.last_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.add_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        self.last_frame.pack()

    def add_person(self):
        name = self.add_entry.get()
        email = self.email_entry.get()
        if name in self.customers:
            result = name + " already exists"
        else:
            result = self.customers.get(name, name + " " + email + " Will Be Added")
            self.customers[name] = email
            output_file = open("customer_file.dat", 'wb')
            pickle.dump(self.customers, output_file)
            output_file.close()
        self.value.set(result)

    def back(self):
        self.add.destroy()


class ChangeGUI:
    def __init__(self, master):

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.change = tkinter.Toplevel(master)
        self.change.title('Change Customer Email')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.change)
        self.middle_frame = tkinter.Frame(self.change)
        self.bottom_frame = tkinter.Frame(self.change)
        self.last_frame = tkinter.Frame(self.change)

        # widgets for top frame - label and entry box for name
        self.name_label = tkinter.Label(self.top_frame, text='Enter customer name: ')
        self.name_entry = tkinter.Entry(self.top_frame, width=15)
        self.email_label = tkinter.Label(self.middle_frame, text='Enter new email address: ')
        self.email_entry = tkinter.Entry(self.middle_frame, width=15)

        # pack top frame
        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')
        self.email_label.pack(side='left')
        self.email_entry.pack(side='left')

        # middle frame - label for results
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.bottom_frame, text='Results: ')
        self.result_label = tkinter.Label(self.bottom_frame, textvariable=self.value)

        # pack Middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # buttons for bottom frame
        self.change_button = tkinter.Button(self.last_frame, text='Change', command=self.change_email)
        self.back_button = tkinter.Button(self.last_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.change_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        self.last_frame.pack()

    def change_email(self):
        name = self.name_entry.get()
        new_email = self.email_entry.get()
        if name in self.customers:
            result = "Successfully Changed"
            self.customers[name] = new_email
            output_file = open("customer_file.dat", 'wb')
            pickle.dump(self.customers, output_file)
            output_file.close()
        else:
            result = "Sorry, we couldn't find you in our records. \nPlease exit this window and then add a new customer."
        self.value.set(result)

    def back(self):
        self.change.destroy()


class DeleteGUI:
    def __init__(self, master):

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.delete = tkinter.Toplevel(master)
        self.delete.title('Change Customer Email')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.delete)
        self.middle_frame = tkinter.Frame(self.delete)
        self.bottom_frame = tkinter.Frame(self.delete)

        # widgets for top frame - label and entry box for name
        self.name_label = tkinter.Label(self.top_frame, text='Enter customer name: ')
        self.name_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')

        # middle frame - label for results
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        # pack Middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # buttons for bottom frame
        self.change_button = tkinter.Button(self.bottom_frame, text='Delete', command=self.delete_customer)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.change_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def delete_customer(self):
        name = self.name_entry.get()
        if name in self.customers:
            result = "Successfully Deleted"
            del self.customers[name]
            output_file = open('customer_file.dat', 'wb')
            pickle.dump(self.customers, output_file)
            output_file.close()
        else:
            result = "Don't worry, you're not even in our records!"
        self.value.set(result)

    def back(self):
        self.delete.destroy()


def main():
    # create a window
    root = tkinter.Tk()
    # call the GUI and send it the root menu
    # use _ as variable name because the variable will not be needed after instantiating GUI
    # the GUI itself will handles the remaining program logic
    _ = CrudGUI(root)
    # control the mainloop from main instead of the class
    root.mainloop()


main()
