import smtplib, ssl

def sendEmail(message, receiver_email):
    import smtplib, ssl
    port = 465  # for ssl
    smtp_server = "smtp.gmail.com"
    sender_email = "daspbltum@gmail.com"
    password = "btzniijtzwnfwdtp"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)