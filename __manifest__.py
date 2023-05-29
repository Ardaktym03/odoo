# -*- coding: utf-8 -*-
{
    'name' : 'MSY RESTAURANT',
    'version' : '1.1',
    'summary': 'MSY RESTAURANT',
    'sequence': -100,
    'description': """MSY RESTAURANT""",
    'category': 'Accounting/Accounting',
    'website': '',
    'author': 'Kuderbek Ardaktym',
    'depends' : ['sale'],
    'images': ['static/img/msy_logo.png'],
    'data': [
        'security/ir.model.access.csv',
        'report/bill_template.xml',
        'views/menu_item_view.xml',
        'views/table_view.xml',
        'views/bill_menu_view.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
