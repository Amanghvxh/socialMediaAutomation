// Install python git and cron

    --> sudo apt update && sudo apt install -y python3 git cron python3-pip install -y libgl1-mesa-glx

//Clone the repository

    --> git clone https://github.com/Amanghvxh/socialMediaAutomation.git
    --> cd socialMediaAutomation

//Install all the requirements

    --> pip3 install -r requirements.txt

// Setup enviroment variable

    --> setup Instagram Username and Password
        python3 set_env_values.py
            --> Enter Instagram Username
            --> Enter Instagram Password

// Run generate_cronjob.py to generate the first cronjob

    --->python3 generate_cronjob.py
