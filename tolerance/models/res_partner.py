from odoo import models, fields


class Tolerance(models.Model):
    _inherit = 'res.partner'

    tolerance = fields.Float('Tolerance', help="Tolerance for customer")
