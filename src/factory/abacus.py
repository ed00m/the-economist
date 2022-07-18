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
        response = Indecon(self.app_name).index_page()
        return response

    def date_page(self, key, date):
        """
        /indecon/date/cobre/02-01-2020.

        Entrega el valor de un elemento particular en una fecha en particular.
        """
        response = Indecon(self.app_name).date_page(key, date)
        return response

    def last_page(self):
        """
        /indecon/last.

        API que entrega los últimos valores de todos los elementos.
        """
        response = Indecon(self.app_name).last_page()
        return response

    def values_page(self, key):
        """
        /indecon/values/cobre.

        API que entrega todos los valores de un elemento particular.
        """
        response = Indecon(self.app_name).values_page(key)
        values = [value for value in response.get("data").get("values").values()]
        response["data"]["values"] = values[:10]
        return response

    def statistics_element(self, element):
        """
        Calcularemos el promedio.

        Desde values obtendremos la informacion por elemento.
        Usaremos 3 metodos: default mean, float mean y calculo manual.
        """
        response = {}
        values = self.values_page(element)

        if isinstance(values.get("data"), dict):
            values_data = values.get("data").get("values")
            values_list  = values_data

            lenofvalues = len(values_list)
            sumofvalues = sum(values_list)
            meanofvalues = fmean(values_list)
            fmeanofvalues = mean(values_list)
            avgcomputofvalues = float(sumofvalues) / lenofvalues

            response["data"] = {
                "avg_stat-dmn": meanofvalues,
                "avg_stat-fmn": fmeanofvalues,
                "avg_comp-ute": avgcomputofvalues,
                "sum": sumofvalues,
                "len": lenofvalues
            }

        return response


    def profiles_page(self):
        """
        /indecon/last.

        API que entrega los últimos valores de todos los elementos
        y crea un perfil de los indicadores
        """
        response = {}
        profiles = []
        response_last = self.last_page()

        for element, value in response_last["data"].items():
            response_statistics = self.statistics_element(element)
            response_values = self.values_page(element)

            value["profile"] = response_statistics.get("data")
            value["values"] = response_values.get("data").get("values")
            profiles.append(value)
        
        response["data"] = profiles
        return response
