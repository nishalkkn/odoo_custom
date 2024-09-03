from odoo import fields, models, api, _


class StockMove(models.Model):
    _inherit = 'stock.move'

    tolerance = fields.Float('Tolerance', compute='_compute_tolerance_delivery')

    @api.depends('sale_line_id')
    def _compute_tolerance_delivery(self):
        """computing the tolerance for delivery orders"""
        for rec in self:
            rec.write({
                'tolerance': rec.sale_line_id.tolerance
            })


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        """validation button for confirmation"""
        res = super().button_validate()
        for rec in self.move_ids_without_package:
            max_tolerance = rec.product_uom_qty + rec.tolerance
            min_tolerance = rec.product_uom_qty - rec.tolerance
            if rec.quantity < min_tolerance or rec.quantity > max_tolerance:
                return {'type': 'ir.actions.act_window',
                        'name': _('Tolerance warning'),
                        'res_model': 'tolerance.wizard',
                        'view_mode': 'form',
                        'view_type': 'form',
                        'context': {'default_stock_picking_id': self.id},
                        'target': 'new',
                        }
        return res
