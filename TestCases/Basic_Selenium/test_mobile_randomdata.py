# utilities/random_data.py

import random

class RandomData:

    @staticmethod
    def generate_mobile():
        return str(random.randint(6000000000, 9999999999))

