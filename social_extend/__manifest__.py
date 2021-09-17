# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Social Marketing Extend',
    'category': 'Marketing/Social Marketing Extend',
    'sequence': 175,
    'summary': 'Manage your social media and website visitors',
    'version': '1.2.1',
    'description': """Manage your social media and website visitors Extended""",
    'website': 'https://www.odoo.com/app/social-marketing',
    'depends': ['social'],
    'qweb': [
        'static/src/xml/social_templates.xml',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/social_post_template_views.xml',

    ],
    'application': True,
    'installable': True,
    'license': 'OEEL-1',
}