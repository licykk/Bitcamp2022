class Task:
    def __init__(self, id, name, priority, assignment, due_date, status):
        self.id = id
        self.name = name
        self.priority = priority
        self.assignment = assignment
        self.due_date = due_date
        self.status = status
    
class File:
    def __init__(self, id, name, file):
        self.id = id
        self.name = name
        self.file = file
    
class Project:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.files = []
        self.tasks = []
        self.reminders = []
        self.meeting_notes = []
        self.calendars = []

manager = {
    "general": Project("general")
}
