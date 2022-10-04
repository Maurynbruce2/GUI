import tkinter
import tkinter.messagebox


class myGUI: 

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.topframe = tkinter.Frame(self.main_window)
        self.midframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        self.promptlabel = tkinter.Label(self.topframe, text = 'Enter a distance in kilometers')
        self.entry = tkinter.Entry(self.topframe, width = 10)
        

        self.promptlabel.pack(side = 'left')
        self.entry.pack(side = 'left')

        self.miles_var = tkinter.StringVar()

        self.desc_label = tkinter.Label(self.midframe,text = 'Converted to miles:')
        self.mile = tkinter.Label(self.midframe, textvariable=self.miles_var)

        self.desc_label.pack(side='left')
        self.mile.pack(side='left')
        

        self.topframe.pack(side='top')
        self.midframe.pack()
        self.bottomframe.pack(side='bottom')

        self.mybutton = tkinter.Button(self.main_window, text = 'Convert', command = self.convert)
        self.quitbutton = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)

        
        self.mybutton.pack(side = 'left')
        self.quitbutton.pack(side = 'right')


        tkinter.mainloop()

    def convert(self): 
        kilo = float(self.entry.get())

        miles = round(kilo*0.6214,2)

        self.miles_var.set(miles)

        #tkinter.messagebox.showinfo('Result', str(kilo) + 'kilometers is equal to ' + str(miles) + 'miles')


my_gui = myGUI()

print('I am done!')