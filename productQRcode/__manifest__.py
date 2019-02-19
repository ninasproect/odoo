# -*- coding: utf-8 -*-
{
    'name': "Product QR Code",

    'summary': "Add a qr code to product",

    'description': """
       
    """,

    'author': "Ninas Softs",
    'website': "",


    'category': 'Product',
    'version': '0.1',
    'license': 'LGPL-3',
    'images': ['images/QRcode.png'],
    #'price': 4.99,
    #'currency': 'EUR',
    'depends': ['base','product'],
    'data': [
        #views
        'views/product_template.xml',
        #reports
        'reports/product_template_qr_code.xml',

    ],
    "external_dependencies": {"python": ['qrcode'], "bin": []},

    'application': False,
}
