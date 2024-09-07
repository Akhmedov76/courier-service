import smtplib


def send_mail(to_user, subject, message):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_sender = 'ahmedovj7686@gmail.com'
    smtp_password = 'xnuj mftg hmqz xtow'
    email = f"Subject: {subject}\n\n{message}"
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_sender, smtp_password)
        server.sendmail(smtp_sender, to_user, email)
        server.quit()
    except smtplib.SMTPException as e:
        print(f"Failed {e}")
