from odoo import models, fields, api


class MachinePart(models.Model):
    _name = "machine.part"
    _description = "Machine Part"

    machine_id = fields.Many2one('machine.management', 'Machine')
    product_id = fields.Many2one('product.product', 'Machine Parts')
    quantity = fields.Integer('Quantity')
    uom = fields.Char('Unit of measure')

    # auto assigning uom
    @api.onchange('product_id')
    def onchange_machine_id(self):
        self.write({
            'uom': self.product_id.uom_id.name
        })
