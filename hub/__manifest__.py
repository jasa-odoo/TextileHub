# -*- coding: utf-8 -*-
{
    'name': "Textile Hub",
    'depends': ['base','stock','sale_management','account','sale_project','social'],
    'data': [
        'security/ir.model.access.csv',
        'views/hub_products_views.xml',
        'views/machine_type_view.xml',
        'views/material_type_view.xml',
        'views/payment_term_view.xml',
        'views/hub_colour_view.xml',
        'views/hub_delivery.xml',
        'views/hub_menus.xml',
        'views/sale_order_views.xml',
        'report/hub_product_reports.xml',
        'report/hub_product_templates.xml',
        'wizard/hub_delivery_views.xml',
    ],
    'demo':[
        "demo/demo_data.xml"
        
    ],


    'application': True,
    'license': 'LGPL-3',
    'images': ['static/description/icon.png']
}
