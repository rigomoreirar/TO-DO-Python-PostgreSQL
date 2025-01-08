from infrastructure.utilities.validators import validate_email

class EmailAddress:
    def __init__(self, email: str):
        if not validate_email(email):
            raise ValueError(f"Invalid email address: {email}")
        self.email = email

    def __str__(self):
        return self.email

    def __eq__(self, other):
        return isinstance(other, EmailAddress) and self.email == other.email