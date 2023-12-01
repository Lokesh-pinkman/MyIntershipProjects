import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.todo_list = ToDoList()

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=3, padx=10, pady=10)

        self.display_button = tk.Button(root, text="Display Tasks", command=self.display_tasks)
        self.display_button.grid(row=1, column=0, padx=10, pady=10, columnspan=4)

        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=10, pady=10, columnspan=4)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.grid(row=3, column=0, padx=10, pady=10, columnspan=4)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=4, column=0, padx=10, pady=10, columnspan=4)

    def add_task(self):
        description = self.task_entry.get()
        self.todo_list.add_task(description)
        messagebox.showinfo("Success", "Task added successfully!")
        self.task_entry.delete(0, tk.END)

    def display_tasks(self):
        tasks = self.todo_list.get_tasks_as_string()
        messagebox.showinfo("Tasks", tasks)

    def complete_task(self):
        try:
            task_index = int(simpledialog.askstring("Complete Task", "Enter the task number you want to mark as completed:"))
            self.todo_list.complete_task(task_index)
            messagebox.showinfo("Success", "Task marked as completed!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid task number.")

    def update_task(self):
        try:
            task_index = int(simpledialog.askstring("Update Task", "Enter the task number you want to update:"))
            new_description = simpledialog.askstring("Update Task", "Enter new description:")
            self.todo_list.update_task(task_index, description=new_description)
            messagebox.showinfo("Success", "Task updated successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid task number.")

    def remove_task(self):
        try:
            task_index = int(simpledialog.askstring("Remove Task", "Enter the task number you want to remove:"))
            self.todo_list.remove_task(task_index)
            messagebox.showinfo("Success", "Task removed successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid task number.")


class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, description):
        task = {"description": description}
        self.tasks.append(task)

    def get_tasks_as_string(self):
        tasks_str = "Tasks:\n"
        for i, task in enumerate(self.tasks, start=1):
            tasks_str += f"{i}. {task['description']}\n"
        return tasks_str

    def complete_task(self, task_index):
        completed_task = self.tasks.pop(task_index - 1)
        self.completed_tasks.append(completed_task)

    def update_task(self, task_index, description):
        self.tasks[task_index - 1]['description'] = description

    def remove_task(self, task_index):
        del self.tasks[task_index - 1]


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
