from odoo import fields, models


class ExtraCostManufacturing(models.Model):
    _name = 'extra.cost'

    charge = fields.Float('Charge', help="Extra charge")
    description = fields.Text('Description', help="Description")
    manufacture_id = fields.Many2one('mrp.production')
