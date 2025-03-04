import pytest
from project import ToDoList, add_task_to_list, mark_task_as_done, list_tasks

@pytest.fixture
def todolist():
    """Fixture to create a temporary ToDoList instance for testing."""
    return ToDoList("test_tasks.json")

def test_add_task_to_list(todolist):
    """Test adding a task."""
    response = add_task_to_list(todolist, "Test Task", "This is a test.")
    assert response == "Task 'Test Task' added."
    assert len(todolist.get_tasks()) == 1

def test_mark_task_as_done(todolist):
    """Test marking a task as done."""
    add_task_to_list(todolist, "Test Task", "This is a test.")
    response = mark_task_as_done(todolist, "Test Task")
    assert response == "Task 'Test Task' marked as done."
    assert todolist.get_tasks()[0].done

def test_list_tasks(todolist):
    """Test listing tasks."""
    add_task_to_list(todolist, "Task 1", "Description 1")
    add_task_to_list(todolist, "Task 2", "Description 2")
    expected_output = "- Task 1: Description 1 [❌]\n- Task 2: Description 2 [❌]"
    assert list_tasks(todolist) == expected_output
