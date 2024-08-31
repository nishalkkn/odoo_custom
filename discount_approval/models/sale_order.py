# -*- coding: utf-8 -*-

from odoo import models, fields

class SaleOrderApprove(models.Model):
    _inherit = 'sale.order'

    # state = fields.Selection(selection_add=[('approval_request','Approval Request')])
    state = fields.Selection([
        ('draft', "Quotation"),
        ('approval_request', 'Approval Request'),
        ('sent', "Quotation Sent"),
        ('sale', "Sales Order"),
        ('cancel', "Cancelled")],
        string="Status",
        readonly=True, copy=False, index=True,
        tracking=3,
        default='draft')

    def hello(self):
        discount_limit = self.env['ir.config_parameter'].sudo().get_param('discount_approval.discount_limit')

        amount_without_disc = 0
        for rec in self.order_line:
            price_tax_incl = rec.price_total + ((rec.discount * rec.price_unit) / 100)
            amount_without_disc += price_tax_incl
        if self.amount_total < (amount_without_disc - float(discount_limit)):
            self.write({
                'state': 'approval_request'
            })

    def action_approve_so(self):
        self.write({
            'state': 'sent'
        })
