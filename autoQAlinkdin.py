from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from sqlalchemy.engine import create_engine
import random
from selenium.webdriver.common.alert import Alert
import pandas as pd
from pyzbar.pyzbar import decode
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
#from PIL import Image
xpathhour="//span[@class='visually-hidden'][text()[contains(.,'hour')]]"
# xpathemail="//span[@dir='ltr']//a"
# xpathseemore="//button[@aria-hidden='true'][text()[contains(.,'see more')]]"
#Run on already opened browser
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9250")
chrome_driver = "D:\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
time.sleep(3)
df = pd.read_csv('C:\\Users\\Robi\\Desktop\\python\\linkdin\\emails.csv')
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
time.sleep(3)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
time.sleep(3)
elem=driver.find_elements_by_xpath(xpathhour)
elem1=driver.find_elements_by_partial_link_text('@')
print(len(elem))
for i in elem:
    print(i.text)
    z=0
    for y in elem1:
        time.sleep(2)
        print(y.text)
        df['email'][z]=y.text
        z=z+1
        time.sleep(2)
        break
print(df)

rowcount= df['email'].count()

# Python code to illustrate Sending mail with attachments 
# from your Gmail account  
for y in range(0,rowcount):
    fromaddr = "ramitrehal@gmail.com"
    toaddr = df['email'][y]

    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    
    # storing the senders email address   
    msg['From'] = fromaddr 
    
    # storing the receivers email address  
    msg['To'] = toaddr 
    
    # storing the subject  
    msg['Subject'] = "Application for job opening | QA"
    
    # string to store the body of the mail 
    body = "Hi \n\n This is with context to job opening posted on linkedin. PFA my resume and let me know if I am considerable for the role \n\n Thanks\nRamit Rehal"
    
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    
    # open the file to be sent  
    filename = "Test_Lead_HCL.pdf"
    attachment = open("D:\\RAMIT_Internantional\\Test_Lead_HCL.pdf", "rb") 
    
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    
    # encode into base64 
    encoders.encode_base64(p) 
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    
    # start TLS for security 
    s.starttls() 
    
    # Authentication 
    s.login(fromaddr, "lab1!@#akcds") 
    
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
    
    # terminating the session 
    s.quit() 











