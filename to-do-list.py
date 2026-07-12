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
        # self.window = Tk()
        # self.tasks = [] Liste für die To-Do-Elemente
        # self.task_input = StringVar()  # Variable für die Eingabe des To-Do-Elements
        # self.file_path = "todos.json"  # Pfad zur JSON-Datei für die To-Do-Liste
        # usw

        #self. create_ui()

    #def create_ui(self)
    # hier wird die Benutzeroberfläche erstellt, z.B. Labels, Buttons, Eingabefelder usw.
    # self.window.geometry("400x400")
    # self.display_label = Label(self.window, textvariable=self.text_line)
    # self.listbox = ttk.Treeview(self.window, columns=("To Dos", "Status"), show="headings")
    # self.window.title("To-Do List")
    # self.input_entry = ttk.Entry(self.window, textvariable=self.text_line)
    # self.add_button = Button(self.window, text="Add", command=self.add_todo)
    # self.remove_button = Button(self.window, text="Remove", command=self.remove_todo)

    # def add_todo(self):
    # hier wird ein neues To-Do hinzugefügt, z.B. self.listbox.insert("", "end", values=(self.text_line.get(), "Pending"))

    # def remove_todo(self):
    # hier wird ein To-Do entfernt, z.B. self.listbox.delete(self.listbox.selection())

    # def save_todos(self):
    # hier werden die To-Dos in einer JSON-Datei gespeichert, z.B. mit json.dump()
     
    # def load_todos(self):
    # hier werden die To-Dos aus einer JSON-Datei geladen, z.B. mit json.load()

    # def update_display(self):
    # hier wird die Anzeige aktualisiert, z.B. self.display_label.config(text="...")

    # def clear_input(self):
    # hier wird das Eingabefeld geleert, z.B. self.text_line.set("")

    # def mark_done(self):
    # hier wird ein To-Do als erledigt markiert, z.B. self.listbox.item(self.listbox.selection(), values=(..., "Done"))

    # def mark_pending(self):
    # hier wird ein To-Do als unerledigt markiert, z.B. self.listbox.item(self.listbox.selection(), values=(..., "Pending"))

    # def edit_todo(self):
    # hier wird ein To-Do bearbeitet, z.B. self.listbox.item(self.listbox.selection(), values=(self.text_line.get(), ...))



#-------main function-------
if __name__ == "__main__":
todolist = ToDoList()
todolist.window.mainloop()
