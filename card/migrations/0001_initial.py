# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.pluginmodel


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(help_text='Enter Title of Card', max_length=50, verbose_name='Title')),
                ('url', models.URLField(null=True, verbose_name='Absolute URL', blank=True)),
                ('description', models.CharField(help_text='Enter Dscription', max_length=500, verbose_name='Description')),
                ('image', models.ImageField(upload_to=cms.models.pluginmodel.get_plugin_media_path, null=True, verbose_name='image')),
                ('alt', models.CharField(help_text='Specifies an alternate text for an image, if the imagecannot be displayed.<br />Is also used by search enginesto classify the image.', max_length=255, null=True, verbose_name='alternate text', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
