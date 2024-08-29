from odoo import models, _, fields, api


class SaleOrderPayment(models.Model):
    _inherit = 'sale.order'

    # invoice_state = fields.Char(default="def")

    def action_register_payment(self):
        if self.invoice_ids.state == 'posted':
            return {
                'name': _('Register Payment'),
                'res_model': 'account.payment.register',
                'view_mode': 'form',
                'views': [[False, 'form']],
                'context': {
                    'active_model': 'account.move',
                    'active_ids': self.invoice_ids.id,
                },
                'target': 'new',
                'type': 'ir.actions.act_window',
            }
