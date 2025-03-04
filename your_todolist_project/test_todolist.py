# test_todolist.py
import pytest
from your_todolist_project.todolist import Task, ToDoList

def test_task_creation():
    """Test creation of Task."""
    task = Task(name="Test task", description="This is a test task")
    assert task.name == "Test task"
    assert task.description == "This is a test task"
    assert task.done == False

def test_add_task():
    """Test adding a task to ToDoList."""
    todolist = ToDoList(filename="test_tasks.json")
    todolist.add_task("Buy groceries", "Buy milk, eggs, and bread.")
    assert len(todolist.get_tasks()) == 1
    assert todolist.get_tasks()[0].name == "Buy groceries"
    assert todolist.get_tasks()[0].description == "Buy milk, eggs, and bread."

def test_mark_task_done():
    """Test marking a task as done."""
    todolist = ToDoList(filename="test_tasks.json")
    
    # Ensure test file is empty
    todolist.tasks = []  
    todolist.save_tasks()  # Save the empty state
    
    todolist.add_task("Clean house", "Vacuum the living room and wash dishes.")
    todolist.mark_task_done("Clean house")
    
    assert todolist.get_tasks()[0].done == True


def test_load_tasks_from_file():
    """Test loading tasks from file."""
    todolist = ToDoList(filename="tasks.json")

    # Ensure at least one task exists
    if len(todolist.get_tasks()) == 0:
        todolist.add_task("Test Task", "This is a test task.")
    
    todolist.save_tasks()  # Save the task
    
    # Reload and test
    reloaded_todolist = ToDoList(filename="tasks.json")
    tasks = reloaded_todolist.get_tasks()
    
    assert len(tasks) > 0
    assert tasks[0].name == "Test Task"


def test_task_not_found():
    """Test marking a non-existent task as done."""
    todolist = ToDoList(filename="test_tasks.json")
    result = todolist.mark_task_done("Non-existent task")
    assert result == False

