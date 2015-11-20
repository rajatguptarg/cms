from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from outlet.models import OutletPlugin, RetailPlugin
from django.utils.translation import ugettext as _


class CMSOutletPlugin(CMSPluginBase):
    model = OutletPlugin  # model where plugin data are saved
    name = _("Outlet")  # name of the plugin in the interface
    render_template = "outlet_details.html"

    def render(self, context, instance, placeholder):
        context.update({
            'outlets': instance,
            'placeholder': placeholder,
        })
        return context


class CMSRetailPlugin(CMSPluginBase):
    model = RetailPlugin  # model where plugin data are saved
    name = _("Retail")  # name of the plugin in the interface
    render_template = "retail_outlets.html"

    def render(self, context, instance, placeholder):
        context.update({
            'retail': instance,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(CMSOutletPlugin)  # register the plugin
plugin_pool.register_plugin(CMSRetailPlugin)  # register the plugin
