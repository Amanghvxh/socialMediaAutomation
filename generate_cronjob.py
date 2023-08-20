#!/usr/bin/env python3
import os
import subprocess

def add_cron_job():
    # Identify python3 path
    python_path = subprocess.getoutput('which python3').strip()

    # Assuming the generate_time_file.py is in the same directory as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(script_dir, 'generate_time_file.py')    
    # Escape spaces in the path
    script_path = script_path.replace(' ', '\ ')

    # Create the cron job command
    cron_cmd = f"0 8 * * * {python_path} {script_path}"

    # Get current cron jobs
    current_cron_jobs = subprocess.getoutput('crontab -l')
    
    # Check if there are no existing cron jobs
    if "no crontab for" in current_cron_jobs:
        current_cron_jobs = ""
    
    # Add the new cron job
    new_cron_jobs = current_cron_jobs + '\n' + cron_cmd + '\n'
    
    # Write the new cron jobs
    with open('temp_cron.txt', 'w') as f:
        f.write(new_cron_jobs)
    
    # Update the cron jobs
    os.system('crontab temp_cron.txt')
    
    # Remove the temporary file
    os.remove('temp_cron.txt')

    print("Cron job added successfully!")

if __name__ == "__main__":
    add_cron_job()
