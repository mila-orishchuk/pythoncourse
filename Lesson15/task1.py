'''
Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.

Email validations:

https://help.xmatters.com/ondemand/trial/valid_email_format.htm 

https://en.wikipedia.org/wiki/Email_address 
'''
import re

class ValidateEmail(object):
    def __init__(self, email: str, *args, **kwargs):
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not ValidateEmail.validate(value):
            raise ValueError(f'Invalid email address "{value}"')
        self._email = value


    @staticmethod
    def validate(email):
        regex = '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
        return bool(re.search(regex, email))


if __name__ == '__main__':
    try:
        email = 'abc-d.qwe@mail.com'
        em = ValidateEmail(email)
        assert em.email == email
        email1 ='abc-dmail.com'
        em1 = ValidateEmail(email1)
        em1 = ValidateEmail(email1)
        assert em1.email == email1
    except ValueError as error:
        print(error)
