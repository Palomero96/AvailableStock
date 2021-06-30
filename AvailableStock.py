#Imports needed
import os

import pandas as pd
import numpy as np
from check import check

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

__csv_dir = 'csv/'
__products_file = 'csv/products.csv'
__example_file = 'csv/example.csv'

def main():
#Read csv file with links into dataframe
# CSV format: link
    urls_df = pd.read_csv(__products_file)
    
#Loop dataframe to get the links
    iteraciones=0
    infinite=True
    while infinite:
        print("Iteracion "+ str(iteraciones))
        for index,row in urls_df.iterrows():
            url = row['Link']

            #call scrap method
            available = check(url)
            print(available)
            #If available send email
            if available is True:
                sendEmail(url)
        iteraciones= iteraciones+1

def sendEmail(url):
    port = 587  # For starttls
    smtp_server = "smtp-mail.outlook.com"
    sender_email = "palomero_96@hotmail.com"
    receiver_email = "david.palomero.1996@gmail.com"
    #Password 
    password = ""

    subject = "GRAPHIC CARD FOUND"
    message = url
    message = 'Subject: {}\n\n{}'.format(subject, message)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()


if __name__ == '__main__':
	main()
