import re

from django.core.exceptions import ValidationError


def validate_if_words_there(*args):
    global validation_args
    validation_args = args
    return validate


def validate(value):
    words = set(validation_args)
    value = value.lower()

    if len(re.findall('|'.join(words), value)) < 1:
        raise ValidationError(f'Обязательно использовать {words}')
