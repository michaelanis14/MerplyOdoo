# -*- coding: utf-8 -*-
{
    'name': "Air Waybill",

    'summary': """
        This Module designed to store Air Waybill details """,

    'description': """
        MAWB, HAWB
    """,

    'author': "Ragaa Maher",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/mawb.xml',
        'views/hawb.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}