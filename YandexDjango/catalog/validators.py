from django.core.exceptions import ValidationError


def validate_if_words_there(value):
    words = {'превосходно', 'роскошно'}
    cleaned_value = set(value.lower().split())

    deifference = words - cleaned_value

    if len(deifference) == len(words):
        raise ValidationError(f'Обязательно использовать {words}')

    return value
