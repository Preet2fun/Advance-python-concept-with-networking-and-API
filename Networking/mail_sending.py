import smtplib

def MAIL():
    sender = 'from@fromdomain.com'
    receivers = ['to@todomain.com']
    message = """From: From Person <from@fromdomain.com>
    To: To Person <to@todomain.com>
    Subject: SMTP e-mail test
    This is a test e-mail message.
    """
    try:
        smtp_obj = smtplib.SMTP('localhost')
        smtp_obj.sendmail(sender,receivers,message)
        print "Message send successfuly"
    except:
        return "Mail not send succesfully"

x = MAIL()
print x