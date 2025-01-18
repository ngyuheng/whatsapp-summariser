from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import pyautogui as pg

from webdriver_manager.chrome import ChromeDriverManager

import google.generativeai as genai
import os
from dotenv import load_dotenv

import time


class WhatsAppMessage:
    def __init__(self, sender, message, time):
        self.sender = sender
        self.message = message
        self.time = time

    def __str__(self):
        # if sender is empty, remove colon
        if self.sender == "":
            return f"{self.message}; "
        return f"{self.sender}{self.message}; " # ({self.time})"

    def __repr__(self):
        # if sender is empty, remove colon
        if self.sender == "":
            return f"{self.message}; "
        return f"{self.sender}{self.message}; " # ({self.time})"


def init(path, profile_name="Profile 5"):
    options = webdriver.ChromeOptions() 
    options.add_argument(f"user-data-dir={path}") # Path to your chrome profile
    options.add_argument(f"profile-directory={profile_name}") # Use the profile name you are using
    options.add_argument("--headless") # no window, need to enable if not logged in


    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    
    # check if cookies are present, cookies not used for anything other than checking if user is logged in
    with open("cookies/cookies.txt", "r") as file:
        cookies = file.read()
        if not cookies:
            driver.get("https://web.whatsapp.com")
            # popup to wait for user to login to WhatsApp Web
            pg.alert('Click OK after logging in to WhatsApp Web')
            with open("cookies/cookies.txt", "w") as file:
                cookies = driver.get_cookies()
                file.write(str(cookies))
    
    return driver


def get_messages(driver, phone_number, chat_type, wait_time=7):
    
    if chat_type == "phone_number":
        # go to chat
        driver.get(f"https://web.whatsapp.com/send?phone={phone_number}")
    
    elif chat_type == "group":
        # go to group
        driver.get(f"https://web.whatsapp.com/accept?code={phone_number}")
    
    # wait
    time.sleep(wait_time)
    
    # Find all message containers (sender and message are inside the same div)
    
    heads = driver.find_elements(By.XPATH, "//div[contains(@class, 'copyable-text')]")
    
    messages = []
    
    for head in heads:
        message = WhatsAppMessage(head.get_attribute("data-pre-plain-text"), head.text, "NA")
        messages.append(message)
        # print(message)
        
    driver.close()
    
    # flip array so that messages are in reverse chronological order
    return messages[::-1]


def gpt_summary(messages):
    model = genai.GenerativeModel("gemini-1.5-flash")
    # print(f"Summarise the content of the texts: {str(messages[::-1])}\n")
    response = model.generate_content(f"Summarise the content of the texts, if the text after the name of the sender is another name, followed by a new line and a line of text, that line of text is a quote, the line after that is a message by the sender: {str(messages[::-1])}\n")
    return response.text

load_dotenv()
genai.configure(api_key=os.environ.get("API_KEY"))
driver = init("C:\\Users\\ngyuh\\AppData\\Local\\Google\\Chrome\\User Data") # <- change address to address of your chrome profile (this is to remove the need to login to WhatsApp Web every time)
messages = get_messages(driver, "ABC", "group") # <- change phone number to phone number of chat you want to summarise, change to "group" if you want to summarise a group chat
print(gpt_summary(messages[0:20])) # <- change number to number of messages you want to summarise