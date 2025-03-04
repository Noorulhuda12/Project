# To-Do List Application

#### Video Demo:  

#### Description:
This project is a simple yet functional command-line To-Do List application that allows users to manage their tasks efficiently. It provides an intuitive way to add, view, and mark tasks as done, ensuring that users can keep track of their to-do lists with ease. The application uses a JSON file for storage, allowing task data to persist between runs. Additionally, it is built with modularity in mind, featuring separate functions that facilitate easy unit testing with `pytest`.

## Features
The application comes with the following core features:

- **Add New Tasks**: Users can add tasks by providing a name and a short description.
- **View All Tasks**: The application lists all tasks, indicating whether they are completed or not.
- **Mark Tasks as Done**: Users can update the status of tasks to mark them as completed.
- **Persistent Storage**: Tasks are saved to a JSON file (`tasks.json`), ensuring that data is retained between runs.
- **Automated Testing**: The project includes test cases using `pytest` to ensure the correctness of key functions.

## Project Structure
The project is structured as follows:

- `project.py`: This is the main script that contains the core logic of the application, including user interactions and the task management functions.
- `test_project.py`: This file contains test cases for the functions in `project.py`, ensuring the application behaves as expected.
- `README.md`: Documentation for the project, explaining its purpose, features, and usage.
- `tasks.json`: A JSON file that stores task data, allowing persistence across multiple uses of the program.

## Implementation Details
### Main Components

1. **Task Management**
   - The `ToDoList` class is responsible for handling tasks, including adding, listing, and updating task statuses.
   - It interacts with the `tasks.json` file to ensure that task data is stored and retrieved correctly.

2. **Standalone Functions**
   - The application includes three standalone functions:
     - `add_task_to_list(name, description)`: Adds a task to the to-do list.
     - `mark_task_as_done(task_name)`: Marks a specific task as completed.
     - `list_tasks()`: Retrieves and displays all tasks.
   - These functions facilitate better modularity and make unit testing easier.

3. **User Interaction**
   - The `main()` function provides a command-line interface where users can interact with the application.
   - Users are given a menu to choose options such as viewing tasks, adding tasks, marking tasks as done, or exiting the program.

4. **File Handling**
   - Tasks are stored in a JSON file (`tasks.json`) to persist data across sessions.
   - The `save_tasks()` and `load_tasks()` methods handle reading from and writing to this file.
   
## Running the Project
### Prerequisites
Ensure you have Python installed on your system. You can check your Python version by running:

```sh
python --version
```
### Installation
No additional libraries are required, as the project uses Python’s built-in `json` module. Simply clone or download the project files and navigate to the project directory.

### Running the Application
To run the application, execute the following command:

```sh
python project.py
```

You will be presented with a menu where you can choose an option:

```
To-Do List:
1. View tasks
2. Add task
3. Mark task as done
4. Exit
Choose an option (1/2/3/4):
```

Follow the prompts to interact with the to-do list.

### Running Tests
To ensure the application works correctly, run the automated tests using `pytest`:

```sh
pytest
```

The test suite checks the correctness of the core functions, including adding tasks, marking tasks as done, and retrieving tasks.

## Use Cases
This application can be useful in several scenarios:
- **Personal Task Management**: Individuals can track their daily or weekly tasks efficiently.
- **Collaborative Work**: Small teams can use the application to manage shared tasks.
- **Learning Project**: Beginners in Python can use this project to understand file handling, object-oriented programming, and unit testing.

## Future Improvements
There are several ways to enhance this project:
- **Graphical User Interface (GUI)**: A simple GUI using Tkinter or PyQt could make the application more user-friendly.
- **Task Categories**: Adding categories or priority levels for tasks.
- **Due Dates & Reminders**: Implementing a feature to set due dates and reminders for tasks.
- **Cloud Storage**: Storing tasks in a database or cloud service for better accessibility.

## Conclusion
This To-Do List application is a simple yet effective tool for task management. It demonstrates fundamental programming concepts such as file handling, object-oriented programming, and automated testing. The project is structured for easy expansion, making it an excellent foundation for future enhancements.

If you're interested in contributing or improving the project, feel free to fork the repository and submit pull requests!

