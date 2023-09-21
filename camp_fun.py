from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imghdr
import json
import os
import requests
from posixpath import basename
import smtplib

from urllib.parse import unquote
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
#                           ####################################
#                           ###### Send WhatsApp Message #######
#                           ####################################
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# WhatsApp API for campaign

def sendWhatsAppMsg(number, msg, Attachments):
    # insetanceId = "621f17f4cd00c56ad254fd4f"
    insetanceId = "64bf6eaaf010b5f71161ee53"
    url = ""
    if msg != "" and Attachments != "":
        url = f"https://wasmsapi.com/api/sendFileWithCaption?token={insetanceId}&phone=+91{number}&message={msg}"
        attachUrl = 'http://103.234.187.197:8051'+Attachments
        url = url+"&link="+unquote(attachUrl)
        loginResponse = requests.post(url, verify=False, timeout=10)
        return json.loads(loginResponse.text)

    elif msg == "" and Attachments != "":
        url = f"https://wasmsapi.com/api/sendFiles?token={insetanceId}&phone=+91{number}"
        attachUrl = 'http://103.234.187.197:8051'+Attachments
        url = url+"&link="+unquote(attachUrl)
        loginResponse = requests.post(url, verify=False, timeout=10)
        return json.loads(loginResponse.text)

    elif msg != "" and Attachments == "":
        url = f"https://wasmsapi.com/api/sendText?token={insetanceId}&phone=+91{number}&message={msg}"
        loginResponse = requests.post(url, verify=False, timeout=10)
        return json.loads(loginResponse.text)
    
    else:
        msg = 'all field are empty! messages will not be sent'
        print(msg)
        return msg

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
#                           ###################################
#                           ####### Send Email Function #######
#                           ###################################
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def sendMail(toEmail, subject, message, attachments):
    print("HEILDSHFSDLF")
    try:

        ServerHost = "smtp.gmail.com"
        ServerPort = 587  # For starttls
        Sender = "shubham.pasosync@gmail.com"
        Password = "8800443616@s"

        # Create message
        # msg = MIMEText(message, "HTML")
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = Sender
        msg['To'] = toEmail
        msg.attach(MIMEText(message, "HTML"))
    
        print(attachments)
        if attachments != "":
            filename = os.path.basename(attachments)
            attachUrl = '/home/www/b2b/haks_pre/bridge/bridge'+attachments
            print(attachUrl)
            with open(attachUrl, "rb") as fil:
                part = MIMEApplication(
                        fil.read(),
                        Name=basename(attachUrl)
                )
            # After the file is closed
            part['Content-Disposition'] = 'attachment; filename="%s"' % filename
            msg.attach(part)

        # Create server object with SSL option
        server = smtplib.SMTP_SSL(ServerHost, ServerPort)

        # Perform operations via server
        server.login(Sender, Password)
        server.sendmail(Sender, [toEmail], msg.as_string())
        server.quit()

        return 'sent'
    except Exception as e:
        print("test end")
        print(str(e))
        print("ddd")
        return str(e)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
