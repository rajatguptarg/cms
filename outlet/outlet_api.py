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
