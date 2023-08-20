from datetime import datetime, timedelta
import random
import subprocess
import os

def generate_schedule():
    start_time = datetime.strptime("08:00", "%H:%M")
    end_time = datetime.strptime("21:00", "%H:%M")
    time_slots = [start_time]

    for _ in range(6):  # 6 more times to generate, as we already have the start time
        # Add randomness to the time between cron jobs
        minutes_randomness = random.randint(0, 59)
        next_time = time_slots[-1] + timedelta(hours=random.randint(2, 4), minutes=minutes_randomness)
        if next_time > end_time:
            break
        time_slots.append(next_time)

    return time_slots

def schedule_cron_jobs(time_slots):
    # Get paths dynamically
    current_dir = os.getcwd()
    python_path = subprocess.getoutput('which python3').strip()
    script_path = os.path.join(current_dir, 'main.py').replace(" ", " ")

    # Create new cron jobs for the generated times
    cron_jobs = []
    for time_slot in time_slots:
        hour, minute = time_slot.strftime("%H:%M").split(":")
        cron_job = f'{minute} {hour} * * * "{python_path}" "{script_path}"'
        cron_jobs.append(cron_job)

    # Add the cron jobs
    with open('cronfile', 'w') as file:
        for job in cron_jobs:
            file.write(job + '\n')
    subprocess.run('crontab cronfile', shell=True)
    subprocess.run('rm cronfile', shell=True)

    print("Cron jobs scheduled.")


if __name__ == "__main__":
    time_slots = generate_schedule()
    schedule_cron_jobs(time_slots)
