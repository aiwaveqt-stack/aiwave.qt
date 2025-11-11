"""Task class representing a single task"""


class Task:
    def __init__(self, task_id, description):
        self.id = task_id
        self.description = description
        self.completed = False

    def get_id(self):
        return self.id

    def get_description(self):
        return self.description

    def is_completed(self):
        return self.completed

    def toggle_completion(self):
        self.completed = not self.completed

    def __str__(self):
        status = "X" if self.completed else " "
        return f"[{status}] {self.description}"

    def to_dict(self):
        """Convert task to dictionary for serialization"""
        return {
            'id': self.id,
            'description': self.description,
            'completed': self.completed
        }

    @staticmethod
    def from_dict(data):
        """Create task from dictionary"""
        task = Task(data['id'], data['description'])
        task.completed = data['completed']
        return task
