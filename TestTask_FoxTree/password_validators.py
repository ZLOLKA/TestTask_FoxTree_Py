from django.core.exceptions import ValidationError
import re


class TwoNumbersValidator:
    """
    Validate whether the password is have 2 numbers
    """
    def validate(self, password, user=None):
        if not re.search(r"\d(\D)*\d", password):
            raise ValidationError("This password don't have 2 numbers")

    def get_help_text(self):
        return "Your password must contain at least 2 numbers."


class TwoLatinValidator:
    """
    Validate whether the password is have 2 latin symbol
    """
    def validate(self, password, user=None):
        if not re.search(r"[A-Za-z][^A-Za-z]*[A-Za-z]", password):
            raise ValidationError("This password don't have 2 latin symbol")

    def get_help_text(self):
        return "Your password must contain at least 2 latin characters."


class SpecialCharValidator:
    """
    Validate whether the password is have special symbol
    """
    def validate(self, password, user=None):
        if set(password).isdisjoint(set("[]{}()<>\"'/|\\,.!@#$%^&*_-+=`~:;?")):
            raise ValidationError("This password don't have special symbol")

    def get_help_text(self):
        return "Your password must contain at least special characters."
