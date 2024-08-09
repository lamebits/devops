ACME_URL = "https://acme-test.uipath.com/p/login"
IMPLICIT_DELAY = 20
EMAIL_XPATH = "//*[@id='email']"
PASSWORD_XPATH = "//*[@id='password']"
SUBMIT_XPATH = "//button[@type='submit']"
WORKITEM_XPATH = "//*[@id='dashmenu']/div[2]/a/button"
WORKITEM_TABLE_XPATH = "/html/body/div/div[2]/div/table"
ERROR_MESSAGE = {
    "DRIVER_INITIALIZATION":"Error on initialization web driver",
    "ACME_LOGIN":"ACME Portal Login to Fail"
}

import os
# Get the absolute path of the directory containing this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE_PATH = BASE_DIR+"\\Input_files\\WorkItemData.xlsx"
MASTER_FILE_PATH = BASE_DIR+"\\Supportive_files\\MasterFile.xlsx"
OUTPUT_FILE_PATH = BASE_DIR+"\\Output_files\\OutputFile.xlsx"

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "meenalmate1663@gmail.com"
RECEIPENT_EMAIL = "meenalmate1663@gmail.com"
EMAIL_SUBJECT = "Subject of the Email"
EMAIL_BODY = "This is the body of the email."
AUTHENTICATION = lambda emailId : "//div/h1/strong[text()='"+emailId+"']"