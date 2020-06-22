# Crawler that would visit a webpage and display email addresses in list 
# Created by Mohammad R Abedin (Rafat)

import re
from urllib.request import urlopen
#importing libraries for their use in this program

print("\n Email addresses for advisors of Business Dept at UTA: \n")

def emails(addresses): #function
    emailList = [] #list declared 
    
    for email in re.findall(r'[\w\.-]+@[\w\.-]+', addresses): #looking for what matches format
        if not email in emailList:
            emailList.append(email) #assigning values to emailList 
    print(emailList) 

url = 'https://www.uta.edu/academics/schools-colleges/business/admissions-and-advising/cob-advising'
addresses = urlopen(url).read().decode() # quickerway to do read and decode
emails(addresses)