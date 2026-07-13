# ----- import libraries -----
import os   
import json #für das Speichern und Laden der To-Do-Liste
from tkinter import Tk, Label, Button, StringVar
from tkinter import ttk

#------- define functions -----
class ToDoList:
    def __init__(self): # Konstruktor
        # Fenstertitel, Fenstergröße definieren
        self.text_line = StringVar()
        self.window = Tk()
        self.window.title("To-Do List")
        self.tasks = [] #Liste für die To-Do-Elemente
        self.file_path = "todos.json"  # Pfad zur JSON-Datei für die To-Do-Liste
        

        self.create_ui()
        self.load_todos()  # To-Dos aus der JSON-Datei laden, falls vorhanden

    def create_ui(self):
        self.window.geometry("400x400")
        self.display_label = Label(self.window, textvariable=self.text_line)
        self.display_label.pack(pady=10)

        self.listbox = ttk.Treeview(self.window, columns=("To Dos", "Status"), show="headings")
        self.listbox.heading("To Dos", text="To Dos")
        self.listbox.heading("Status", text="Status")
        self.window.title("To-Do List")
        self.input_entry = ttk.Entry(self.window, textvariable=self.text_line)
        self.input_entry.pack(pady=10)
        self.add_button = Button(self.window, text="Add", command=self.add_todo)
        self.add_button.pack(pady=5)
        self.remove_button = Button(self.window, text="Remove", command=self.remove_todo)
        self.remove_button.pack(pady=5)
        self.edit_button = Button(self.window, text="Edit", command=self.edit_todo)
        self.edit_button.pack(pady=5)
        self.toggle_button = Button(self.window, text="Toggle Status", command=self.toggle_status)
        self.toggle_button.pack(pady=5)

    def load_todos(self):# hier werden die To-Dos aus einer JSON-Datei geladen, z.B. mit json.load()
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                self.tasks = json.load(f)

    def add_todo(self):# hier wird ein neues To-Do hinzugefügt
        todo_text = self.text_line.get()
        self.tasks.append({
            "todo": todo_text, 
            "status": "Pending"
        })
        self.listbox.insert("", "end", values=(self.text_line.get(), "Pending"))
        self.text_line.set("")  # Eingabefeld leeren
        self.save_todos()  # To-Dos in der JSON-Datei speichern

    def remove_todo(self): # hier wird ein To-Do entfernt, z.B. 1
        if not self.listbox.selection():
            return  # Keine Auswahl, daher keine Entfernung

        selected_item = self.listbox.selection()[0]
        todo_text = self.listbox.item(selected_item, "values")[0]
        self.listbox.delete(selected_item)
        # Entferne das To-Do aus der Liste
        self.tasks = [task for task in self.tasks if task["todo"] != todo_text]
        self.save_todos()  # To-Dos in der JSON-Datei speichern

    def edit_todo(self): # hier wird ein To-Do bearbeitet, z.B. 
        if not self.listbox.selection():
            return  # Keine Auswahl, daher keine Bearbeitung
        
        selected_item = self.listbox.selection()[0]
        current_values = self.listbox.item(selected_item, "values")
        old_todo = current_values[0]
        old_status = current_values[1]
        self.text_line.set(old_todo)
        self.listbox.item(selected_item, values=(new_todo, old_status))

        for task in self.tasks: 
            if task["todo"] == old_todo:
                
                task["todo"] = new_todo
                break

        self.text_line.set("")  # Eingabefeld leeren
        self.save_todos()  # To-Dos in der JSON-Datei speichern

    def toggle_status(self): # hier wird der Status eines To-Dos geändert, z.B. von "Pending" zu "Completed" und umgekehrt
        todo_status = self.listbox.item(self.listbox.selection(), "values")[1]
        new_status = "Completed" if todo_status == "Pending" else "Pending"
        self.listbox.item(self.listbox.selection(), values=(self.listbox.item(self.listbox.selection(), "values")[0], new_status))

    def update_display(self): # hier wird die Anzeige der To-Dos aktualisiert, z.B. self.listbox.insert("", "end", values=(todo, status))
        self.listbox.delete(*self.listbox.get_children())
        for task in self.tasks:
            self.listbox.insert("", "end", values=(task["todo"], task["status"]))

    def save_todos(self):# hier werden die To-Dos in einer JSON-Datei gespeichert
        with open(self.file_path, "w") as f:
            json.dump(self.tasks, f)

    def clear_input(self):
        self.text_line.set("")
     


#-------main function-------
if __name__ == "__main__":
todolist = ToDoList()
todolist.window.mainloop()
