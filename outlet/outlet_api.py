import os
import json
import requests
from collections import defaultdict


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
        _api = os.getenv('API_URL', None)
        _response = requests.get(_api)
        self.outlet_details = json.loads(_response.content)

        return self.outlet_details
