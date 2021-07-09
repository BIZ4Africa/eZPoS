# -*- coding: utf-8 -*-

{
    'name': 'Custom Laundry Management',
    'version': '14.0.1.0.0',
    'summary': """Complete Laundry Service Management""",
    'description': 'This module is very useful to manage all process of laundry service',
    "category": "BIZ4A",
    'author': 'BIZ4A',
    'company': 'BIZ4A Techno Solutions',
    'website': "https://www.biz-4-africa.com",
    'depends': ['base', 'mail', 'sale', 'account', 'uom'],
    'data': [
        'views/laundry.xml',
        'data/data.xml',
    ],
    'images': [],
    'license': 'AGPL-3',
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
