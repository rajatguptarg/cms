from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from card.models import CardPlugin
from django.utils.translation import ugettext as _


class CMSCardPlugin(CMSPluginBase):
    model = CardPlugin  # model where plugin data are saved
    name = _("Card")  # name of the plugin in the interface
    render_template = "card_details.html"

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context

plugin_pool.register_plugin(CMSCardPlugin)  # register the plugin
