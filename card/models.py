from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from cms.utils.compat.dj import python_2_unicode_compatible
import os


try:
    from cms.models import get_plugin_media_path
except ImportError:
    def get_plugin_media_path(instance, filename):
        """
        See cms.models.pluginmodel.get_plugin_media_path
        on django CMS 3.0.4+ for information
        """
        return instance.get_media_path(filename)


@python_2_unicode_compatible
class CardPlugin(CMSPlugin):
    """
    Card Plugin Information
    """
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=50,
        help_text=_('Enter Title of Card'),
    )

    url = models.URLField(
        _('Absolute URL'),
        blank=True,
        null=True
    )

    description = models.CharField(
        verbose_name=_('Description'),
        max_length=500,
        help_text=_('Enter Dscription'),
    )

    image = models.ImageField(
        _("image"),
        upload_to=get_plugin_media_path,
        null=True,
    )

    alt = models.CharField(
        _("alternate text"), max_length=255, blank=True, null=True,
        help_text=_("Specifies an alternate text for an image, if the image"
                    "cannot be displayed.<br />Is also used by search engines"
                    "to classify the image."))

    def __unicode__(self):
        return self.title

    def __str__(self):
        if self.alt:
            return self.alt[:40]
        elif self.image:
            # added if, because it raised attribute error when file wasn't
            # defined.
            try:
                return u"%s" % os.path.basename(self.image.name)
            except AttributeError:
                pass
        return u"<empty>"

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
