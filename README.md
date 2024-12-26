# Steps to set up all the tools

**Link to Manage Google App Passwords:**
[Generate an App Password Here](https://myaccount.google.com/apppasswords)

## 1. Prerequisites

- **Get the Latest Version of Python (not from the Microsoft Store).**  
  Download Python from the official [Python downloads page](https://www.python.org/downloads/).

- **Install Dependencies**  
  Once Python is installed, you will install the required dependencies in a virtual environment or globally (depending on your preference).

- **Grab the Gmail App Password**  
  1. Go to your [Google Account Security Settings](https://myaccount.google.com/security).
  2. Under "Signing in to Google," locate **App passwords**.
  3. Generate a new app password specifically for this project.
---
## 2. Project Setup
- Create a new folder not in a Onedrive folder git / snyching issues
---
## 3. Create a .gitignore File
- Create a .gitignore file inlclude sensitive creds in listed files
---
## 4. Create a .env File
create a .env file where you store gmail app creds
---
## 5. Install Dependencies
- On that python install the dependencies
---
## 6. Create the Python Script
---
## 7. Run and Test Locally
~...\AppData\Local\Programs\Python\Python313\python.exe ~...\send_email.py
---
## 8. Initialize Git and Commit to GitHub
- git init
- git add .
- git commit -m "Initial commit with email script"
- git remote add origin https://github.com/<username>/<repo_name>.git
- git push -u origin main
- Check ignored files are not on github
---
## 9. Schedule the Script in Windows Task Scheduler
Make sure the start in is the same as your folder.