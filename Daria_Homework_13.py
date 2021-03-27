import random
import string

def create_str(min_limit, max_limit):
    len_str = random.randint(min_limit, max_limit)
    alphabet = string.ascii_letters
    my_str = "".join([random.choice(alphabet) for _ in range(len_str)])
    return my_str

class EmailGenerator:


    def __init__(self, ):
        self._email = self.create_email()

    @property

    def email(self):
        return self._email

    def create_email(self):
        my_string = create_str(5, 7)

        numb = random.randint(100, 999)

        names = ["king", "miller", "kean"]
        name = random.choice(names)

        domains = ["net", "com", "ua"]
        domain = random.choice(domains)

        create_email = f"{name}.{numb}@{my_string}.{domain}"
        return create_email


test_create = EmailGenerator()

email = test_create.email
print(email)
