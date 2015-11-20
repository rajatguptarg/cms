from cms.models import CMSPlugin
from outlet_api import Outlet


class OutletPlugin(CMSPlugin):
    """
    CMS Plugin for Outlets
    """
    outlet = Outlet()

    name = 'Outlets'
    outlet_details = outlet.get_outlets()
    outlet_details = outlet_details['content']

    for outlet in outlet_details:
        image_url = "http://172.18.75.2/bial/images/outlets/normal/"
        image_url += outlet['code'] + ".png"
        outlet['image'] = image_url

    def __unicode__(self):
        return self.name


class RetailPlugin(CMSPlugin):
    """
    CMS Plugin for Retail Outlets
    """
    outlet = Outlet()

    name = 'Retail'
    retail_outlets = outlet.retail_outlets()
    retail_categories = outlet.retail_categories()
    retail_categories = retail_categories['content']
    retail_outlets = retail_outlets['content']

    for outlet in retail_outlets:
        image_url = "http://172.18.75.2/bial/images/outlets/normal/"
        image_url += outlet['code'] + ".png"
        outlet['image'] = image_url

    def __unicode__(self):
        return self.name
