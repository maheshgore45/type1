class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    max_deadline = max(jobs, key=lambda x: x.deadline).deadline
    schedule = [None] * max_deadline
    total_profit = 0

    for job in jobs:
        for i in range(job.deadline - 1, -1, -1):
            if schedule[i] is None:
                schedule[i] = job.id
                total_profit += job.profit
                break

    return schedule, total_profit

# Take user input for the jobs
num_jobs = int(input("Enter the number of jobs: "))
jobs = []
for i in range(num_jobs):
    id = i + 1
    deadline, profit = map(int, input(f"Enter deadline and profit for job {id}: ").split())
    jobs.append(Job(id, deadline, profit))

schedule, total_profit = job_scheduling(jobs)

print("Job Schedule:")
for i in range(len(schedule)):
    if schedule[i] is not None:
        print(f"Time Slot {i+1}: Job {schedule[i]}")

print("Total Profit:", total_profit)

