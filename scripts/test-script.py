import requests
from bs4 import BeautifulSoup

def login_to_course_library(username, password):
    try:
        # URL of the login page
        login_url = "https://courses.xmpro.com/wp-login.php"

        # Prepare login data
        login_data = {
            "log": username,
            "pwd": password,
            "wp-submit": "Log In"
        }

        # Send POST request to submit login form
        login_response = requests.post(login_url, data=login_data)

        # Check if login was successful
        if "course-library/dashboard" in login_response.url:
            print("Login successful.")
        else:
            print("Login failed. Please check your credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Provide your username and password here
username = "jackson.mcgurik@xmpro.com"
password = "$Jstark2004"

# Perform login
login_to_course_library(username, password)
