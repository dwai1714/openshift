def send_gmail_message(toadd,fromaddr,password,subject,dir,filename,body):
    import smtplib
    from email import encoders
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase

    #fromaddr = "rackspace.accion@gmail.com"


    msg = MIMEMultipart()
    msg['From'] = fromaddr
    toaddr = toadd
    msg['To'] = ",".join(toaddr)
    msg['Subject'] = subject
    body = body
    msg.attach(MIMEText(body, 'plain'))

    if filename != 0:
        try:
            filename = filename
            attachment = open(dir + filename, "rb")
        except:
            return False
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    return True
