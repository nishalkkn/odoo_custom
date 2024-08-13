{
    'name': "Machine Management",
    'application': True,
    'version': '17.0.1.0.2',
    'category' : 'Sales/Sales',
    'description' : """
This is a base module for managing machines and machine transfers
    """,

    'depends': [
        'base',
        'mail',
    ],

    'data': [
        'views/machine_management.xml',
        'views/machine_transfer.xml',

        'security/ir.model.access.csv',

        'data/machine_sequence.xml',
        'data/machine_type_data.xml'
    ]
}
