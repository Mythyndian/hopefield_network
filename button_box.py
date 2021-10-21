import tkinter as tk

class ButtonBox:
    def __init__(self, id, button):
        self.id = id
        self.value = 0
        self.button = button

    def change_color(self,event=None):
        if self.value == 0:
            self.button.configure(bg='black')
            self.value = 1
        else:
            self.button.configure(bg='white')
            self.value = 0
