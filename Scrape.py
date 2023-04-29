#importing the required libraries
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time  
import csv

#creating an instance of the webdriver 
driver = webdriver.Chrome() 

#navigating to the web page 
driver.get("https://www.eecs.mit.edu/role/faculty/") 
time.sleep(2) 

Names = []
Emails = []
Research_interests = []

#locating the elements
all_divs = driver.find_elements(By.CLASS_NAME, "people-entry small-12 medium-6 large-4 larger-3 cell")
names = driver.find_elements(By.TAG_NAME,"h5")
research_interests=driver.find_elements(By.CLASS_NAME,"people-research")
emails = driver.find_elements(By.XPATH, "//a[contains(@href, 'mailto:')]")

for name in names:
    Names.append(name.text)
    
for research_interest in research_interests:
    Research_interests.append(research_interest.text)
    
for email in emails:
    Emails.append(email.text)

#writing to the csv file
with open('faculty_info.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Email','Research Interests'])
    for i in range(len(Names)):
        writer.writerow([Names[i],Emails[i], Research_interests[i]])
