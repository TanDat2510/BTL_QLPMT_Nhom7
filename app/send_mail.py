from email.message import EmailMessage
import ssl
import smtplib

#Đăng ký trực tuyến
def send(email_receiver, date, time):
    email = 'ledat14425@gmail.com'
    password = "ssof vmdg inmt crrp"

    subject = "Thông tin Đặt lịch khám - Phòng Mạch"
    body = """
    Chào {},

    Bạn vừa đặt lịch khám trực tuyến trên hệ thống của chúng tôi. Thông tin khám bao gồm:

    Ngày đặt lịch: {}

    Giờ khám: {}

    Tôi xin gửi lời cảm ơn chân thành về sự quan tâm và sự tin tưởng của bạn khi đăng ký phòng mạch của chúng tôi để khám sức khỏe.
    Chúng tôi trân trọng sự hợp tác của bạn và hy vọng rằng chúng tôi sẽ có cơ hội phục vụ bạn trong thời gian sớm nhất.
    Chúc bạn một ngày tốt lành!

    """.format(email_receiver, date, time)

    em = EmailMessage()
    em['From'] = email
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email, password)
        smtp.sendmail(email, email_receiver, em.as_string())


#Đăng ký tại phòng mạch
def send2(email_receiver, date, time):
    email = 'ledat14425@gmail.com'
    password = "ssof vmdg inmt crrp"

    subject = "Thông tin Đặt lịch khám"
    body = """
       Chào {},

    Bạn vừa đặt lịch khám trực tuyến trên hệ thống của chúng tôi. Thông tin khám bao gồm:

    Ngày đặt lịch: {}

    Giờ khám: {}

    Tôi xin gửi lời cảm ơn chân thành về sự quan tâm và sự tin tưởng của bạn khi đăng ký phòng mạch của chúng tôi để khám sức khỏe.
    Chúng tôi trân trọng sự hợp tác của bạn và hy vọng rằng chúng tôi sẽ có cơ hội phục vụ bạn trong thời gian sớm nhất.
    Chúc bạn một ngày tốt lành!
       """.format(email_receiver, date, time)

    em = EmailMessage()
    em['From'] = email
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email, password)
        smtp.sendmail(email, email_receiver, em.as_string())


# def send(email_receiver, date, time):
#     email = 'vantanss1001ez@gmail.com'
#     password = "tzwaxabqoawzyhav"
#
#     subject = "Thông tin Đặt lịch khám - Phòng Mạch"
#     body = """
#     Chào {},
#
#     Bạn vừa đặt lịch khám trực tuyến trên hệ thống của chúng tôi. Thông tin khám bao gồm:
#
#     Ngày đặt lịch: {}
#
#     Giờ khám: {}
#
#     Tôi xin gửi lời cảm ơn chân thành về sự quan tâm và sự tin tưởng của bạn khi đăng ký phòng mạch của chúng tôi để khám sức khỏe.
#     Chúng tôi trân trọng sự hợp tác của bạn và hy vọng rằng chúng tôi sẽ có cơ hội phục vụ bạn trong thời gian sớm nhất.
#     Chúc bạn một ngày tốt lành!
#
#     """.format(email_receiver, date, time)
#
#     em = EmailMessage()
#     em['From'] = email
#     em['To'] = email_receiver
#     em['Subject'] = subject
#     em.set_content(body)
#
#     context = ssl.create_default_context()
#
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#         smtp.login(email, password)
#         smtp.sendmail(email, email_receiver, em.as_string())



# def send2(email_receiver, date, time):
#     email = 'vantanss1001ez@gmail.com'
#     password = "tzwaxabqoawzyhav"
#
#     subject = "Thông tin Đặt lịch khám"
#     body = """
#        Chào {},
#
#     Bạn vừa đặt lịch khám trực tuyến trên hệ thống của chúng tôi. Thông tin khám bao gồm:
#
#     Ngày đặt lịch: {}
#
#     Giờ khám: {}
#
#     Tôi xin gửi lời cảm ơn chân thành về sự quan tâm và sự tin tưởng của bạn khi đăng ký phòng mạch của chúng tôi để khám sức khỏe.
#     Chúng tôi trân trọng sự hợp tác của bạn và hy vọng rằng chúng tôi sẽ có cơ hội phục vụ bạn trong thời gian sớm nhất.
#     Chúc bạn một ngày tốt lành!
#        """.format(email_receiver, date, time)
#
#     em = EmailMessage()
#     em['From'] = email
#     em['To'] = email_receiver
#     em['Subject'] = subject
#     em.set_content(body)
#
#     context = ssl.create_default_context()
#
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#         smtp.login(email, password)
#         smtp.sendmail(email, email_receiver, em.as_string())

