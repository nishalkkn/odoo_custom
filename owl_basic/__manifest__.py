# -*- coding: utf-8 -*-

{
    'name': 'Owl Basics',
    'version': '17.0.1.0.0',
    'category': 'website',
    'summary': """Owl Basic""",
    'depends': ['base'],
    'data': [
        'views/client_action.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'owl_basic/static/src/js/**',
            'owl_basic/static/src/xml/**',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}