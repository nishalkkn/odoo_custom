# -*- coding: utf-8 -*-
from odoo import fields, models


class ManufacturingBill(models.Model):
    _inherit = 'account.move'

    manufacture_id = fields.Many2one('mrp.production', 'Manufacturing id')
