{
    'name': "Machine Management",
    'application': True,
    'version': '17.0.1.0.9',
    'summary': 'Machine management, transfer and service',
    'description': """
This is a base module for managing machine and machine transfer and machine service
    """,

    'depends': [
        'base',
        'mail',
        'product',
        'contacts',
        'hr',
        'account',
        'website',
    ],

    'data': [
        'views/machine_management.xml',
        'views/machine_transfer.xml',
        'views/machine_part_view.xml',
        'views/res_partner_view.xml',
        'views/machine_service_view.xml',
        'views/website_menu.xml',
        'views/website_template.xml',
        'views/snippet.xml',
        'views/static_snippet.xml',

        'security/security.xml',
        'security/record_rules.xml',
        'security/ir.model.access.csv',

        'data/machine_sequence.xml',
        'data/machine_type_data.xml',
        'data/product_product_data.xml',
        'data/email_template.xml',
        'data/ir_cron_data.xml',

        'wizard/machine_wizard_view.xml',

        'report/ir_actions_report.xml',
        'report/machine_transfer_report.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'machine_management/static/src/js/action_manager.js'
        ],
        # 'web.assets_frontend': [
        #     'machine_management/static/src/js/best_seller_snippet.js',
        #     'machine_management/static/src/xml/best_seller_snippet_templates.xml',
        # ],
    },

    'license': 'LGPL-3',

}
