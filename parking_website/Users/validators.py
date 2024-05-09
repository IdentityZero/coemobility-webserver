from django.core.exceptions import ValidationError
import re

def validate_password_strength(value):
    if not re.search(r'[A-Z]', value):
        raise ValidationError('Password must contain at least one uppercase letter.')
    if not re.search(r'[a-z]', value):
        raise ValidationError('Password must contain at least one lowercase letter.')
    if not re.search(r'\d', value):
        raise ValidationError('Password must contain at least one digit.')
    # if not re.search(r'[!@#$%^&*()_+]', value):
    #     raise ValidationError('Password must contain at least one special character.')

def validate_numerics_in_charfields(value):
    if re.search(r'[A-Z]', value):
        raise ValidationError('Must only be numerical values (0-9)')
    if re.search(r'[a-z]', value):
        raise ValidationError('Must only be numerical values (0-9)')
