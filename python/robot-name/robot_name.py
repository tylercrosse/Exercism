import string
import random


class Robot(object):
    used_names = set()

    def __init__(self):
        self.reset()

    def random_name(self):
        letters = [random.choice(string.ascii_uppercase) for _ in range(2)]
        numbers = [random.choice(string.digits) for _ in range(3)]
        name = ''.join(letters + numbers)
        return name

    def generate_random_name(self):
        while True:
            new_random_name = self.random_name()
            if new_random_name not in self.used_names:
                return new_random_name

    def reset(self):
        self.name = self.generate_random_name()
        self.used_names.add(self.name)