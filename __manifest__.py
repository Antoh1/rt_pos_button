# -*- coding: utf-8 -*-
{
    'name': "rt_pos_button",

    'summary': """
        Added action button to POS screen""",

    'description': """
        Action Button
    """,

    'author': "RopeTech Solutions",
    'website': "http://www.ropetech.co.ke",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale', 'base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    "qweb": ["static/src/xml/rt_pos_btn.xml"],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
