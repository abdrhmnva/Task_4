import datetime
import re
import random

class UserUtil:
    @staticmethod
    def generate_user_id():
        year_prefix = str(datetime.now().year)[-2:]
        random_digits = ''.join(str(random.randint(0, 9)) for _ in range(7))
        return int(year_prefix + random_digits)

    @staticmethod
    def generate_password():
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
        while True:
            password = ''.join(random.choice(chars) for _ in range(8))
            if (re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) and
                    re.search(r"\d", password) and re.search(r"[!@#$%^&*()]", password)):
                return password

    @staticmethod
    def is_strong_password(password):
        return (len(password) >= 8 and
                bool(re.search(r"[A-Z]", password)) and
                bool(re.search(r"[a-z]", password)) and
                bool(re.search(r"\d", password)) and
                bool(re.search(r"[!@#$%^&*()]", password)))

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"

    @staticmethod
    def validate_email(email):
        pattern = r"^[a-z]+\.[a-z]+@[a-z]+\.[a-z]{2,}$"
        return bool(re.match(pattern, email))
