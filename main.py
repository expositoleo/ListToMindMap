import tkinter as tk
import text_manager as tm


class Window(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pos = tk.CENTER
        self.master.title("MindMap Maker")
        c = tk.Canvas()
        self.pack(fill=tk.BOTH, expand=1)


root = tk.Tk()
mainapp = Window(root)
root.geometry("%dx%d" % (535, 380))

mainapp.mainloop()
