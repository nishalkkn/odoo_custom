{
    'name': "Machine Management",
    'application': True,
    'version': '17.0.1.0.1',
    'category' : 'Sales/Sales',
    'description' : """
This is a base module for managing machines 
    """,

    'depends': [
        'base',
        'mail'
    ],

    'data': [
        'views/machine_management.xml',

        'security/ir.model.access.csv',

        'data/my_module_sequence.xml',
    ]
}
