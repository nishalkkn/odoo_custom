{
    'name': 'Tolerance',
    'version': '17.0.1.0.1',
    'application': True,
    'summary': 'Tolerance',
    'discription': """
    This module deals with tolerance of a customer 
    """,
    'depends': [
        'base',
        'contacts',
        'sale',
        'purchase',
        'stock',
    ],
    'data': [
        'views/res_partner.xml',
        'views/sale_order.xml',
        'views/purchase_order.xml',
        'views/stock_picking.xml',

        'wizard/tolerance_wizard_view.xml',

        'security/ir.model.access.csv',
    ],
    'license': 'LGPL-3',
}
