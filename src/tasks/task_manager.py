class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, task_name):
        self.tasks.append(task_name)
        print(f"Task '{task_name}' created.")

    def delete_task(self, task_name):
        if task_name in self.tasks:
            self.tasks.remove(task_name)
            print(f"Task '{task_name}' deleted.")
        else:
            print(f"Task '{task_name}' not found.")

    def execute_task(self, task_name):
        if task_name in self.tasks:
            print(f"Executing task '{task_name}'...")
        else:
            print(f"Task '{task_name}' not found.")