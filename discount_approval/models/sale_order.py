# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderApprove(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection([
        ('draft', "Quotation"),
        ('approval_request', 'Approval Request'),
        ('sent', "Quotation Sent"),
        ('sale', "Sales Order"),
        ('cancel', "Cancelled")],
        string="Status",
        readonly=True, copy=False, index=True,
        tracking=1,
        default='draft')

    @api.model
    def action_confirm(self):
        """confirm button"""
        res = super(SaleOrderApprove, self).action_confirm()
        is_discount_limit = self.env['ir.config_parameter'].sudo().get_param('discount_approval._is_discount_limit')
        if is_discount_limit:

            if not self.env.user.has_group('sales_team.group_sale_manager'):

                discount_type = self.env['ir.config_parameter'].sudo().get_param('discount_approval.discount_type')
                apply_on = self.env['ir.config_parameter'].sudo().get_param('discount_approval.apply_on')
                amount_without_disc = 0

                for rec in self.order_line:
                    if rec.price_total > 0:

                        if apply_on == 'tax_included_price':
                            tax = (rec.tax_id.amount * rec.price_unit) / 100
                            price_tax_incl = rec.price_total + ((rec.discount / 100) * (tax + rec.price_unit))
                            amount_without_disc += price_tax_incl

                        else:
                            price_tax_excl = rec.price_subtotal + ((rec.discount / 100) * rec.price_unit)
                            amount_without_disc += price_tax_excl

                if discount_type == 'fixed_amount':
                    discount_limit_fixed = self.env['ir.config_parameter'].sudo().get_param(
                        'discount_approval.discount_limit_fixed')
                    if self.amount_total < (amount_without_disc - float(discount_limit_fixed)):
                        self.write({
                            'state': 'approval_request'
                        })

                else:
                    discount_limit_percentage = self.env['ir.config_parameter'].sudo().get_param(
                        'discount_approval.discount_limit_percentage')
                    if self.amount_total < (
                            amount_without_disc - ((float(discount_limit_percentage)) * amount_without_disc)):
                        self.write({
                            'state': 'approval_request'
                        })

                return res

    def action_approve_so(self):
        """approve so button for manager"""
        self.write({
            'state': 'sale'
        })
