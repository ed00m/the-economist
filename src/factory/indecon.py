"""
the-economist - Project X_periment.

Python3.x
"""

from helpers.services import Services


class Indecon():
    """
    Indicadores Economicos.

    Se debe conectar por lo menos a un servicio de https://www.indecon.space/
    para obtener uno o varios indicadores economicos.
    """

    def __init__(self, app_name="indecon"):
        """Initialize service endpoint."""
        self.app_name = app_name
        self.url = "https://www.indecon.space"

    def index_page(self):
        """
        https://www.indecon.space/.

        Get All Apis information.
        """
        self.response = Services(self.app_name).request(self.url)
        return self.response

    def date_page(self, key, date):
        """
        https://www.indecon.space/date/cobre/02-01-2020.

        Entrega el valor de un elemento particular en una fecha en particular.
        """
        self.url = "{}/date/{}/{}".format(self.url, key, date)
        self.response = Services(self.app_name).request(self.url)
        return self.response

    def last_page(self):
        """
        https://www.indecon.space/last.

        API que entrega los últimos valores de todos los elementos.
        """
        self.url = self.url + "/last"
        self.response = Services(self.app_name).request(self.url)
        return self.response

    def values_page(self, key):
        """
        https://www.indecon.space/values/cobre.

        API que entrega todos los valores de un elemento particular.
        """
        self.url = "{}/values/{}".format(self.url, key)
        self.response = Services(self.app_name).request(self.url)
        return self.response
