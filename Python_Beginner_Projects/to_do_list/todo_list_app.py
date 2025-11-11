"""TO-DO-LIST-PROGRAM"""
from task_manager import TaskManager


class TodoListApp:
    def __init__(self):
        self.task_manager = TaskManager()
        self.filename = "tasks.json"

    def menu(self):
        """Display menu and process user choice"""
        print("TO-DO-LIST-PROGRAM")
        print("-" * 49)
        print("1. ADD \n2. DELETE \n3. DISPLAY \n4. TOGGLE TASK COMPLETION \n5. SAVE AND EXIT")
        print("-" * 49)
        choice = input("Please enter an option(1-5): ")
        self.validate_choice(choice)

    def add(self):
        """Add a new task"""
        print("Enter task description: ", end="")
        print("-" * 56)
        description = input()
        print("-" * 56)
        self.task_manager.add_task(description)

    def get_id(self):
        """Get task ID from user"""
        task_id = int(input("Enter task ID: "))
        print("-" * 56)
        return task_id

    def validate_choice(self, option):
        """Validate and process user choice"""
        try:
            option = int(option)
            if option == 1:
                self.add()
            elif option == 2:
                task_id = self.get_id()
                self.task_manager.delete_task(task_id)
            elif option == 3:
                self.task_manager.display_task()
            elif option == 4:
                task_id = self.get_id()
                self.task_manager.toggle_task_completion(task_id)
            elif option == 5:
                self.task_manager.save_tasks(self.filename)
                print("Task saved successfully. Exiting....")
                exit()
            else:
                print("Invalid Input.")
        except ValueError:
            print("Invalid Input. Please enter a number.")

    def main(self):
        """Main method"""
        # Load existing tasks from file
        self.task_manager.load_tasks(self.filename)

        while True:
            self.menu()
            print()
            print("-" * 45)


if __name__ == "__main__":
    app = TodoListApp()
    app.main()
