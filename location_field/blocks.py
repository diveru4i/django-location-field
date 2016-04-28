# -*- coding: utf-8 -*-
from wagtail.wagtailcore.blocks import FieldBlock

from location_field.forms.plain import PlainLocationField


class PlainLocationBlock(FieldBlock):
    def __init__(self, required=True, help_text=None, **kwargs):
        kwargs.update({'is_wagtail_block': True})
        self.field = PlainLocationField(**kwargs)
        super(PlainLocationBlock, self).__init__(**kwargs)
