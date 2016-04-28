# -*- coding: utf-8 -*-
from wagtail.wagtailcore import hooks


@hooks.register('insert_editor_js')
def editor_js():
    files = [
        '/static/location_field/js/googlemaps.api.js',
        '/static/location_field/js/jquery.livequery.js',
        '/static/location_field/js/form.js',
    ]

    includes = '\n'.join(['<script src="%s"></script>' % filename for filename in files])

    return includes
