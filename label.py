import tkinter


class myGUI: 

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.label1 = tkinter.Label(self.main_window, text = 'Hello World!')
        self.label2 = tkinter.Label(self.main_window, text = 'This is my GUI program')

        self.label1.pack(side = 'left')
        self.label2.pack(side = 'bottom')

        self.label1.pack()
        self.label2.pack()


        tkinter.mainloop()


my_gui = myGUI()

print('I am done!')