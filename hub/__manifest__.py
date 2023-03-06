# -*- coding: utf-8 -*-
{
    'name': "Textile Hub",
    'depends': ['website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/hub_machine_views.xml',
        'views/hub_assecories_view.xml',
        'views/hub_materials_view.xml',
        'views/machine_type_view.xml',
        'views/material_type_view.xml',
        'views/operating_type_view.xml',
        'views/payment_term_view.xml',
        'views/hub_colour_view.xml',
        'views/hub_delivery.xml',
        'views/hub_menus.xml'
    ],
    'application': True,
    'license': 'LGPL-3',
    'images': ['static/description/icon.png']
}
