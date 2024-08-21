# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    machine_id = fields.One2many('machine.management', 'customer_id', string="Machine")
    alternative_cust_ids = fields.Many2many('machine.management', compute="compute_employee_machine_count")

    # domain setting for machine_id
    @api.depends('name')
    def compute_employee_machine(self):
        self.alternative_cust_ids = self.env['machine.management'].search([('customer_id', '=', self.name)])

    def action_archive(self):
        if self.active == False:
            print("Hello")