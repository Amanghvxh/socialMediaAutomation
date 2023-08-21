from datetime import datetime, timedelta
import random
import subprocess
import os

def generate_schedule():
    # Randomize the start time between 8 AM and 9 AM
    start_time = datetime.strptime("08:00", "%H:%M") + timedelta(minutes=random.randint(0, 59))
    end_time = datetime.strptime("21:00", "%H:%M")
    time_slots = [start_time]

    while len(time_slots) < 7:  # Ensure there are always 7 cron jobs
        # Add randomness to the time between cron jobs
        minutes_randomness = random.randint(0, 59)
        next_time = time_slots[-1] + timedelta(hours=1) + timedelta(minutes=minutes_randomness)
        if next_time > end_time:
            break
        time_slots.append(next_time)

    return time_slots

def schedule_cron_jobs(time_slots):
    # Get paths dynamically
    python_path = subprocess.getoutput('which python3').strip()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(script_dir, 'main.py')

    # Create new cron jobs for the generated times
    cron_jobs = []
    for time_slot in time_slots:
        hour, minute = time_slot.strftime("%H:%M").split(":")
        cron_job = f'{minute} {hour} * * * "{python_path}" "{script_path}"'
        cron_jobs.append(cron_job)

    # Schedule this script to run every day at 8 AM
    self_schedule = f'0 8 * * * "{python_path}" "{os.path.abspath(__file__)}"'
    cron_jobs.append(self_schedule)

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
