from tkinter import *
from venv_control import *


class MainWindows():

    def __init__(self, root):
        self.root = root
        self.root.geometry("467x205+507+284")
        
        self.frame = Frame(self.root)
        self.frame_auxiliar = Frame(self.root)
        self.frame_list_box = Frame(self.frame_auxiliar)

        self.scrollbar = Scrollbar(self.frame_list_box)
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        self.lb_venv = Label(self.frame)
        self.lb_message = Label(self.frame_auxiliar, wrap=200)

        self.list_box = Listbox(self.frame_list_box, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.list_box.yview)

        self.button = Button(self.frame_auxiliar)

        self.initialize()
        self.populate_list_box()
        self.pack_frames()
        self.pack_widgets()


    def initialize(self):
        self.lb_venv['text'] = get_sublime_text_venv()
        self.button['command'] = self.button_click
        self.button['text'] = "Alterar Venv"

    def populate_list_box(self):
        venvs = get_venvs()
        for venv in venvs:
            self.list_box.insert("end", venv)
            self.list_box.config(width=0)


    def pack_frames(self):
        self.frame.pack(pady=5, padx=5)
        self.frame_auxiliar.pack(fill=BOTH, pady=5, padx=5)
        self.frame_list_box.grid(row=1, column=0, rowspan=5, pady=[0,5])

    def pack_widgets(self):
        self.lb_venv.grid(row=0, column=0, columnspan=5, pady=[0,5])
        self.list_box.grid(row=0, column=0, sticky="nswe")
        self.button.grid(row=5, column=1)
        self.lb_message.grid(row=1, column=1, columnspan=5, sticky="we")

    def button_click(self):
        venv = self.list_box.get(ACTIVE)
        set_sublime_text_venv(venv)
        self.lb_venv['text'] = get_sublime_text_venv()
        self.lb_message['text'] = f"Ambiente virtual alterado para: {venv}"
        


if __name__ == '__main__':
    root = Tk()
    MainWindows(root)
    root.mainloop()
