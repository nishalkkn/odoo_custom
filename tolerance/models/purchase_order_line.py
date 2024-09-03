from odoo import fields, models, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    tolerance = fields.Float('Tolerance', compute='_compute_tolerance_po', inverse='_inverse_tolerance_po', store=True)

    @api.depends('order_id.partner_id')
    def _compute_tolerance_po(self):
        """computing the tolerance field in purchase order line"""
        for rec in self:
            rec.write({
                'tolerance': rec.order_id.partner_id.tolerance
            })

    def _inverse_tolerance_po(self):
        """inverse function for making tolerance field in purchase order line editable"""
        pass
