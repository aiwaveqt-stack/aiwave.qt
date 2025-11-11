"""Bug Tracking System"""
from bug import Bug


class BugTracker:
    def __init__(self):
        self.bugs = []

    def add_bug(self, description, severity):
        """Add a new bug"""
        new_bug = Bug(description, severity)
        self.bugs.append(new_bug)
        print("Bug added successfully!")

    def view_bugs(self):
        """View all bugs"""
        if not self.bugs:
            print("No bugs found.")
            return

        print("List of Bugs:")
        for bug in self.bugs:
            print(bug)

    def update_bug_status(self, bug_id, new_status):
        """Update bug status"""
        for bug in self.bugs:
            if bug.get_id() == bug_id:
                bug.set_status(new_status)
                print("Bug status updated successfully!")
                return
        print(f"Bug with ID {bug_id} not found.")


def main():
    """Main function to run the bug tracker"""
    tracker = BugTracker()

    while True:
        print("\n" + "=" * 50)
        print("Bug Tracking System")
        print("=" * 50)
        print("1. Add Bug")
        print("2. View Bugs")
        print("3. Update Bug Status")
        print("4. Exit")
        print("=" * 50)

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                description = input("Enter bug description: ")
                severity = input("Enter severity (Low/Medium/High): ")
                tracker.add_bug(description, severity)
            elif choice == 2:
                tracker.view_bugs()
            elif choice == 3:
                bug_id = int(input("Enter bug ID: "))
                new_status = input("Enter new status (Open/In Progress/Resolved): ")
                tracker.update_bug_status(bug_id, new_status)
            elif choice == 4:
                print("Exiting Bug Tracking System...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
