from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    tolerance = fields.Float('Tolerance', compute='_compute_tolerance_so', inverse='_inverse_tolerance_so', store=True)

    @api.depends('order_id.partner_id')
    def _compute_tolerance_so(self):
        """computing the tolerance field in sale order line"""
        for rec in self:
            rec.write({
                'tolerance': rec.order_id.partner_id.tolerance
            })

    def _inverse_tolerance_so(self):
        """inverse function for making tolerance field in sale order line editable"""
        pass
