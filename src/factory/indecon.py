from helpers.services import Services


class Indecon():
    """
    Se debe conectar por lo menos a un servicio de https://www.indecon.online/
    para obtener uno o varios indicadores económicos.
    """

    def __init__(self, app_name="indecon"):
        self.app_name = app_name
        self.url = "https://www.indecon.online"

    def index_page(self):
        """
        All Apis information
        """
        # https://www.indecon.online/
        self.response = Services(self.app_name).request(self.url)
        return self.response

    def date_page(self, key, date):
        """
        API que entrega el valor de un elemento particular en una fecha en particular
        """
        # https://www.indecon.online/date/cobre/02-01-2020
        self.url = "{}/date/{}/{}".format(self.url, key, date)
        self.response = Services(self.app_name).request(self.url)
        return self.response

    def last_page(self):
        """
        API que entrega los últimos valores de todos los elementos
        """
        # https://www.indecon.online/last
        self.url = self.url + "/last"
        self.response = Services(self.app_name).request(self.url)
        return self.response

    def values_page(self, key):
        """
        API que entrega todos los valores de un elemento particular
        """
        # https://www.indecon.online/values/cobre
        self.url = "{}/values/{}".format(self.url, key)
        self.response = Services(self.app_name).request(self.url)
        return self.response
