"""
the-economist - Project X_periment.

Python3.x
"""

from factory.indecon import Indecon
from statistics import fmean, mean


class Abacus():
    """
    Indicadores Economicos.

    Se debe conectar por lo menos a un servicio de https://www.indecon.online/
    para obtener uno o varios indicadores economicos.
    """

    def __init__(self, app_name="abacus"):
        """Initialize service endpoint."""
        self.app_name = app_name

    def index_page(self):
        """
        /indecon.

        Get All Apis information.
        """
        self.response = Indecon(self.app_name).index_page()
        return self.response

    def date_page(self, key, date):
        """
        /indecon/date/cobre/02-01-2020.

        Entrega el valor de un elemento particular en una fecha en particular.
        """
        self.response = Indecon(self.app_name).date_page(key, date)
        return self.response

    def last_page(self):
        """
        /indecon/last.

        API que entrega los últimos valores de todos los elementos.
        """
        self.response = Indecon(self.app_name).last_page()
        return self.response

    def values_page(self, key):
        """
        /indecon/values/cobre.

        API que entrega todos los valores de un elemento particular.
        """
        self.response = Indecon(self.app_name).values_page(key)
        return self.response

    def statistics_element(self, element):
        """
        Calcularemos el promedio.

        Desde values obtendremos la informacion por elemento.
        Usaremos 3 metodos: default mean, float mean y calculo manual.
        """
        self.response = None
        self.values = self.values_page(element)

        if isinstance(self.values.get("data"), dict):
            self.values_data = self.values.get("data").get("values")

            self.values_list = [
                value for value in self.values_data.values()
            ]

            self.lenofvalues = len(self.values_list)
            self.sumofvalues = sum(self.values_list)
            self.meanofvalues = fmean(self.values_list)
            self.fmeanofvalues = mean(self.values_list)
            self.avgcomputofvalues = float(self.sumofvalues) / self.lenofvalues

            self.response["data"] = {
                "avg_stat-dmn": self.meanofvalues,
                "avg_stat-fmn": self.fmeanofvalues,
                "avg_comp-ute": self.avgcomputofvalues,
                "sum": self.sumofvalues,
                "len": self.lenofvalues
            }

        return self.response
