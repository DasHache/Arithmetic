import Tkinter as tk
import random
import time

class App(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createLogic()
        self.createInterface()

    def initializeLogic(self):
        self.num1.set(random.randint(1,100))
        self.num2.set(random.randint(1,100))
        self.answer.set("< your answer here >")

    def createLogic(self):
        self.num1 = tk.StringVar()
        self.num2 = tk.StringVar()
        self.answer = tk.StringVar()

        self.initializeLogic()

    def initializeInterface(self):
        self.e_answer.focus_set()
        self.e_answer.selection_range(0, tk.END) 

    def createInterface(self):
        self.label_num1 = tk.Label(self, textvariable=self.num1)
        self.label_num1.pack()

        self.op = tk.Label(self)
        self.op['text'] = "+"
        self.op.pack()

        self.label_num2 = tk.Label(self, textvariable=self.num2)
        self.label_num2.pack()

        self.eq = tk.Label(self)
        self.eq['text'] = "="
        self.eq.pack()

        self.e_answer = tk.Entry(self, textvariable=self.answer, justify='center')
        self.e_answer.pack()
        self.e_answer.bind("<Return>", self.my_callback_function_ENTER)

        self.mark = tk.Label(self)
        self.mark['text'] = "?"
        self.mark.pack()

        self.initializeInterface()

    def my_callback_function_ENTER(self,event):
        print "pressed", repr(event.char)

        n1 = self.num1.get()
        print "num1 = ", n1

        n2 = self.num2.get()
        print "num2 = ", n2

        ans = self.answer.get()
        print "your answer is: ", ans

        res = str( int(n1) + int(n2) )
        print "correct result is: ", res
        
        res_string = n1+'+'+n2+'='+ans
        if int(ans) == int(res):
            self.mark['text'] = 'CORRECT: ' + res_string
            self.mark['bg'] = 'Green'
        else:
            self.mark['text'] = 'WRONG: ' + res_string
            self.mark['bg'] = 'Red'

        self.initializeLogic()
        self.initializeInterface()

root = tk.Tk()
app = App(master=root)
app.mainloop()
