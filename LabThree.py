# Crawler that would visit a webpage and college email addresses 
# Created by Mohammad R Abedin (Rafat)

from re import findall
import urllib.request

url = "https://www.uta.edu/academics/schools-colleges/business/admissions-and-advising/cob-advising"

print("\n Email addresses for advisors of Business Dept at UTA: \n")

response = urllib.request.urlopen(url)

html = response.read()

htmlStr = html.decode()

pdata = findall(r"[A-Za-z0-9._%+-]+" r"@[A-Za-z0-9.-]+" r"\.[A-Za-z]{2,4}", htmlStr)

for item in pdata[::2]:
    print(item)