"""
the-economist - Project X_periment.

Python3.x
"""
import time
from faker import Faker
from helpers.wrapper import RESPONSE


class Dummies:
    """Get data for tests mocks or whatever."""

    def __init__(self):
        """Initialize Dummies."""
        self.time_init = time.time()
        self.dummy = []
        self.response = {}
        self.dummer = Faker()

    def db(self, query, limit=10):
        """
        Get data, with Faker similar, to MySQL*.

        Use limit for the total rows,
        in the future example queries for mapping will be supported
        """
        self.limit = limit
        self.query = query

        for num in range(self.limit):
            self.name = self.dummer.name()
            self.mount = self.dummer.random_number()
            self.descriptor = self.dummer.text()
            self.address = self.dummer.address()

            self.row = [
                self.name,
                self.mount,
                self.descriptor,
                self.address,
                str(num+1).zfill(4)
            ]
            self.dummy.append(self.row)

        RESPONSE["data"] = self.dummy
        RESPONSE["backend_time"] = time.time() - self.time_init

        return RESPONSE
