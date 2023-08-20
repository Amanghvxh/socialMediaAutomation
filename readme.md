//open the terminal and SSH into your VM/(Virtual Enviroment)

    ssh [username]@[hostname_or_IP_address]

//Clone the repository

     git clone https://github.com/Amanghvxh/socialMediaAutomation.git
     cd socialMediaAutomation

// Install python git and cron

     sudo apt update && sudo apt install -y python3 git cron python3-pip libgl1-mesa-glx

//Install all the requirements

     pip3 install -r requirements.txt

// Setup enviroment variable

     setup Instagram Username and Password

        python3 set_env_values.py

             Enter Instagram Username
             Enter Instagram Password

// Run generate_cronjob.py to generate the first cronjob

        python3 generate_cronjob.py

//prompts for generating the quotes

         Category: Love ,love at first sight , first love, unconditoinal love and true love, long distance love logo, love , long distance love , flash, cold , true love , cry , water , air, road, cloud , wave , ring. Number of Quotes: 60, In the chosen category, your task is to craft [Number of Quotes] quotes that sing with creativity, yet are concise and potent. Each quote should be a blend of poetic artistry and insightful wisdom, presented in a way that will fit into the space of an Instagram post and be mostly viewed on m Imagine words that dance and play, yet strike at the very core of human emotion. Let your creativity soar and weave quotes that are not just heard but felt. They should be brushstrokes of genius that paint vivid pictures with just a few Along with each quote, fashion a realistic author's name that's short but resonates with the essence of the Envision these quotes lighting up screens, sparking thoughts, and inspiring hearts. Feel the rhythm of the words, the beat of the sentiment, the melody of w Now, with a creative spirit and an understanding heart, compose an array containing [Number of Quotes] subarrays, each with a succinct and imaginative quote, and a fitting author's name that together will resonate with beauty and xxxxxxx[ ["Your Creative Quote 1", "Realistic Author's Name 1"], ["Your Creative Quote 2", "Realistic Author's Name 2"]xxxxxxxx, ... continue for the specified number of quotes ONLY PYTHON ARRAY SHOULD BE GENERATED , ONLY PYTHON ARRAY SHOULD BE GENERATED ,ONLY PYTHON ARRAY SHOULD BE GENERATED, ONLY PYTHON ARRAY SHOULD BE GENERATEDONLY PYTHON ARRAY SHOULD BE GENERATED , ONLY PYTHON ARRAY SHOULD BE GENERATED ,ONLY PYTHON ARRAY SHOULD BE GENERATED, ONLY PYTHON ARRAY SHOULD BE GENERATED , there should be nothing else than array itself , no function no code , no nothing.

// create quote.txt file and update the pending.json file

    nano quote.txt (command)
    --past the copied array/quotes here-- (This is not a command but is only instructions)
    press ctrl+O , then Enter , then ctrl+X
    python3 update_json.py(command)

// when updating quotes again

    nano quote.txt (command)
    delete everything first then
    --past the copied array/quotes here-- (This is not a command but is only instructions)
    press ctrl+O , then Enter , then ctrl+X
    python3 update_json.py(command)
