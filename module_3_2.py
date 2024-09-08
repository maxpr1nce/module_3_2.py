def send_email(message, recipient, sender="university.help@gmail.com"):
    # Проверка на корректность e-mail отправителя и получателя
    if "@" not in recipient or not recipient.endswith((".com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if "@" not in sender or not sender.endswith((".com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    # Проверка на отправку самому себе
    if sender == recipient:
        print(f"Нельзя отправить письмо самому себе!")
        return

    # Проверка на отправителя по умолчанию
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

        send_email("Привет!", "user@example.com")
        # Письмо успешно отправлено с адреса university.help@gmail.com на адрес user@example.com.

        send_email("Привет!", "user@example", "admin@company.com")
        # Невозможно отправить письмо с адреса admin@company.com на адрес user@example

        send_email("Привет!", "user@example.com", "admin@company.com")
        # НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса admin@company.com на адрес user@example.com.

        send_email("Привет!", "user@example.com", "user@example.com")
        # Нельзя отправить письмо самому себе!