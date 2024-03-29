import sys
import os
import subprocess

if sys.version_info[0] < 3:
    # python 2
    from Tkinter import *
    import tkFileDialog as filedialog
    import ttk
    import tkMessageBox as mBox
    import clips
    clips.Reset()

else:
    # python 3
    from tkinter import *
    from tkinter import filedialog
    from tkinter import ttk
    from tkinter import messagebox as mBox

def build(text):
	clips.SendCommand(text)

def GetValues(filename='rulez.clp'):
    f = open(filename, 'r')

    flagLHS = False
    flagRHS = False

    LHS = []
    RHS = []

    for line in f:
        # if line not in ['\n', '\r\n']:
        # print line[0]+line[1]
        if "=>" in line:
            flagLHS = False
        if flagLHS:
            # print line
            LHS.append(line.strip()[1:-1])
        if "defrule" in line:
            flagLHS = True

        if "defrule" in line:
            flagRHS = False
        if flagRHS:
            # print line
            line = line.strip()
            index = line.find(")))")
            if index==-1:
                index = line.find("))")
            if line != "":
                RHS.append(line[9:index])
        if "=>" in line:
            flagRHS = True
        # re.search(r'\s[\s]*\s', x, re.S)
    f.close()
    return LHS, RHS


# class Window, inheriting from the Frame class.
class Window(Frame):
    # define settings upon initialization.
    def __init__(self, master,clips):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master=None)

        # reference to the master widget, which is the tk window
        self.master = master

        # window initialization
        self.init_window(clips)
	

    # creation of init_window
    def init_window(self,clips):
	self.clips=clips
        # changing the title of our master widget
        self.master.title("Fault diagnostics")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        self.top = Frame(self.master)
        self.middle = Frame(self.master)
        self.bottom = Frame(self.master)

        self.top.pack(side=TOP, fill=BOTH, expand=1)
        self.middle.pack(side=TOP, fill=X, expand=1, padx=40, pady=10)
        self.bottom.pack(side=BOTTOM, fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object
        file_menu = Menu(menu)

        # adds a command to the menu option, calling it exit, and the command it runs on event is client_exit
        file_menu.add_command(label="New            ", command=self.client_new)
        file_menu.add_command(label="Open", command=self.client_open)
        file_menu.add_command(label="Save", command=self.client_save)
        file_menu.add_command(label="Save As", command=self.client_saveas)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.client_exit)

        # added "File" to our menu
        menu.add_cascade(label="    File    ", menu=file_menu)

        # create the rule object
        rule_menu = Menu(menu, tearoff=1)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit

        # added "Rules" to our menu
        menu.add_cascade(label="    Rules   ", menu=rule_menu)
        rule_menu.add_command(label="Add new...     ", command=self.ruleWin)

        # Add another Menu to the Menu Bar and an item
        help_menu = Menu(menu, tearoff=1)
        menu.add_cascade(label="    Help    ", menu=help_menu)
        help_menu.add_command(label="Database", command=lambda: self.openPDF("test.pdf"))
        help_menu.add_command(label="Presentation", command=lambda: self.openPDF("test.pdf"))
        help_menu.add_command(label="Documentation", command=lambda: self.openPDF("test.pdf"))
        help_menu.add_separator()
        help_menu.add_command(label="About", command=self.msgBox)

        # Text description before combobox
        lab_ = Label(self.master, text="Select symptoms:", font=("Arial", 14), anchor="w")
        lab_.pack(in_=self.top, side=TOP, fill=X, pady=10, padx=15)

        # define combobox
        self.symptom = StringVar()
        self.combo_one = ttk.Combobox(self.master, textvariable=self.symptom, state='readonly')

        self.filename = 'rulez.clp'

        LHS, RHS = GetValues(self.filename)
        self.LHS = LHS
        self.values = list(set(self.LHS))

        # combobox for symptom display
        self.combo_one.configure(values=self.values)
        self.combo_one.pack(in_=self.top, fill=BOTH, padx=20, pady=10, ipadx=5, ipady=5, side=TOP)

        # delete button
        self.del_button = Button(self.master, text='delete symptom', width=15, height=2,
                          command=lambda: self.remove_simptom(self.combo_one.get()))
        self.del_button.pack(in_=self.middle, side=LEFT, padx=0)

        # run button
        self.run_button = Button(self.master, text='RUN', fg="red", width=15, height=2,
                          command=lambda: self.run())
        self.run_button.pack(in_=self.middle, side=LEFT, padx=40)

        # reset button
        self.reset_button = Button(self.master, text='clear output', width=15, height=2,
                                   command=lambda: self.clear())
        self.reset_button.pack(in_=self.middle, side=RIGHT, padx=0)


        # add separator between comboboxes and text area
        ttk.Separator(self.master, orient=HORIZONTAL).pack(side=TOP, pady=10, padx=15, ipadx=300, ipady=5)

        # text area where user will have preview of possible symptoms
        self.text_area = Text(self.master, state='disable')
        self.text_area.pack(side=BOTTOM)

        # value = self.combo_one.get()
        self.combo_one.bind('<<ComboboxSelected>>', self.add_simptom)
        self.clips.Load(self.filename)

    def clear(self):
        self.text_area.configure(state='normal')
        self.text_area.delete('1.0', END)
        self.text_area.configure(state='disable')

    def run(self):
        sys.stdout = open("logfile", "w")
        self.text_area.configure(state='normal')
        data = self.text_area.get(0.0, END)
        split_data = data.split("\n")
        self.text_area.delete(0.0, END)
        # look if there is already that value inside textbox and if it is, do not add it (remove it)
        # print(len(split_data))
        for inputs in split_data:
            inputs = inputs.encode("utf-8")
            if inputs != "":
                # print inputs
                if inputs != "\n":
                    self.clips.Assert("("+inputs+")")
                    # in2 = " ".join(inputs.split())
                    # self.text_area.insert(END, inputs.strip() + "\n")
                split_data_edited = []
                for line in split_data:
                    line = line.encode("utf-8")
                    if line != "":
                        if line != "\n":
                            split_data_edited.append(line)
        self.clips.Run()

        lines = []
        answer = []
        self.clips.PrintFacts()

        sys.stdout = open("/dev/stdout", "w")
        f = open("logfile", 'r')
        for line in f:
            lines.append(line)

        for line in lines[1:-1]:
            # print line
            line = line.encode("utf-8")
            index = line.find(")")
            line = line[9:index]
            # print line
            if line not in split_data_edited:
                answer.append(line)
        for line in answer:
            self.text_area.insert(END, line.strip() + "\n")
        self.clips.Reset()

        # LHS, RHS = GetValues(self.filename)
        # self.values = list(set(LHS))
        # self.combo_one.configure(values=self.values)

    def add_simptom(self, event=None):
        # get data so far in textbox
        self.text_area.configure(state='normal')
        data = self.text_area.get(0.0, END)
        value = self.combo_one.get()
        split_data = data.split("\n")
        # print len(split_data)
        ifIn = 0
        # look if there is already that value inside textbox
        for inputs in split_data:
            if inputs == value:
                ifIn = 1
        # if value is not in, add it
        # if value is not in, add it
        if not ifIn:
            self.text_area.insert(END, value + "\n")
            self.text_area.configure(state='disable')
        pass

    def remove_simptom(self, value):
        # get data so far in textbox
        self.text_area.configure(state='normal')
        data = self.text_area.get(0.0, END)
        split_data = data.split("\n")

        self.text_area.delete(0.0, END)
        # look if there is already that value inside textbox and if it is, do not add it (remove it)
        # print(len(split_data))
        for inputs in split_data:
            inputs = inputs.encode("utf-8")
            if inputs != value:
                if inputs != "":
                    # print inputs
                    if inputs != "\n":
                        # in2 = " ".join(inputs.split())
                        self.text_area.insert(END, inputs.strip() + "\n")
        self.text_area.configure(state='disable')

    def ruleWin(self):
        gringo = Tk()
        gringo.geometry("550x550")

        # creation of an instance
        app = ParametersWin(gringo, self)

        # mainloop
        gringo.mainloop()

    # Display a Message Box, Callback function
    def msgBox(self):
        mBox.showinfo('About the software', 'Version 1.0\nFER 2017\nAuthors: Matkovic, Miskulin')

    def client_new(self):
        root = Tk()
        root.geometry("600x500")
        root.resizable(0, 0)
        app = Window(root)
        root.mainloop()

    def client_open(self):
        mask = \
            [("CLISP files", "*.clp"),
             ("All files", "*.*")]
        filename = filedialog.askopenfilename(filetypes=mask, title="Select file")
        self.filename=filename
        if len(filename) > 0:
            self.clips.Load(filename)
            self.filename = filename
            LHS, RHS = GetValues(filename)
            self.values = list(set(LHS))
            self.combo_one.configure(values=self.values)

    def client_save(self):
        if self.filename is None:  # asksaveasfile return 'None' if dialog closed with "cancel".
            file_exists = filedialog.asksaveasfile(title="Save", mode='w', defaultextension=".clp")
            self.filename = file_exists
            self.clips.Run()
            self.clips.Save(self.filename)
        return

    def client_saveas(self):
        cwd = os.getcwd()
        # print cwd
        file_exists=filedialog.asksaveasfilename(initialdir=cwd, title="Save As",filetypes=(("CLISP files", "*.clp"), ("ASCII files", "*.txt"), ("all files", "*.*")))
        if len(file_exists)!=0:
                self.filename = file_exists
                self.clips.Run()
                self.clips.Save(self.filename)

    def client_exit(self):
        self.clips.Run()
        if self.filename is None:
            self.clips.Save("rulez.clp")
        else:
            self.clips.Save(self.filename)
            self.master.destroy()
        # exit()

    def openPDF(self, filename):

        if sys.platform == 'linux2':
            subprocess.call(["xdg-open", filename])
        else:
            os.startfile(filename)


class ParametersWin(Frame):

    def __init__(self, parent, ancestor):
        Frame.__init__(self, parent)
        self.ancestor = ancestor
        self.values = ancestor.values
        # print ancestor.values
        self.init_window()

    def init_window(self):
        # changing the title of our master widget
        self.master.title("Rules")
        self.pack(fill=BOTH, expand=1)

        self.tabControl = ttk.Notebook(self) # create Tab Control
        self.tabAdd = Frame(self.tabControl)  # Create a tab
        self.tabControl.add(self.tabAdd, text=' Add rule ')  # Add the tab
        self.tabEdit = Frame(self.tabControl) # Create a tab
        self.tabControl.add(self.tabEdit, text=' Edit rules ')  # Add the tab
        self.tabControl.pack(side="top", expand=1, fill="both")  # Pack to make visible

        ################## TAB ADD

        lab = Label(self.tabAdd, text="Add new rule by entering the rule name, symptom and the malfunctions", anchor="w")
        lab.pack(side=TOP, fill=X, pady=10, padx=15)

        # entry to add malfunction
        self.e = Entry(self.tabAdd)
        self.e.pack(pady=10)
        self.LHS = Text(self.tabAdd, height=12, width=50)
        self.LHS.pack()
        self.e.delete(0, END)
        self.e.insert(0, "add-rule-name")

        self.RHS = Text(self.tabAdd, height=12, width=50)
        self.RHS.pack()

        self.but = Button(self.tabAdd, text='Add', width=15, height=2, command=lambda: self.add_rule(self.e.get(), self.LHS.get(0.0, END), self.RHS.get(0.0, END)))
        self.but.pack(side="bottom", padx=0, pady=30)

        self.RHS.insert(0.0, "add possible malfunction")
        self.LHS.insert(0.0, "add sypmtom")

        ################## TAB EDIT
        # Load the whole file in a text
        self.file = Text(self.tabEdit, height=28, width=65)
        self.file.pack(padx=0, pady=20)
        self.fileButton = Button(self.tabEdit, text="Edit", width=15, height=2, command=lambda: self.editFile(self.file.get(0.0, END)))
        self.fileButton.pack(padx=100, pady=10)
        f = open(self.ancestor.filename, 'r')
        for line in f:
            # print line
            self.file.insert(END, line)
        f.close()

    def editFile(self, textToSave):
        f = open(self.ancestor.filename, 'w')
        for line in textToSave:
            f.write(line)
        f.close()
        self.ancestor.clips.Clear()
        self.ancestor.clips.Load(self.ancestor.filename)
	LHS, RHS = GetValues(self.ancestor.filename)
        self.ancestor.LHS = LHS
        self.ancestor.values = list(set(self.ancestor.LHS))

        # combobox for symptom display
        self.ancestor.combo_one.configure(values=self.ancestor.values)


    def add_rule(self,name, rule, things):
        # print name,rule, things
        # self.LHS.delete(0.0, END)
        # self.RHS.delete(0.0, END)
        # self.RHS.insert(0.0, "add possible malfunction")
        # self.LHS.insert(0.0, "add sypmtom")
        # dataLHS = self.LHS.get(0.0, END)
        split_rule = rule.splitlines()
        # data = self.text_area.get(0.0, END)
        split_things = things.splitlines()
        split_rule=set(split_rule)
        split_rule=list(split_rule)
        if '' in split_rule:
                split_rule.remove('')
        split_things=set(split_things)
        split_things=list(split_things)
        if '' in split_things:
                split_things.remove('')
        # print name, split_rule, split_things
        stringRHSL = '(assert ('
        stringRHSR = '))'
        stringLHSL = '('
        stringLHSR = ')'
        RHSString = ''
        LHSString = ''
        for i in range(len(split_rule)):
            LHSString = LHSString + "   " + stringLHSL + split_rule[i].encode("utf-8") + stringLHSR + "\n"
        for j,i in enumerate(range(len(split_things))):
		if(j<len(split_things)-1):
			RHSString = RHSString + "   " + stringRHSL + split_things[i].encode("utf-8") + stringRHSR + "\n"
		else:
			RHSString = RHSString + "   " + stringRHSL + split_things[i].encode("utf-8") + stringRHSR + ")"
            # clips.BuildRule("user-rule", "(test (eq (python-call py_getvar",RHSString, "the user rule")
        #print(name)
        #print(LHSString)
        #print(RHSString)
	stringBuild = "(defrule MAIN::"+name+"\n"+LHSString+"   =>\n"+RHSString+"\n"
	print(stringBuild)
	#build(stringBuild)
	#self.ancestor.clips.SendCommand(stringBuild)
	#self.ancestor.clips.Build(stringBuild)
	#self.ancestor.clips.BuildRule(name,LHSString,RHSString)
        #clips.BuildRule(name, LHSString, RHSString)
	###PATCH
	textToSave = []
	f = open(self.ancestor.filename, 'r')
        for line in f:
            # print line
            textToSave.append(line)
        f.close()
	
	f = open(self.ancestor.filename, 'w')
        for line in textToSave:
            f.write(line)
	for line in stringBuild.splitlines():
	    f.write(line)
	    f.write("\n")
        f.close()
        self.ancestor.clips.Clear()
        self.ancestor.clips.Load(self.ancestor.filename)
	LHS, RHS = GetValues(self.ancestor.filename)
        self.ancestor.LHS = LHS
        self.ancestor.values = list(set(self.ancestor.LHS))

        # combobox for symptom display
        self.ancestor.combo_one.configure(values=self.ancestor.values)

        return


if __name__ == "__main__":
    # root window created. Here, that would be the only window, but
    # you can later have windows within windows.
    root = Tk()

    root.geometry("600x500")
    root.resizable(0, 0)

    # creation of an instance
    app = Window(root,clips)

    # mainloop
    root.mainloop()
