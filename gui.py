import sys
import os
import subprocess
from capturer import CaptureOutput
from cStringIO import StringIO

if sys.version_info[0] < 3:
    # python 2
    from Tkinter import *
    import tkFileDialog as filedialog
    import ttk
    import tkMessageBox as mBox
    # import clips6
    import clips
    clips.Reset()

else:
    # python 3
    from tkinter import *
    from tkinter import filedialog
    from tkinter import ttk
    from tkinter import messagebox as mBox

def GetValues(filename='rulez.clp'):
	f = open(filename, 'r')

	flagLHS = False
	flagRHS = False

	LHS = []
	RHS = []
	for line in f:
		#if line not in ['\n', '\r\n']:
		#	print line[0]+line[1]
		if "=>" in line:
			flagLHS = False
		if flagLHS:
			#print line
			LHS.append(line.strip()[1:-1])	
		if "defrule" in line:
			flagLHS = True

		if "defrule" in line:
			flagRHS = False
		if flagRHS:
			#print line
			line = line.strip()
			index = line.find(")))")
			if index==-1:
				index = line.find("))")
			if line != "":
				RHS.append(line[9:index])	
		if "=>" in line:
			flagRHS = True
		#re.search(r'\s[\s]*\s', x, re.S)
	f.close()
	return LHS,RHS

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
        rule_menu = Menu(menu, tearoff=1)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit

        # added "Rules" to our menu
        menu.add_cascade(label="Rules", menu=rule_menu)
        rule_menu.add_command(label="Add new...", command=self.ruleWin)

        # Add another Menu to the Menu Bar and an item
        help_menu = Menu(menu, tearoff=1)
        menu.add_cascade(label="Help", menu=help_menu)
        #help_menu.add_command(label="Presentation", command=self.openPDF("filename.pdf"))
        #help_menu.add_command(label="Documentation", command=self.openPDF("filename.pdf"))
        help_menu.add_separator()
        help_menu.add_command(label="About", command=self.msgBox)

        Label(self.master, text="Select symptoms:").pack(side=TOP)#.grid(column=0, row=0)

        #combo_master = Combos(self.master)
        self.symptom = StringVar()
        self.combo_one = ttk.Combobox(self.master, textvariable=self.symptom, state='readonly')

	LHS,RHS=GetValues('rulez.clp')
	self.filename='rulez.clp'
	self.LHS=LHS
        self.values = list(set(self.LHS))#(1, 2, 3, 4, 5)
        self.combo_one.configure(values=self.values)
        self.combo_one.pack(fill=BOTH, padx=20, pady=10, ipadx=5, ipady=5, side=TOP)

        #self.symptom2 = StringVar()
        #self.combo_two = ttk.Combobox(self.master, textvariable=self.symptom2, state='disabled')
        #self.combo_two.configure(values=values)
        #self.combo_two.pack(fill=BOTH, padx=20, pady=10, ipadx=5, ipady=5, side=TOP)

        self.del_button = Button(self.master, text='delete symptom', width=15, height=2,
                          command=lambda: self.remove_simptom(self.combo_one.get()))
        self.del_button.pack()
	self.run_button = Button(self.master, text='run', width=15, height=2,
                          command=lambda: self.run())
        self.run_button.pack()

        # add separator between comboboxes and text area
        ttk.Separator(self.master, orient=HORIZONTAL).pack(pady=10, padx=5, ipadx=300, ipady=5)

        # text area where user will have preview of possible symptoms
        self.text_area = Text(self.master, state='disable')
        self.text_area.pack()

        value = self.combo_one.get()
        self.combo_one.bind('<<ComboboxSelected>>', self.add_simptom)
	clips.Load('rulez.clp')

    def run(self):
	sys.stdout = open("logfile", "w")
	self.text_area.configure(state='normal')
        data = self.text_area.get(0.0, END)
        split_data = data.split("\n")
        self.text_area.delete(0.0, END)
        # look if there is already that value inside textbox and if it is, do not add it (remove it)
        #print(len(split_data))
        for inputs in split_data:
	    inputs = inputs.encode("utf-8")
	    if inputs != "":
		#print inputs
		if (inputs != "\n"):
		     clips.Assert("("+inputs+")")
		     #in2 = " ".join(inputs.split())
		     #self.text_area.insert(END, inputs.strip() + "\n")
	split_data_edited = []
	for line in split_data:
		line = line.encode("utf-8")
		if line != "":
			if (line != "\n"):
				split_data_edited.append(line)
		
	clips.Run()
	
	lines = []
	answer = []
	clips.PrintFacts()
	"""
	with CaptureOutput() as capturer:
		clips.PrintFacts()
		lines = capturer.get_lines()
	"""	
	#print lines
	sys.stdout = open("/dev/stdout", "w")
	f = open("logfile", 'r')
	for line in f:
		lines.append(line)
		
	for line in lines[1:-1]:
		#print line
		line = line.encode("utf-8")
		index = line.find(")")
		line = line[9:index]
		#print line
		if line not in split_data_edited:
			answer.append(line)
	for line in answer:
		self.text_area.insert(END, line.strip() + "\n")
	clips.Reset()
	LHS,RHS=GetValues(self.filename)
	self.values = list(set(LHS))#(1, 2, 3, 4, 5)
        self.combo_one.configure(values=self.values)
	#clips.Assert("(Engine fails to start)")

    def on_selection(self, event=None):
        # self.text_area.insert(END, "Just a text Widget\nin two lines\n")
        print self.combo_one.get()
        self.combo_two.configure(state='readonly')

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
            if (inputs == value):
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
	#print split_data
        self.text_area.delete(0.0, END)
        # look if there is already that value inside textbox and if it is, do not add it (remove it)
        #print(len(split_data))
        for inputs in split_data:
	    inputs = inputs.encode("utf-8")
            if (inputs != value):
		if inputs != "":
			#print inputs
		        if (inputs != "\n"):
		            #in2 = " ".join(inputs.split())
		            self.text_area.insert(END, inputs.strip() + "\n")
        self.text_area.configure(state='disable')

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
        app = ParametersWin(gringo,self)

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
            [("CLISP files", "*.clp"),
             ("All files", "*.*")]
        filename = filedialog.askopenfilename(filetypes=mask, title="Select file")
	clips.Load(filename)
	self.filename=filename
	LHS,RHS=GetValues(filename)
	self.values = list(set(LHS))#(1, 2, 3, 4, 5)
        self.combo_one.configure(values=self.values)

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
	clips.Run()
	clips.Save("rulez.clp")
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


class Combo:
    def __init__(self, parent):
        self.parent = parent;
        self.values = StringVar();
        self.make_combobox(self.parent, self.values)
        self.add_symptoms(self.values)

    def make_combobox(self, parent, values):
        newCombo = ttk.Combobox(self.parent, textvariable=self.values)
        newCombo.pack(fill=BOTH, padx=20, pady=10, ipadx=5, ipady=5, side=TOP)
        return newCombo

    def add_symptoms(self, symptoms):
        newCombo = ttk.Combobox(self.parent, textvariable=self.values)
        newCombo['values'] = symptoms


class Combos:
    def __init__(self, parent):
        self.parent = parent

    def add_combo(self, symptom):
        newCombo = ttk.Combobox(self.parent, textvariable=symptom)
        newCombo.pack(fill=BOTH, padx=20, pady=10, ipadx=5, ipady=5, side=TOP)
        # newCombo.grid(column=c, row=r)
        # newCombo.current(0)
        return newCombo


class ParametersWin(Frame):

    def __init__(self, parent, ancestor):
        Frame.__init__(self, parent)
        self.ancestor = ancestor
	self.values = ancestor.values
	#print ancestor.values
        label = Label(self, text="Edit rules")
	self.init_window()        
	label.pack(side="top", fill="x", pady=10)

    def init_window(self):
        # changing the title of our master widget
        self.master.title("Edit rules")
        self.pack(fill=BOTH, expand=1)

        self.tabControl = ttk.Notebook(self) # create Tab Control
        self.tabAdd = Frame(self.tabControl)  # Create a tab
        self.tabControl.add(self.tabAdd, text=' Add rule ')  # Add the tab
        self.tabEdit = Frame(self.tabControl) # Create a tab
        self.tabControl.add(self.tabEdit, text=' Edit rule ')  # Add the tab
        #self.tabTwo = Frame(self.tabControl)  # Create a tab
        #self.tabControl.add(self.tabTwo, text=' Monetary Incentive Delay ')  # Add the tab
        self.tabControl.pack(side="top",expand=1, fill="both")  # Pack to make visible

	################## TAB ADD
        # entry to add malfunction
        self.e = Entry(self.tabAdd)
        self.e.pack()#side="top", padx=50, pady=50)
	self.LHS = Text(self.tabAdd,height=12, width=50)
        self.LHS.pack()#x=0,y=0, height=200, width=200)
	self.e.delete(0, END)
        self.e.insert(0, "add-rule-name")

        self.RHS = Text(self.tabAdd,height=12, width=50)
        self.RHS.pack()#x=101,y=101, height=200, width=200)

	self.but = Button(self.tabAdd, text='add', width=15, height=5,
                             command=lambda: self.add_rule(self.e.get(),self.LHS.get(0.0, END), self.RHS.get(0.0, END)))
        self.but.pack(side="bottom", padx=0, pady=0)
	
	self.RHS.insert(0.0, "add possible malfunction")
        self.LHS.insert(0.0, "add sypmtom")
	
	################## TAB EDIT
	#self.symptom = StringVar()
        #self.combo_one = ttk.Combobox(self.tabEdit, textvariable=self.symptom, state='readonly')
        #self.combo_one.configure(values=self.values)
	#self.combo_one.pack()
	#Load the whole file in a text
	self.file = Text(self.tabEdit,height=28, width=65)
        self.file.pack()#x=101,y=101, height=200, width=200)
	self.fileButton = Button(self.tabEdit,text="Edit",command= lambda: self.editFile(self.file.get(0.0, END)))
	self.fileButton.pack()
	f = open(self.ancestor.filename, 'r')
	for line in f:
		#print line
		self.file.insert(END,line)
	f.close()
	
    def editFile(self,textToSave):
	f = open(self.ancestor.filename, 'w')
	for line in textToSave:
		f.write(line)
	f.close()
	clips.Clear()
	clips.Load(self.ancestor.filename)


    def add_rule(self,name, rule, things):
        #print name,rule, things
        #self.LHS.delete(0.0, END)
        #self.RHS.delete(0.0, END)
	#self.RHS.insert(0.0, "add possible malfunction")
        #self.LHS.insert(0.0, "add sypmtom")
	#dataLHS = self.LHS.get(0.0, END)
        split_rule = rule.splitlines()
	#data = self.text_area.get(0.0, END)
        split_things = things.splitlines()
	print name,split_rule,split_things
	stringRHSL = '(assert ('
	stringRHSR = '))'
	stringLHSL = '('
	stringLHSR = ')'
	RHSString = ''
	LHSString = ''
	for i in range(len(split_rule)):
		LHSString=LHSString+stringLHSL+split_rule[i].encode("utf-8")+stringLHSR
	for i in range(len(split_things)):
		RHSString=RHSString+stringRHSL+split_things[i].encode("utf-8")+stringRHSR
	#clips.BuildRule("user-rule", "(test (eq (python-call py_getvar",RHSString, "the user rule")
	clips.BuildRule(name, LHSString,RHSString, "the user rule")
        pass

if __name__ == "__main__":
    # root window created. Here, that would be the only window, but
    # you can later have windows within windows.
    root = Tk()

    root.geometry("600x500")

    # creation of an instance
    app = Window(root)

    # mainloop
    root.mainloop()
