import json, time, requests

#variables
url = open('note_url', 'r').read()
price_target = open('note_target', 'r').read()
price_limit = open('note_limit', 'r').read()
loop = True

sender = open('note_sender', 'r').read()
receiver = open('note_receiver', 'r').read()
password = open('note_password', 'r').read()

#Test E-mail
email_test = EmailMessage()
email_test["Subject"] = 'Currency Tracker Bot Test'
email_test["From"] = sender 
email_test["To"] = receiver
email_test.set_content("Hello! \n\n I am the Currency Tracker Bot you hired! \n This is just a test email to check if it's all right. For now on, I will be tracking the price of the currencies you ask. When they were in one of the prices you choose, I'll tell you! \n\n See you!")
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(sender, password)
    smtp.send_message(email_test)
    
#Email for low values 
email_low = EmailMessage()
email_low["Subject"] = 'Currency Tracker Bot'
email_low["From"] = sender 
email_low["To"] = receiver
email_low.set_content("Hey! \n\n The currency you are tracking get cheaper! \n\n Check it out: "+url)

#Email for high values 
email_high = EmailMessage()
email_high["Subject"] = 'Currency Tracker Bot'
email_high["From"] = sender 
email_high["To"] = receiver
email_high.set_content("Hey! \n\n The currency you are tracking get higher value! \n\n Check it out: "+url)

#Email back
email_back = EmailMessage()
email_back["Subject"] = 'Currency Tracker Bot'
email_back["From"] = sender 
email_back["To"] = sender
email_back.set_content("The bot work is finished for "+ receiver)

while loop == True:
    #API data manipulation

#Send E-mail
    #Attention to the price string!
    if float(price.text[1:9]) <= float(price_limit):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(sender, password)
            smtp.send_message(email_low)
            smtp.send_message(email_back)
        loop = False
    elif float(price.text[1:9]) >= float(price_target):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(sender, password)
            smtp.send_message(email_high)
            smtp.send_message(email_back)
        loop = False
    time.sleep(86400)
