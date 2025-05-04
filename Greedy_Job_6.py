def job_schedule(jobs):
    jobs.sort(key=lambda x:x[2], reverse=True)
    max_deadline=max(job[1] for job in jobs)
    slot=[False]*max_deadline
    schedule=[None]*max_deadline
    total_profit=0

    for job in jobs:
        job_id,job_deadline,job_profit=job
        for i in range(min(job_deadline,max_deadline) -1,-1,-1):
            if not slot[i]:
                slot[i]=True
                schedule[i]=job_id
                total_profit+=job_profit
                break
    print("schedule job: ", [job for job in schedule if job])
    print("Total profit:" ,total_profit)

jobs = [
    ('J1', 2, 60),
    ('J2', 1, 10),
    ('J3', 3, 20),
    ('J4', 2, 40),
    ('J5', 1, 20)
]

job_schedule(jobs)

