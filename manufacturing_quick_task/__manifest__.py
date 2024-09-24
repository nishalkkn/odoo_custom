{
    'name': 'Manufacturing quick task',
    'application': True,
    'version': '17.0.1.0.1',
    'summary': 'Manufacturing quick task',
    'description': """
    This module provide a extra charge adding filed in manufacturing.
    """,

    'depends': [
        'base',
        'mrp',
        'account',
    ],
    'data': [
        'views/manufacturing.xml',
        'views/extra_cost.xml',

        'security/ir.model.access.csv',
    ],

    'license': 'LGPL-3'

}
