from django.core.exceptions import ValidationError


def validate_if_words_there(*args):
    global validation_args
    validation_args = args
    return validate


def validate(value):
    words = set(validation_args)
    cleaned_value = set(value.lower().split())

    deifference = words - cleaned_value

    if len(deifference) == len(words):
        raise ValidationError(f'Обязательно использовать {words}')
