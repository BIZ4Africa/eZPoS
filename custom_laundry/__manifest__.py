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
    'depends': ['base', 'laundry_management'],
    'data': [
        'data/order_receipt_paper.xml',
        'views/laundry.xml',
        'data/data.xml',
        'views/laundry_order_receipt.xml'
    ],
    'images': [],
    'license': 'AGPL-3',
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
