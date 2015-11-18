from django.test import TestCase
from outlet_api import Outlet


class OutletTest(TestCase):
    """
    Test Case of Outlets
    """
    outletes = Outlet()

    def test_outlets(self):
        try:
            response = self.outletes.get_outlets()
            if not response.content:
                self.fail('API is not working')
        except:
            self.fail('Set Environment Varibale, it is not set!')
