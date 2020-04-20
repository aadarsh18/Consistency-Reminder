import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import re 
import os
import smtplib
import imghdr
import schedule 
import time 
from email.message import EmailMessage
from datetime import datetime





def scrumcall(start):    
    #EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    #EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    contacts = []

 
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("My Project 74674-48aa88984250.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("sprint sheet").sheet1  

    #data = sheet.get_all_records()  
    #print(data)
    #row = sheet.row_values(3)  
    #col = sheet.col_values(3)  
    #cell = sheet.cell(50,4).value  
    #print(cell)
    #This is for calculating sum of proposed

    def find_sum(t): 
        return sum(map(int,re.findall('\d+',t))) 
    #print(sheet.cell(1,4).value)
    # numrows = sheet.row_count 
    # print(numrows)
    numcols = sheet.col_count
    #print(numcols)  
    count=4
    per=0
    while(count<numcols):
        #print(per)
        #print(sheet.cell(1,count).value)
        msg = EmailMessage()
        msg1=EmailMessage()
        msg2=EmailMessage()
        a=find_sum(sheet.cell(start,count).value)
        b=find_sum(sheet.cell(start+1,count).value)
        name=sheet.cell(1,count).value
        msg2['Subject'] = 'Hey! {} your scrum is here!'.format(name)
        msg1['Subject'] = 'Hey! {} your scrum is here!'.format(name)
        msg1['From'] = 'Team Now n Never'
        msg2['From'] = 'Team Now n Never'
        msg1['To'] = contacts[per]
        msg2['To'] = contacts[per]
        msg['Subject'] = 'Hey {} your scrum is here!'.format(name)
        msg['From'] = 'Team Now n Never'
        msg['To'] = contacts[per]
        msg1.set_content('{} Looks like you are behind current scrum.You just have did {} questions while you have proposed {} questions'.format(name,b,a))
        msg.set_content('Hey! {} You are doing great! keep it up'.format(name)) 
        msg2.set_content('Hey! {} Looks like you have not did any question during this scrum Is everything ok!'.format(name) )      
        per+=1
        count=count+5
        if a==0 or b==0:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg2)
        elif a>b:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg1)
        else:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)               

start=50   

#schedule.every(5).minutes.do(scrumcall,start)
#schedule.every().monday.at("00:59").do(scrumcall,start=start+3)
#schedule.every().monday.at("01:00").do(scrumcall,start=start+14)
#schedule.every().monday.at("01:01").do(scrumcall,start=start+3)
#schedule.every().monday.at("01:02").do(scrumcall,start=start+3)

if datetime.today().strftime('%A')=='Monday':    
    schedule.every().monday.at("14:50").do(scrumcall,start)
    start+=14

if datetime.today().strftime('%A')=='Monday':    
    schedule.every().monday.at("14:53").do(scrumcall,start)
    start+=3

if datetime.today().strftime('%A')=='Monday':    
    schedule.every().monday.at("14:56").do(scrumcall,start)
    start+=3


while True: 
    schedule.run_pending() 
    time.sleep(1) 
#insertRow = ["hello", 5, "red", "blue"]
#sheet.add_rows(insertRow, 4)  
#sheet.update_cell(2,2, "CHANGED")  
#numRows = sheet.row_count  
#print(numRows)