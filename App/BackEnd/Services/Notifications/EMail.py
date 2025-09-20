import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(sender_email: str, sender_password: str, receiver_email: str, subject: str, body: str):
    """
    Отправка письма через SMTP (по умолчанию Gmail)
    :param sender_email: адрес отправителя
    :param sender_password: пароль приложения/SMTP пароль
    :param receiver_email: адрес получателя
    :param subject: тема письма
    :param body: текст письма
    """
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Формируем письмо
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Письмо успешно отправлено!")
    except Exception as e:
        print("Ошибка при отправке письма:", e)

def main():
    pass

if __name__ == "__main__":
    main()