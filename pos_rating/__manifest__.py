{
    'name': 'POS Rating',
    'application': True,
    'version': '17.0.1.0.1',
    'summary': 'Rating filed in the POS',
    'description': """
This is a base module for setting a rating field in POS product view
    """,

    'depends': [
        'base',
        'product',
    ],

    'data':[
        'views/product.xml',
    ],

    'license': 'LGPL-3',

}
