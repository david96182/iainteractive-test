from django.core.exceptions import ValidationError


def validate_age(value):
    """
    This function validates the age of the applicants
    The age must be between 7 and 99
    """
    if len(str(value)) != 2:
        raise ValidationError(
            ("%(value)s must have only two digits"),
            params={"value": value},
        )


def validate_letters_only(value):
    """
    Validation for letters only
    """
    if not value.isalpha():
        raise ValidationError(
            ("%(value)s must contain only letters"),
            params={"value": value},
        )