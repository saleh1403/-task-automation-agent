import schedule
import time

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, interval):
        self.tasks.append((task, interval))
        schedule.every(interval).seconds.do(task)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == '__main__':
    scheduler = TaskScheduler()

    def example_task():
        print('Task executed!')

    scheduler.add_task(example_task, 10)  # Execute the example_task every 10 seconds
    scheduler.run()