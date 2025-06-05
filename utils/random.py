import string
import random

class Random:
    @staticmethod
    def get_random_letter_string(length: int):
        return ''.join(random.choices(string.ascii_letters, k=length))
