# -*- coding: utf-8 -*-
{
    'name' : 'Real Estate',
    'version' : '1.0',
    'summary': 'Real estate advertising app',
    'sequence': 10,
    'description': """
       This app used for the training purpose
       of Al Khidma System.

    """,
    'category': 'sales',
    'website': 'www.alkhidmasystems.com',

    'depends' : ['base'],
    'data': [

     'security/ir.model.access.csv',
          
     'view/property.xml',
     'view/customer.xml',
     'data/data.xml',
    ],
    'demo': [
        'data/data.xml',

    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}
