import smtplib
import json 
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication 

email json {
    "from": "email@example.com",
    "to": "to@example.com",
    "subject": "test email",
    "body": "this contant".
    "attachments":[]
}

def send_email(email_data):
    try:
        server = smtplib.SMTP("smtp.gamil.com",587)
        server.starttls()

        server.login("email","password")

        msg = MIMEMultipart()
        msg["From"] = email_data["from"]
        msg["To"] = ", ".join(email_data["to"]) 
        msg["Subject"] = email_data["subject"]

        body = MIMEText(email_data["body"],"plain")
        msg.attach(body)

        for attachment in email_data["attachments"]:
            with open (attachment,"rb") as f:
                part = MIMEApplication(f.read(),Name=attachment)
                part['Content-Disposition'] = f'attachment;filename="{attachment}"'
                msg.attach(part)


        server.sendmail(email_data["from"],email_data["to"],msg.as_string())        
        server.quit()
        print("email send")
    except Exception as e:
        print(f"Error{e}")

send_email(email json)        

