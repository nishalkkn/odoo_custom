{
    'name': "Machine Management",
    'application': True,
    'version': '17.0.4.0.0',
    'category' : 'Sales/Sales',
    'description' : """
This is a base module for managing machines and machine transfers
    """,

    'depends': [
        'base',
        'mail',
        'product',
        'contacts',
        'hr',
        'account',
    ],

    'data': [
        'views/machine_management.xml',
        'views/machine_transfer.xml',
        'views/machine_part_view.xml',
        'views/res_partner_view.xml',
        'views/machine_service_view.xml',

        'security/ir.model.access.csv',

        'data/machine_sequence.xml',
        'data/machine_type_data.xml'
    ],

    'license': 'LGPL-3',

}
