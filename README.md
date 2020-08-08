# Consistency Reminder
  A project that shows how behind you are in latest scrum What you had proposed and what you did have achieved till last date of scrum.
  This project has been developed by using google sheet api and python libraries.
       
       project demo-https://youtu.be/54YZnZMFZBk
              
1-> For using it on your local machine fill the list contacts with emails of members as in sheet sorted order. Make sure that it is as sorted as in google spreadsheet names. This code does not sort contact list because names are in sorted order but emails may not be.
So fill this list according to the name.

2-> Use your email ans password to send message to everyone.("""EMAIL_ADDRESS = 'EMAIL_USER'
    EMAIL_PASSWORD = 'EMAIL_PASS'""" in line 18 and 19 in code either you can put your mail and pass directly "smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)")
    
3-> "Allow less secure apps: ON" using this link https://myaccount.google.com/lesssecureapps.

4-> Turn off Two Step verification using link https://myaccount.google.com/security.

5-> Now you can put your time and day in week when you want to notify team members from line 102 to 112. I have put their monday and time according to my testing time. You have to put current time and day when you are testing.

6-> Now you have to request for Google Sheet api and google drive api(to update sheet) using this youtube link https://www.youtube.com/watch?v=cnPlKLEGR7E&t=311s  or you can find screenshot of this process in repository.

7-> You will get a json file put that name in line 26 you can rename it.

8->Put sheet name in line 30.

Thankyou,
