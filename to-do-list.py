# ----- import libraries -----
import os   
import json #für das Speichern und Laden der To-Do-Liste
from tkinter import Tk, Label, Button, StringVar
from tkinter import ttk

#------- define functions -----
class ToDoList:
    def __init__(self): # Konstruktor
        # Fenstertitel, Fenstergröße definieren
        # Startvariablen initialisieren: self.text_line = StringVar()
        # usw

        #self. create_ui()

    #def create_ui(self)
    # hier wird die Benutzeroberfläche erstellt, z.B. Labels, Buttons, Eingabefelder usw.
    # self.window = Tk()
    # self.window.title("To-Do List")



#-------main function-------
if __name__ == "__main__":
todolist = ToDoList()
todolist.window.mainloop()
