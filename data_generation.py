
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import ast
import os
load_dotenv()
options = uc.ChromeOptions()
options.add_argument('--headless')
driver = uc.Chrome(options=options)
# driver = uc.Chrome()

GMAIL = os.getenv("GMAIL")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")

def click_element(selector, driver, by=By.CSS_SELECTOR, wait_time=10):
    try:
        element = WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((by, selector))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        sleep(1)
        driver.execute_script("arguments[0].click();", element)
        return True
    except TimeoutException:
        print(f"Element with selector {selector} not found.")
        return False
    except StaleElementReferenceException:
        print(f"Stale element with selector {selector}. Retrying...")
        return click_element(selector, driver, by, wait_time)




def loginAndFormalities():
    driver.get("https://chat.openai.com/")
    sleep(2)
    if not click_element('.btn.relative.btn-primary', driver):
        if not click_element('.relative.flex.h-12.items-center.justify-center', driver):
            driver.quit()
    sleep(3)
    if not click_element(".c83859ab9.c6080078a.ce510e60e", driver): driver.quit()
    sleep(3)

    actions = ActionChains(driver)
    actions.send_keys(GMAIL).send_keys(Keys.RETURN).perform()
    sleep(1)

    password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']")))
    password_field.send_keys(GMAIL_PASSWORD)
    password_field.send_keys(Keys.RETURN)

    # if not click_element("//button[contains(., 'Try another way')]", driver, By.XPATH): driver.quit()
    # sleep(1)

    # enter_backup_code_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Enter one of your 8-digit backup codes")]')))
    # enter_backup_code_div.click()
    # sleep(1)

    # backup_code_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "backupCodePin")))
    # backup_code_field.send_keys("87661906")
    # backup_code_field.send_keys(Keys.RETURN)

    # actions.send_keys(Keys.RETURN)
    # sleep(2)




import json

def generateData():
    loginAndFormalities()

    full_prompt = """Category: Love ,love at first sight , first love, unconditoinal love and true love, long distance love , Number of Quotes: 60, In the chosen category, your task is to craft [Number of Quotes] quotes that sing with creativity, yet are concise and potent. Each quote should be a blend of poetic artistry and insightful wisdom, presented in a way that will fit into the space of an Instagram post and be mostly viewed on m Imagine words that dance and play, yet strike at the very core of human emotion. Let your creativity soar and weave quotes that are not just heard but felt. They should be brushstrokes of genius that paint vivid pictures with just a few Along with each quote, fashion a realistic author's name that's short but resonates with the essence of the  Envision these quotes lighting up screens, sparking thoughts, and inspiring hearts. Feel the rhythm of the words, the beat of the sentiment, the melody of w Now, with a creative spirit and an understanding heart, compose an array containing [Number of Quotes] subarrays, each with a succinct and imaginative quote, and a fitting author's name that together will resonate with beauty and  xxxxxxx[  ["Your Creative Quote 1", "Realistic Author's Name 1"], ["Your Creative Quote 2", "Realistic Author's Name 2"]xxxxxxxx,    ... continue for the specified number of quotes ONLY PYTHON ARRAY SHOULD BE GENERATED , ONLY PYTHON ARRAY SHOULD BE GENERATED ,ONLY PYTHON ARRAY SHOULD BE GENERATED, ONLY PYTHON ARRAY SHOULD BE GENERATEDONLY PYTHON ARRAY SHOULD BE GENERATED , ONLY PYTHON ARRAY SHOULD BE GENERATED ,ONLY PYTHON ARRAY SHOULD BE GENERATED, ONLY PYTHON ARRAY SHOULD BE GENERATED , there should be nothing else than array itself , no function no code , no nothing."""

# Check if the element exists before proceeding
    for _ in range(5):  # Retry up to 5 times
        try:
            driver.find_element(By.ID, "prompt-textarea")
            break
        except:
            print("Waiting for the textarea to load...")
            sleep(10)
    else:
        print("The textarea was not found after multiple attempts. Exiting.")
        driver.quit()
        return

    # Using JavaScript to set the value of the textarea
    driver.execute_script("""
        document.getElementById('prompt-textarea').value = arguments[0];
        var event = new Event('input', {'bubbles': true, 'cancelable': true});
        document.getElementById('prompt-textarea').dispatchEvent(event);
    """, full_prompt)

    # Sleep for a bit to let the page process the input
    sleep(5)

    # Using JavaScript to click the submit button
    driver.execute_script("""
        document.querySelector('textarea[id="prompt-textarea"] + button').click();
    """)
    
    # Wait for results
    sleep(50)

    # Fetch the results using JavaScript
    result_string = driver.execute_script("""
        let codeElement = document.querySelector('.p-4.overflow-y-auto code');
        if (codeElement) {
            return codeElement.textContent;
        } 
        let proseElement = document.querySelector('.markdown.prose p');
        if (proseElement) {
            return proseElement.textContent;
        }
        return null;
    """)

    if result_string.startswith("quotes = ["):
        content = result_string.split("[", 1)[1].rsplit("]", 1)[0]
        try:
            data_list = ast.literal_eval(f"[{content}]")
        except ValueError:
            print(f"Error evaluating the extracted content: [{content}]")
            driver.quit()
            return
    else:
        try:
            data_list = json.loads(result_string)
        except json.JSONDecodeError:
            print(f"Error decoding JSON from result string: {result_string}")
            driver.quit()
            return

    

    # Format the data into a list of dictionaries where each entry has the key set to false
    formatted_data = [{"quote": item[0], "author": item[1], "key": False} for item in data_list]

    # Create a dictionary that includes the formatted data
    output_data = {"pending_quotes": formatted_data}

    # Save the results in a new JSON file
    output_file_path = './utils/pending.json'
    with open(output_file_path, 'w') as f:
        json.dump(output_data, f)

    print(f"Data has been saved to {output_file_path}")

    # Close the driver
    driver.quit()

