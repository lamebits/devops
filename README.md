# devops

# Python Library
webdriver,selenium,os,openpyxl,panda,devenv,email,smtplib

# Get Environment Variable like username and password
""" pip install python-dotenv 
from dotenv import load_dotenv
load_dotenv()"""

# passing variable inside variable
lambda emailId : "//div/h1/strong[text()='"+emailId+"']"

# Create an Array which contains all error related message
ERROR_MESSAGE = {
    "DRIVER_INITIALIZATION":"Error on initialization web driver",
    "ACME_LOGIN":"ACME Portal Login to Fail"
}
Calling: 
1. ERROR_MESSAGE.get("ACME_LOGIN") OR
2. ERROR_MESSAGE["ACME_LOGIN"]