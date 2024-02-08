class Task:
    def __init__(self, name, wcet, period, deadline=float('inf')):
        self.name = name
        self.wcet = wcet
        self.period = period
        self.deadline = deadline

def calculate_analysis(tasks):
    for task in tasks:
        wcrt = task.wcet
        bwcrt = task.wcet
        q_wcet = task.wcet

        for other_task in tasks:
            if other_task != task:
                q_wcet += (1 / other_task.period) * other_task.wcet
                bwcrt += (q_wcet - task.wcet) * other_task.wcet

        print(f"Analysis of Result:")
        print(f"• {task.name} in priority {task.period}: wcrt={wcrt}")
        print(f"bwcrt=q*WCET:{task.period}*{bwcrt}={bwcrt}")
        print(f"q*WCET:{task.period}*{q_wcet}={q_wcet}\n")

# Define the tasks
road1_light = Task("Traffic Light Road 1", 7, 20, 20)
road2_light = Task("Traffic Light Road 2", 7, 20, 20)
ambulance = Task("Ambulance", 5, 15, 80)  # Assuming a WCET of 2 for the ambulance

# Perform the analysis
calculate_analysis([road1_light, road2_light, ambulance])




