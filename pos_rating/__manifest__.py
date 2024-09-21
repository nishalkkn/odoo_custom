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
        'point_of_sale',
    ],

    'data': [
        'views/product.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_rating/static/src/xml/product_widget.xml',
            'pos_rating/static/src/xml/pos_screen.xml',
        ],
    },

    'license': 'LGPL-3',

}
