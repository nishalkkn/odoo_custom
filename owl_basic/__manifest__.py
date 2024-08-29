{
    'name': 'Odoo basic',
    'application': True,
    'version': '1.0.0',
    'description': '''
This is a module for Odoo demo
    ''',

    'data': [
        'views/client_action.xml',
    ],
    'assets': {
        'web.assets_backend': [
            # 'owl_basic/static/src/js/**',
            'owl_basic/static/src/xml/**',

        ]
    },

    'license': 'LGPL-3'
}
