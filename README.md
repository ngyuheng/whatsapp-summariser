<div align="left" style="position: relative;">
<h1>WhatsApp Chat Summariser</h1>

For those who are too lazy to read long chats.
</div>

##  Table of Contents

- [ Overview](#overview)
- [ Features](#features)
- [ Project Structure](#project-structure)
- [ Getting Started](#getting-started)
  - [ Prerequisites](#prerequisites)
  - [ Installation](#installation)
  - [ Usage](#usage)
- [ Contributing](#contributing)
- [ License](#license)
- [ Acknowledgments](#acknowledgments)

---

##  Overview

<!-- Introduce OBC -->
<!-- link to FreeRTOS repo. -->
<!-- link to CSP repo. -->

This project provides an easy way for chat logs in WhatsApp to be summarised and sent to Google Gemini's API. This is useful for chat logs that are too long to be read in one sitting, or for chat logs that need to be summarised for a report, or for people who are too lazy to read long chats.

---

##  Features

Reads and summarises WhatsApp DMs and Group Chats using Selenium and Google Gemini's API.

Number of text messages can be changed in the `summariser.py` file (line 99).

- [x]  Read WhatsApp DMs and Group Chats
- [x]  Summarise WhatsApp DMs and Group Chats
- [x]  Send summarised messages to Google Gemini's API
- [ ]  Use Edge instead of Chrome so that it can be run when Chrome is being used as Chrome does not allow multiple instances to be run at the same time (and who uses Edge anyways?)

---

##  Project Structure

<details>
<summary>View Project Structure</summary>

```sh
└── obc/
    ├── cookies
    │   ├── cookies.txt
    ├── .env
    ├── .gitignore
    ├── README.md
    └── summariser.py
```
</details>

---

##  Getting Started

###  Prerequisites

- A [Gemini API Key](https://docs.gemini.com/rest-api/#authentication) is required to access the Gemini API.
    - Create a `.env` file in the root directory of the project.
    - Add the following line to the `.env` file:
        ```sh
        API_KEY=YOUR_API_KEY
        ```
- I'm too lazy to write a requirements.txt file, so you'll have to install the dependencies manually. Using pip install, install the following dependencies:
    - selenium
    - pyautogui
    - google-generativeai
    - python-dotenv
    - webdriver-manager

###  Installation

Clone the repository using the following command:

```sh
git clone https://github.com/ngyuheng/whatsapp-summariser
```

###  Usage

Note: It's recommended to comment out line 40, otherwise login QR Code will not appear. After login, the line may be uncommented.
Note: Close existing Chrome Tabs. Otherwise an error will be raised. ("Message: session not created: Chrome failed to start: crashed.")

#### 1. Chrome Profile Path
The script uses a specific Chrome user profile to bypass logging in to WhatsApp Web. On a different machine, you must update the path to your Chrome user profile.

In the init() function, change the following line (line 97):

```python
driver = init("C:\\Users\\ngyuh\\AppData\\Local\\Google\\Chrome\\User Data")
```
Replace the path with the correct path to your Chrome profile directory. On a Mac, it might be something like:

```bash
"/Users/your-username/Library/Application Support/Google/Chrome" 
```
Make sure the profile name matches the one you're using, or update "Profile 5" to the correct name. (Refer to the User Data directory to identify the name of the profile)

#### 2. Phone Number or Group Info
To scrape messages from a specific WhatsApp chat, update the phone number or group code in the get_messages() function. Change this line (line 98):

```python
messages = get_messages(driver, "ABC", "group")
```
Replace ```"ABC"``` with the phone number or group code you want to scrape. Phone numbers should include the country code, and contain no spaces.

Set the second parameter ("group" or "phone_number") accordingly, depending on whether you want to scrape messages from a group or individual. For Groups, the ID is accessed through the ```Invite to Group via Link``` option in the group settings.
#### 3. API Key for Google Generative AI
This script uses Google's Generative AI API to summarize the messages. You need to configure the API key for access.

Create a .env file in the same directory as the script.

Add your API key to the .env file as follows:

```makefile
API_KEY=your_api_key_here
```
The script loads the API key from the .env file using the dotenv package, so ensure the file is in the correct location.

#### 4. Run the Python File
Run using the following command:

```sh
python summariser.py
```

---
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com/ngyuheng/whatsapp-summariser/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=ngyuheng/whatsapp-summariser">
   </a>
</p>
</details>

---

##  License

This project is not protected under any license. You are free to use, modify, and distribute the software as you see fit.

---

##  Acknowledgments

- [UnidentifiedX](https://github.com/UnidentifiedX/UnidentifiedX) for the inspiration to create this project.

---
