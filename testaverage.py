import tkinter
import tkinter.messagebox

class TestInput:

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.topframe = tkinter.Frame(self.main_window)
        self.midframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        # Create Entries

        self.test1entry = tkinter.Label(self.topframe, text = 'Enter the score for test 1:')
        self.entry1 = tkinter.Entry(self.topframe, width = 10)

        self.test2entry = tkinter.Label(self.topframe, text = 'Enter the score for test 2:')
        self.entry2 = tkinter.Entry(self.topframe, width = 10)

        self.test3entry = tkinter.Label(self.topframe, text = 'Enter the score for test 3:')
        self.entry3 = tkinter.Entry(self.topframe, width = 10)

        # Pack Entries 

        self.test1entry.pack()
        self.entry1.pack()

        self.test2entry.pack()
        self.entry2.pack()

        self.test3entry.pack()
        self.entry3.pack()

        # Create Labels for Average

        self.average_var = tkinter.StringVar()

        self.desc_label = tkinter.Label(self.midframe,text = 'Average:')
        self.average = tkinter.Label(self.midframe, textvariable=self.average_var)

        # Pack Labels for Average

        self.desc_label.pack(side='left')
        self.average.pack(side='left')

        self.topframe.pack(side='top')
        self.midframe.pack()
        self.bottomframe.pack(side='bottom')

        # Create Buttons 

        self.averagebutton = tkinter.Button(self.main_window, text = 'Average', command = self.convert)
        self.quitbutton = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)

        # Pack Buttons 

        self.averagebutton.pack(side = 'left')
        self.quitbutton.pack(side = 'right')

        tkinter.mainloop()

    def convert(self): 
        total_score = float(self.entry1.get() + self.entry2.get() + self.entry3.get())

        average =(total_score/3)

        self.average_var.set(average)

test_average = TestInput()
print('I am done')

        







        

    