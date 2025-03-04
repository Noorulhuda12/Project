import json
from typing import List

class Task:
    """Class to represent a task."""
    def __init__(self, name: str, description: str, done: bool = False):
        self.name = name
        self.description = description
        self.done = done

    def mark_done(self):
        """Mark the task as done."""
        self.done = True

    def __repr__(self):
        return f"Task(name={self.name}, description={self.description}, done={self.done})"

class ToDoList:
    """Class to represent the to-do list."""
    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, name: str, description: str):
        """Add a new task."""
        task = Task(name, description)
        self.tasks.append(task)
        self.save_tasks()

    def mark_task_done(self, task_name: str):
        """Mark a task as done by its name."""
        for task in self.tasks:
            if task.name == task_name and not task.done:
                task.mark_done()
                self.save_tasks()
                return True
        return False

    def get_tasks(self) -> List[Task]:
        """Get all tasks."""
        return self.tasks

    def save_tasks(self):
        """Save tasks to a JSON file."""
        with open(self.filename, "w") as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_tasks(self) -> List[Task]:
        """Load tasks from a JSON file."""
        try:
            with open(self.filename, "r") as file:
                tasks_data = json.load(file)
                return [Task(**task) for task in tasks_data]
        except FileNotFoundError:
            return []

def main():
    """Main function to interact with the to-do list."""
    todolist = ToDoList()
    
    while True:
        print("\nTo-Do List:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")

        if choice == "1":
            print("\nTasks:")
            tasks = todolist.get_tasks()
            if not tasks:
                print("No tasks found!")
            for task in tasks:
                print(task)

        elif choice == "2":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            todolist.add_task(name, description)
            print(f"Task '{name}' added.")

        elif choice == "3":
            task_name = input("Enter task name to mark as done: ")
            if todolist.mark_task_done(task_name):
                print(f"Task '{task_name}' marked as done.")
            else:
                print(f"Task '{task_name}' not found or already done.")

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
