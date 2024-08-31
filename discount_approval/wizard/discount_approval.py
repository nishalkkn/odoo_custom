# -*- coding: utf-8 -*-

from odoo import models, fields


class DiscountApproval(models.TransientModel):
    _inherit = "res.config.settings"

    _is_discount_limit = fields.Boolean('Discount limit', config_parameter='discount_approval._is_discount_limit',
                                        help='Check this field for enabling discount limit')
    discount_limit = fields.Float('Limit amount', config_parameter='discount_approval.discount_limit',
                                    help='The discount limit amount  ')


