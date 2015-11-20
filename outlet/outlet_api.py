import json
import requests
from collections import defaultdict
from bial import settings


class Outlet:
    """
    Outlet Details
    """
    def __init__(self):
        self.outlet_details = defaultdict()

    def get_outlets(self):
        """
        Return list of outlets
        """
        _api = settings.API_URL
        _response = requests.get(_api)
        self.outlet_details = json.loads(_response.content)

        return self.outlet_details

    def retail_categories(self):
        """
        Categories for retail outlet
        """
        _api = 'http://172.18.75.2/cs/categories?type=Retail'
        _response = requests.get(_api)
        Outlet.retail_categories = json.loads(_response.content)

        return Outlet.retail_categories

    def retail_outlets(self):
        """
        Return list of outlets
        """
        _api = 'http://172.18.75.2/cs/outlets?type=Retail'
        _response = requests.get(_api)
        self.outlet_details = json.loads(_response.content)

        return self.outlet_details
