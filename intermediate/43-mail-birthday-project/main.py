import smtplib

my_email = "lucianflorincioba@gmail.com"
password = "vfdp ocod zdck sceo"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()  # transfer layer security
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="pascaadina@gmail.com",
    msg="Subject:Hello\n\n ")
connection.close()
