# -*- coding: utf-8 -*-
# Copyright 2021 Morwi Encoders Consulting SA de CV
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Geosoft Customizations',
    'version': '14.0.1.0.0',
    'category': 'Hidden',
    'summary': 'View Customizations for Geosoft',
    'license': 'LGPL-3',
    'depends': [
        'sale_management',
        'crm',
        'sale_crm',
        'sale_purchase'
    ],
    'description': "This module contains the view customizations for Geosoft",
    'data': [
        'views/sale_order_view.xml',
        'views/crm_view.xml',
        'views/purchase_view.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
}
