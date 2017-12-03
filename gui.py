import sys
import os
import subprocess

if sys.version_info[0] < 3:
    # python 2
    from Tkinter import *
    import tkFileDialog as filedialog
    import ttk
    import tkMessageBox as mBox
    # import clips6
    # import clips
else:
    # python 3
    from tkinter import *
    from tkinter import filedialog
    from tkinter import ttk
    from tkinter import messagebox as mBox


# class Window, inheriting from the Frame class.

class Window(Frame):
    # define settings upon initialization.
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        # window initialization
        self.init_window()

    # creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Fault diagnostics")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object
        file_menu = Menu(menu)

        # adds a command to the menu option, calling it exit, and the command it runs on event is client_exit
        file_menu.add_command(label="New", command=self.client_new)
        file_menu.add_command(label="Open", command=self.client_open)
        file_menu.add_command(label="Save", command=self.client_save)
        file_menu.add_command(label="Save As", command=self.client_saveas)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.client_exit)

        # added "File" to our menu
        menu.add_cascade(label="File", menu=file_menu)

        # create the rule object
        rule_menu = Menu(menu, tearoff=0)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit

        # added "Rules" to our menu
        menu.add_cascade(label="Rules", menu=rule_menu)
        rule_menu.add_command(label="Add new...", command=self.ruleWin)

        # Add another Menu to the Menu Bar and an item
        help_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help_menu)
        #help_menu.add_command(label="Presentation", command=self.openPDF("filename.pdf"))
        #help_menu.add_command(label="Documentation", command=self.openPDF("filename.pdf"))
        help_menu.add_separator()
        help_menu.add_command(label="About", command=self.msgBox)

        Label(self.master, text="Select symptoms:").pack(side=TOP)#.grid(column=0, row=0)
        combo_master = Combos(self.master)
        combo_one = combo_master.add_combo('readonly', (1, 2, 3, 4, 5))
        combo_two = combo_master.add_combo('readonly', (6, 7, 8, 9, 10))
        # combo_two.configure(state='disabled')

        # add separator between comboboxes and text area
        ttk.Separator(self.master, orient=HORIZONTAL).pack(pady=10, padx=5, ipadx=300, ipady=5)

        # text area where user will have preview of possible symptoms
        textarea = Text(self.master, state='disabled').pack()
        #textarea.grid(row=6, column=0)


        #combo_one.bind('<<ComboboxSelected>>', self.add_simptom(combo_one.get(), textarea))

    def add_simptom(self, value, text_area):
        # get data so far in textbox
        data = text_area.get(0.0, END)
        split_data = data.split("\n")
        # print len(split_data)
        ifIn = 0
        # look if there is already that value inside textbox
        for inputs in split_data:
            if (inputs == value):
                ifIn = 1
        # if value is not in, add it
        if not ifIn:
            self.text_area.insert(END, value + "\n")
        pass

    def remove_simptom(self, value):
        # get data so far in textbox
        data = self.TextArea.get(0.0, END)
        split_data = data.split()
        self.TextArea.delete(0.0, END)
        # look if there is already that value inside textbox and if it is, do not add it (remove it)
        print(len(split_data))
        for inputs in split_data:
            if (inputs != value):
                if (inputs != "\n"):
                    in2 = " ".join(inputs.split())
                    self.TextArea.insert(END, in2.strip() + "\n")

    '''
            # Label(self.master, text="Select your symptom:").grid(column=1, row=0)
            combo_one = self.addCombo(1, 3, 'readonly')
            # combo_two = self.addCombo(2, 3, 'disabled', self.changeComboParam(combo_one, self.combo_two))
            #combo_one.bind('<<ComboboxSelected>>', self.enableCombo)
            #self.addCombo(2, 3)

            Combos(self.master)

        def changeComboParam(self, combo_en, combo_dis):
            if combo_en.get() == '2':
                combo_dis.configure(state='readonly')
            else:
                pass

        def addCombo(self, r, c, s, ccp=None):
            symptom = StringVar()
            newCombo = ttk.Combobox(self.master, width=40, textvariable=symptom, state=s, postcommand=ccp)
            newCombo['values'] = (1, 2, 10, 42, 100)
            newCombo.grid(column=c, row=r)
            # newCombo.current(0)
            return newCombo
    '''




    def ruleWin(self):
        gringo = Tk()
        gringo.geometry("500x500")

        # creation of an instance
        app = ParametersWin(gringo)

        # mainloop
        gringo.mainloop()

    # Display a Message Box, Callback function
    def msgBox(self):
        mBox.showinfo('About the software', 'Version 1.0\nFER 2017\nAuthors: Matkovic, Miskulin')

    def client_new(self):
        root = Tk()
        root.geometry("400x300")
        app = Window(root)
        root.mainloop()

    def client_open(self):
        mask = \
            [("ASCII files", "*.txt"),
             ("HTML files", "*.htm"),
             ("All files", "*.*")]
        filename = filedialog.askopenfilename(filetypes=mask, title="Select file")

    def client_save(self):
        file_exists = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if file_exists is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return
        text2save = str(self.text.get(1.0, END))  # starts from `1.0`, not `0.0`
        file_exists.write(text2save)
        file_exists.close()  # `()` was missing.

    def client_saveas(self):
        filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                     filetypes=(("ASCII files", "*.txt"), ("all files", "*.*")))

    def client_exit(self):
        exit()

    def client_open_directory(self):
        #from  Tkinter import *
        #import Tkinter, Tkconstants, tkFileDialog
        #root = Tk()
        #root.directory = tkFileDialog.askdirectory()
        #print(root.directory)
        print("proba")

   # def show_frame(self, page_name):
        # Show a frame for the given page name
        #frame = self.frames[page_name]
        #frame.tkraise()

    def openPDF(self, filename):
        if sys.platform == "win32":
           os.startfile(filename)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, filename])



class Combos:
    def __init__(self, parent):
        self.parent = parent

    def change_state(self, combo, s):
        combo.configure(state=s)

    def add_combo(self, s, sym_values):
        symptom = StringVar()
        newCombo = ttk.Combobox(self.parent, textvariable=symptom, state=s)
        newCombo['values'] = sym_values
        newCombo.pack(fill=BOTH, padx=20, pady=10, ipadx=5, ipady=5, side=TOP)
        # newCombo.grid(column=c, row=r)
        # newCombo.current(0)
        return newCombo

class ParametersWin(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.init_window()
        label = Label(self, text="Edit rules")
        label.pack(side="top", fill="x", pady=10)

    def init_window(self):
        # changing the title of our master widget
        self.master.title("Edit rules")
        self.pack(fill=BOTH, expand=1)

        tabControl = ttk.Notebook(self) # create Tab Control
        tabScan = Frame(tabControl)  # Create a tab
        tabControl.add(tabScan, text=' Pre-scan ')  # Add the tab
        tabOne = Frame(tabControl) # Create a tab
        tabControl.add(tabOne, text=' Simple Reaction Time ')  # Add the tab
        tabTwo = Frame(tabControl)  # Create a tab
        tabControl.add(tabTwo, text=' Monetary Incentive Delay ')  # Add the tab
        tabControl.pack(expand=1, fill="both")  # Pack to make visible




if __name__ == "__main__":
    # root window created. Here, that would be the only window, but
    # you can later have windows within windows.
    root = Tk()

    root.geometry("600x500")

    # creation of an instance
    app = Window(root)

    # mainloop
    root.mainloop()
