import Tkinter as tk

class App(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createTheApp()

    def createTheApp(self):
        self.button = tk.Button(self)
        self.button['text'] = "Button Name"
        self.button.pack()


root = tk.Tk()
app = App(master=root)
app.mainloop()
