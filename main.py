# Importing all necessary libraries
import yagmail
from decouple import config
from pathlib import Path
import pandas as pd

EMAIL=config('EMAIL')
PASSWORD=config('PASSWORD')
yagmail.register(EMAIL, PASSWORD)
yag=yagmail.SMTP(EMAIL,PASSWORD)

# Remove the very first try and except block

question_1=str(input(f'Do you have a list of emails saved to the home directory you would like to use?:'))

if question_1 == 'y':
    try:
        control_flow_maintainer=f'Your emails have sent!'
                
        with open('email_list.csv', 'r') as email_list:
            imported_file = pd.read_csv(email_list)
            
            for name in imported_file['name']:

                text = f"""
                    Hello {name} Thank you for using the Spotify Data ETL.
                    Your file is attached to this email."""
                subject = 'This is a Test Email'
                
            for email in imported_file['email']:
                with open('test1.txt', 'rb') as attachment:
                    yag.send(to=[email],
                    subject=subject,
                    contents=text,
                    attachments=attachment) 
        
        print(control_flow_maintainer)        
        
    except Exception as e:
        print(f'Sorry there was an error')
        print(e)


if question_1 == 'n':
    try:
        control_flow_maintainer=f'Your emails have sent!'
        additional_emails=str(input(f'Enter the list of emails separated with a comma:'))
        additional_email_list=list(additional_emails.split(sep=','))
        text = f"""
                Hello! Thank you for using the Spotify Data ETL.
                Your file is attached to this email."""
        
        subject = 'This is a Test Email'

        with open('test1.txt', 'rb') as attachment:
            yag.send(to=additional_email_list,
                        subject=subject,
                        contents=text,
                        attachments=attachment
                        )
            print(control_flow_maintainer)
    
    except Exception as e:
        print(f'Sorry there was an error')
        print(e)
    

    
