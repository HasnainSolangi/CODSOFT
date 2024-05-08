# Task_002 - To-Do List

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3 as sql

class ToDoListManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Solangi To-Do List Manager")
        self.root.geometry("500x600+500+200")
        self.root.resizable(0, 0)
        self.root.configure(bg="#C4E538")

        self.connection = sql.connect('listOfTasks.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)')

        self.create_layout()

    def create_layout(self):
        header_frame = tk.Frame(self.root, bg="#3B5998") 
        header_frame.pack(fill="x")

        ttk.Label(header_frame, text="To-Do List", font=("Arial", 30, "bold"), background="#3B5998", foreground="#FFFFFF").pack(pady=10)

        main_frame = tk.Frame(self.root, bg="#F4B400")  # Main frame color to yellowish
        main_frame.pack(expand=True, fill="both")

        left_frame = tk.Frame(main_frame, bg="#FF6B6B", padx=20, pady=20)  # left frame color to redish
        left_frame.pack(side="left", fill="both", expand=True)

        ttk.Label(left_frame, text="Enter the Task:", font=("Arial", 14, "bold"), background="#FF6B6B", foreground="#FFFFFF").pack()

        self.task_entry = ttk.Entry(left_frame, font=("Arial", 12))
        self.task_entry.pack(pady=10)

        ttk.Button(left_frame, text="Add Task", command=self.add_task).pack(pady=5)
        ttk.Button(left_frame, text="Delete Task", command=self.delete_task).pack(pady=5)

        right_frame = tk.Frame(main_frame, bg="#9B51E0", padx=20, pady=20)  # Changed right frame color to purple
        right_frame.pack(side="right", fill="both", expand=True)

        self.task_listbox = tk.Listbox(right_frame, width=30, height=15, font=("Arial", 12), background="#9B51E0", foreground="#FFFFFF", selectbackground="#3B5998", selectforeground="#FFFFFF")
        self.task_listbox.pack(pady=10)

        self.retrieve_database()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.cursor.execute('INSERT INTO tasks VALUES (?)', (task,))
            self.connection.commit()
            self.task_listbox.insert('end', task)
            self.task_entry.delete(0, 'end')
        else:
            messagebox.showinfo('Error', 'Field is Empty.')

    def delete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            task = self.task_listbox.get(selection)
            self.cursor.execute('DELETE FROM tasks WHERE title = ?', (task,))
            self.connection.commit()
            self.task_listbox.delete(selection)
        else:
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

    def retrieve_database(self):
        for row in self.cursor.execute('SELECT title FROM tasks'):
            self.task_listbox.insert('end', row[0])

if __name__ == "__main__":
    guiWindow = tk.Tk()
    app = ToDoListManager(guiWindow)
    guiWindow.mainloop()
