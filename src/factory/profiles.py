"""
the-economist - Project X_periment.

Python3.x
"""

from helpers.dummies import Dummies
#from statistics import fmean, mean


class Profiles():
    """Profiles Users."""

    def __init__(self, app_name="profiles"):
        """Initialize factory Profiles."""
        self.app_name = app_name

    def index_page(self):
        """
        /.

        Get profiles with limit configuration.
        """
        query = "select 1"
        self.response = Dummies().db(query, limit=20)
        return self.response

    # def statistics_element(self, element):
    #     """
    #     Calcularemos el promedio.
    #
    #     Desde values obtendremos la informacion por elemento.
    #     Usaremos 3 metodos: default mean, float mean y calculo manual.
    #     """
    #     self.response = None
    #     self.values = self.values_page(element)
    #
    #     if isinstance(self.values.get("data"), dict):
    #         self.values_data = self.values.get("data").get("values")
    #
    #         self.values_list = [
    #             value for value in self.values_data.values()
    #         ]
    #
    #         self.lenofvalues = len(self.values_list)
    #         self.sumofvalues = sum(self.values_list)
    #         self.meanofvalues = fmean(self.values_list)
    #         self.fmeanofvalues = mean(self.values_list)
    #         self.avgcomputofvalues = float(self.sumofvalues) / self.lenofvalues
    #
    #         self.response["data"] = {
    #             "avg_stat-dmn": self.meanofvalues,
    #             "avg_stat-fmn": self.fmeanofvalues,
    #             "avg_comp-ute": self.avgcomputofvalues,
    #             "sum": self.sumofvalues,
    #             "len": self.lenofvalues
    #         }
    #
    #     return self.response
