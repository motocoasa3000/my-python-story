import smtplib

my_email = "(myEmail).com"
password = "your application password"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # transfer layer security
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="to-mail-address~@gmail.com",
        msg="Subject:Hello\n\nlove you :*"
    )