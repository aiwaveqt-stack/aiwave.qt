"""Task Manager class for managing tasks"""
import json
import os
from task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def load_tasks(self, filename):
        """Load tasks from file"""
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data]
                    self.next_id = len(self.tasks) + 1
            else:
                print("No previous task found, starting afresh.")
        except FileNotFoundError:
            print("No previous task found, starting afresh.")
        except json.JSONDecodeError as e:
            print(f"Error reading tasks file: {e}")
        except Exception as e:
            print(f"Unexpected Error Occurred: {e}")

    def save_tasks(self, filename):
        """Method to Save Tasks"""
        try:
            with open(filename, 'w') as f:
                task_data = [task.to_dict() for task in self.tasks]
                json.dump(task_data, f, indent=2)
        except IOError as e:
            print(f"Error saving tasks: {e}")

    def add_task(self, description):
        """Method to add task"""
        new_task = Task(self.next_id, description)
        self.next_id += 1
        self.tasks.append(new_task)
        print(f"Task added: {new_task}")

    def delete_task(self, task_id):
        """Method to remove a task"""
        self.tasks = [task for task in self.tasks if task.get_id() != task_id]
        print(f"Task with id {task_id} has been deleted.")

    def display_task(self):
        """Display all tasks"""
        if not self.tasks:
            print("No tasks available")
            return
        print("Current Task: ")
        for task in self.tasks:
            print(task)
            print("-" * 52)

    def toggle_task_completion(self, task_id):
        """Toggle the completion status of a task"""
        for task in self.tasks:
            if task.get_id() == task_id:
                task.toggle_completion()
                print(f"Toggled completion for task {task}")
                return
        print(f"Task with ID {task_id} was not found!")
