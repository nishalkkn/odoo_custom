{
    'name': "Machine Management",
    'application': True,
    'version': '17.0.1.0.4',
    'summary': 'Machine management, transfers and service',
    'description': """
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

        'security/security.xml',
        'security/record_rules.xml',
        'security/ir.model.access.csv',

        'data/machine_sequence.xml',
        'data/machine_type_data.xml',
        'data/product_product_data.xml',
        'data/email_template.xml',
        'data/ir_cron_data.xml',

        'wizard/machine_wizard_view.xml',
    ],

    'license': 'LGPL-3',

}
