"""Bug class representing a single bug"""


class Bug:
    id_counter = 0  # Static counter for unique IDs

    def __init__(self, description, severity):
        Bug.id_counter += 1
        self.id = Bug.id_counter
        self.description = description
        self.status = "Open"  # e.g., "Open", "In Progress", "Resolved"
        self.severity = severity  # e.g., "Low", "Medium", "High"

    def get_id(self):
        return self.id

    def get_description(self):
        return self.description

    def get_status(self):
        return self.status

    def get_severity(self):
        return self.severity

    def set_status(self, status):
        self.status = status

    def __str__(self):
        return f"Bug ID: {self.id}, Description: {self.description}, Status: {self.status}, Severity: {self.severity}"
