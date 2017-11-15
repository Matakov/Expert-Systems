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
        self.master.title("Monetary Incentive Delay Task")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object
        fileMenu = Menu(menu)

        # adds a command to the menu option, calling it exit, and the command it runs on event is client_exit
        fileMenu.add_command(label="New", command=self.client_new)
        fileMenu.add_command(label="Open", command=self.client_open)
        fileMenu.add_command(label="Save", command=self.client_save)
        fileMenu.add_command(label="Save As", command=self.client_saveas)
        fileMenu.add_separator()
        #fileMenu.add_command(label="SRT", command=self.client_srt)
        #fileMenu.add_command(label="MID", command=self.client_mid)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.client_exit)

        # added "File" to our menu
        menu.add_cascade(label="File", menu=fileMenu)

        # create the file object
        simMenu = Menu(menu, tearoff=0)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit

        # added "Simulation" to our menu
        menu.add_cascade(label="Simulation", menu=simMenu)
        simMenu.add_command(label="Parameters", command=self.paramWin)
     #   simMenu.add_command(label="Analysis", command=hello)

        # Add another Menu to the Menu Bar and an item
        helpMenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="Documentation", command=self.msgBox)
        helpMenu.add_command(label="About", command=self.msgBox)

    def paramWin(self):
        gringo = Tk()
        gringo.geometry("500x500")

        # creation of an instance
        app = ParametersWin(gringo)

        # mainloop
        gringo.mainloop()

    def simPage(self):
        root.geometry("600x500")

        # creation of an instance
        app = SimulationPage(root)

        # mainloop
        root.mainloop()

    # Display a Message Box, Callback function
    def msgBox(self):
        mBox.showinfo('About the software', 'Version 1.0\nFER 2017\nAuthors: Babic, Farszky, Miskulin')

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

class ParametersWin(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.init_window()
        label = Label(self, text="This is the start page")
        label.pack(side="top", fill="x", pady=10)

    def init_window(self):
        # changing the title of our master widget
        self.master.title("Parameters")
        self.pack(fill=BOTH, expand=1)

        tabControl = ttk.Notebook(self) # create Tab Control
        tabScan = Frame(tabControl)  # Create a tab
        tabControl.add(tabScan, text=' Pre-scan ')  # Add the tab
        tabOne = Frame(tabControl) # Create a tab
        tabControl.add(tabOne, text=' Simple Reaction Time ')  # Add the tab
        tabTwo = Frame(tabControl)  # Create a tab
        tabControl.add(tabTwo, text=' Monetary Incentive Delay ')  # Add the tab
        tabControl.pack(expand=1, fill="both")  # Pack to make visible


class SimulationPage(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        label = Label(self, text="This is page 1")

#class AnalysisPage(Frame):

#    def __init__(self, parent, controller):
#        Frame.__init__(self, parent)
#        self.controller = controller
#        label = Label(self, text="This is page 1", font=controller.title_font)
#        label.pack(side="top", fill="x", pady=10)
#        button = Button(self, text="Go to the start page",
#                           command=lambda: controller.show_frame("StartPage"))
#        button.pack()


#class SRTPage(Frame):

#    def __init__(self, parent, controller):
#        Frame.__init__(self, parent)
#        self.controller = controller
#        label = Label(self, text="This is page 2", font=controller.title_font)
#        label.pack(side="top", fill="x", pady=10)
#        button = Button(self, text="Go to the start page",
#                           command=lambda: controller.show_frame("StartPage"))
#        button.pack()


#class MIDPage(Frame):

#    def __init__(self, parent, controller):
#        Frame.__init__(self, parent)
#        self.controller = controller
#        label = Label(self, text="This is page 2", font=controller.title_font)
#        label.pack(side="top", fill="x", pady=10)
#        button = Button(self, text="Go to the start page",
#                           command=lambda: controller.show_frame("StartPage"))
#        button.pack()

if __name__ == "__main__":
    # root window created. Here, that would be the only window, but
    # you can later have windows within windows.
    root = Tk()

    root.geometry("600x500")

    # creation of an instance
    app = Window(root)

    # mainloop
    root.mainloop()