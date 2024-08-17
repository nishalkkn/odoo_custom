from odoo import models, fields


class Coc(models.Model):
    _inherit = 'mrp.bom'

    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('approved', 'Approved'),
    ], string='Status', required=True, copy=False,
        tracking=True, default='draft')
