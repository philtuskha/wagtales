# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 00:06
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20170519_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internalpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('halfs_block', wagtail.wagtailcore.blocks.StructBlock([(b'photo', wagtail.wagtailimages.blocks.ImageChooserBlock(classname='img')), (b'title', wagtail.wagtailcore.blocks.CharBlock(classname='title', required=True)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock())], classname='full title')), ('person', wagtail.wagtailcore.blocks.StructBlock([(b'first_name', wagtail.wagtailcore.blocks.CharBlock(classname='fname', required=True)), (b'surname', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'photo', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'biography', wagtail.wagtailcore.blocks.RichTextBlock())]))]),
        ),
    ]
