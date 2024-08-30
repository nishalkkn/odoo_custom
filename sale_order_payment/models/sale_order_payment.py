from odoo import models, _, fields, api


class SaleOrderPayment(models.Model):
    _inherit = 'sale.order'

    payment = fields.Boolean(default=False)
    button_state = fields.Selection(selection=[('hidden', 'Hidden'), ('visible', 'Visible')], required=True, copy=False,
                                    store=True, tracking=True, default='hidden', compute='_compute_button_state')
    fully_paid_ribbon = fields.Boolean(default=False)
    partial_paid_ribbon = fields.Boolean(default=False)

    def action_register_payment(self):
        """button for register payment in sale order"""
        return {
            'name': _('Register Payment'),
            'res_model': 'account.payment.register',
            'view_mode': 'form',
            'views': [[False, 'form']],
            'context': {
                'active_model': 'account.move',
                'active_ids': self.invoice_ids.ids,
            },
            'target': 'new',
            'type': 'ir.actions.act_window',
        }

    @api.depends('invoice_ids.payment_state', 'invoice_ids.state')
    def _compute_button_state(self):
        """computing the button state"""
        if self.invoice_ids:
            var = self.invoice_ids.mapped('payment_state')
            for rec in self.invoice_ids:
                if rec.state == 'posted':
                    self.write({
                        'button_state': 'visible'
                    })
                if 'paid' in var:
                    self.write({
                        'partial_paid_ribbon': True
                    })
            if 'paid' in var and 'not_paid' not in var:
                self.write({
                    'button_state': 'hidden',
                    'partial_paid_ribbon': False,
                    'fully_paid_ribbon': True
                })
