import smtplib
server =smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("window8090@gmail.com","jkmhfgefstopgoqp") #need to get app access passward then it login else unaurthorised failed
subject = "Sample of Email Automation "
body = """  Hi,

            please find the attached document for to day report.
            
            Thanks ,
            Balkumar"""
msg = f'Subject: {subject}\n\n{body}' #subject and body
#l=server.sendmail("window8090@gmail.com","pushpalatha.s120@gmail.com",msg) #from to To mail id
l=server.sendmail("window8090@gmail.com","balkumarunivision@gmail.com",msg) #from to To mail id
try:
    print("Mail sent")

except:
    print("Mail do not send ")
