import time
import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd

class Task:
    def __init__(self, name, period, deadline, execution_time):
        self.name = name
        self.period = period
        self.deadline = deadline
        self.next_release_time = time.time() + period
        self.execution_time = execution_time
        self.execution_times = []

    def execute(self, current_time):
        self.execution_times.append(current_time)
        current_time_seconds = int(current_time)  # Extracting the integer part (seconds)
        last_three_digits = current_time_seconds % 1000  # Extracting the last three digits
        print(f"{self.name} is executing at time {last_three_digits}")

    def update_next_release_time(self):
        self.next_release_time += self.period

def visualize_execution(tasks, num_periods):
    replicated_tasks = []
    for i in range(1, num_periods):
        replicated_tasks.extend(
            {
                "Task": task.name,
                "Start": task.execution_times[-1],
                "Finish": task.execution_times[-1] + task.period,
            }
            for task in tasks
        )

    df = pd.DataFrame(replicated_tasks)
    bar_height = 0.1

    fig, ax = plt.subplots(figsize=(10, bar_height * len(df["Task"].unique())))

    ax.set_yticks([i * bar_height + bar_height / 2 for i in range(len(df["Task"].unique()))])
    ax.set_yticklabels(df["Task"].unique())

    for i, task in enumerate(df["Task"].unique()):
        task_df = df[df["Task"] == task]
        ax.broken_barh(
            [(start, finish - start) for start, finish in zip(task_df["Start"], task_df["Finish"])],
            (i * bar_height, bar_height),
            facecolors=["blue", "orange", "green"],
        )

    ax.set_xlabel("Time")
    ax.set_title(f"Scheduling Visualization ({num_periods} Periods)")

    plt.show()

def edf_scheduler(tasks, simulation_time):
    start_time = time.time()

    while time.time() - start_time < simulation_time:
        current_time = time.time()
        ready_tasks = [task for task in tasks if current_time >= task.next_release_time]

        if ready_tasks:
            earliest_deadline_task = min(ready_tasks, key=lambda task: task.deadline)
            earliest_deadline_task.execute(current_time)
            earliest_deadline_task.update_next_release_time()

        for task in tasks:
            if task.next_release_time <= current_time:
                task.execute(current_time)
                task.update_next_release_time()

        time.sleep(1)

    visualize_execution(tasks, int(simulation_time / min(task.period for task in tasks)))

def rms_scheduler(tasks, simulation_time):
    start_time = time.time()

    while time.time() - start_time < simulation_time:
        current_time = time.time()
        ready_tasks = [task for task in tasks if current_time >= task.next_release_time]

        if ready_tasks:
            highest_priority_task = min(ready_tasks, key=lambda task: task.period)
            highest_priority_task.execute(current_time)
            highest_priority_task.update_next_release_time()

        for task in tasks:
            if task.next_release_time <= current_time:
                task.execute(current_time)
                task.update_next_release_time()

        time.sleep(1)

    visualize_execution(tasks, int(simulation_time / min(task.period for task in tasks)))

def main_edf():
    road1_light = Task("Traffic Light Road 1", 20, 20, 8)
    road2_light = Task("Traffic Light Road 2", 20, 20, 8)
    ambulance = Task("Ambulance", 20, 20, 2)

    tasks = [road1_light, road2_light, ambulance]

    edf_scheduler(tasks, simulation_time=300)

def main_rms():
    road1_light = Task("Traffic Light Road 1", 20, 20, 5)
    road2_light = Task("Traffic Light Road 2", 40, 20, 5)
    ambulance = Task("Ambulance", 80, 10, 5)

    tasks = [road1_light, road2_light, ambulance]

    rms_scheduler(tasks, simulation_time=300)

if __name__ == "__main__":
    main_edf()  
    # Uncomment the line below to run RMS scheduler
    # main_rms()
