import time
import requests
import requests_cache
from wrapper import RESPONSE


class Services():
    """
    """

    def __init__(self, name_cache="default", expire_after=300):
        self.time_init = time.time()
        self.name_cache = name_cache
        self.expire_after = expire_after

        requests_cache.install_cache(
            self.name_cache,
            expire_after=self.expire_after
        )

    def request(self, url, format=None, routes=None):
        self.url = url
        self.routes = routes
        self.data = requests.get(url)

        RESPONSE["cache"] = self.data.from_cache
        RESPONSE["data"] = self.data.json()
        RESPONSE["backend_time"] = time.time() - self.time_init
        return RESPONSE
