{
    'name': 'Discount Approval',
    'application': True,
    'version': '17.0.1.0.1',
    'summary': 'Discount Approval',
    'description': """
    
    """,

    'depends': [
        'sale',
    ],
    'data': [
        'views/sale_order.xml',

        'wizard/discount_approval.xml',
    ],

    'license': 'LGPL-3'

}
