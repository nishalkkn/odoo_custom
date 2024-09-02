# -*- coding: utf-8 -*-

from odoo import models, fields


class DiscountApproval(models.TransientModel):
    _inherit = "res.config.settings"

    _is_discount_limit = fields.Boolean('Discount limit', config_parameter='discount_approval._is_discount_limit',
                                        help='Check this field for enabling discount limit')
    discount_type = fields.Selection([('fixed_amount', 'Fixed Amount'), ('percentage', 'Percentage')], 'Discount Type',
                                     default='fixed_amount', config_parameter='discount_approval.discount_type')
    apply_on = fields.Selection(
        [('tax_included_price', 'Tax included price'), ('tax_excluded_price', 'Tax excluded price')], 'Apply on',
        default='tax_included_price', config_parameter='discount_approval.apply_on')
    discount_limit_fixed = fields.Float('Limit', config_parameter='discount_approval.discount_limit_fixed',
                                        help='The discount limit')
    discount_limit_percentage = fields.Float('Limit', config_parameter='discount_approval.discount_limit_percentage',
                                             help='The discount limit')
